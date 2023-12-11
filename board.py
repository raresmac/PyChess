import pieces


class Board:
    def __init__(self):
        self.board = []
        self.players = [None, None]
        self.check = False
        self.checkmate = False
        self.move = 0
        for i in range(9):
            lst = []
            for j in range(9):
                lst.append(None)
            self.board.append(lst)
        # white pieces
        self.board[1][1] = pieces.Rook(self, 1, 1, 'w')
        self.board[1][2] = pieces.Knight(self, 1, 2, 'w')
        self.board[1][3] = pieces.Bishop(self, 1, 3, 'w')
        self.board[1][4] = pieces.Queen(self, 1, 4, 'w')
        self.board[1][5] = pieces.King(self, 1, 5, 'w')
        self.board[1][6] = pieces.Bishop(self, 1, 6, 'w')
        self.board[1][7] = pieces.Knight(self, 1, 7, 'w')
        self.board[1][8] = pieces.Rook(self, 1, 8, 'w')
        for i in range(1, 9):
            self.board[2][i] = pieces.Pawn(self, 2, i, 'w')

        # black pieces
        self.board[8][1] = pieces.Rook(self, 8, 1, 'b')
        self.board[8][2] = pieces.Knight(self, 8, 2, 'b')
        self.board[8][3] = pieces.Bishop(self, 8, 3, 'b')
        self.board[8][4] = pieces.Queen(self, 8, 4, 'b')
        self.board[8][5] = pieces.King(self, 8, 5, 'b')
        self.board[8][6] = pieces.Bishop(self, 8, 6, 'b')
        self.board[8][7] = pieces.Knight(self, 8, 7, 'b')
        self.board[8][8] = pieces.Rook(self, 8, 8, 'b')
        for i in range(1, 9):
            self.board[7][i] = pieces.Pawn(self, 7, i, 'b')

    def get_cell(self, x, y):
        return self.board[x][y]

    def set_cell(self, x, y, piece):
        ord_x, ord_y = piece.get_coords()
        other = self.move * (-1) + 1

        # moving the rook removes castling option
        if self.players[self.move] and isinstance(piece, pieces.Rook):
            if piece == self.board[1][1]:
                self.players[0].get_piece(0).no_castle_queen()
            elif piece == self.board[1][8]:
                self.players[0].get_piece(0).no_castle_king()
            elif piece == self.board[8][1]:
                self.players[1].get_piece(0).no_castle_queen()
            elif piece == self.board[8][8]:
                self.players[1].get_piece(0).no_castle_king()

        # castling
        if self.players[self.move] and isinstance(piece, pieces.King):
            castle_king, castle_queen = piece.get_castle()
            if y - ord_y > 1 and castle_king:
                if self.move == 0:
                    self.set_move()
                    self.set_cell(ord_x, ord_y + 1, self.board[1][8])
                else:
                    self.set_move()
                    self.set_cell(ord_x, ord_y + 1, self.board[8][8])
            elif ord_y - y > 1 and castle_queen:
                if self.move == 0:
                    self.set_move()
                    self.set_cell(ord_x, ord_y - 1, self.board[1][1])
                else:
                    self.set_move()
                    self.set_cell(ord_x, ord_y - 1, self.board[8][1])
            piece.no_castle_king()
            piece.no_castle_queen()

        # removing all en passant from the other player
        if self.players[other]:
            other_pieces = self.players[other].get_pieces()
            for a_piece in other_pieces:
                if isinstance(a_piece, pieces.Pawn) and a_piece.get_en_pass():
                    a_piece.set_en_pass()

        # preparing en passant
        if self.players[self.move] and isinstance(piece, pieces.Pawn):
            if piece.get_start() and abs(x - ord_x) == 2:
                piece.set_en_pass()

        # en passant
        if self.players[self.move] and isinstance(piece, pieces.Pawn) and not self.board[x][y] and y != ord_y:
            if self.move == 0:
                if self.players[other]:
                    self.players[other].lose_piece(self.board[x - 1][y])
                self.board[x - 1][y] = None
            else:
                if self.players[other]:
                    self.players[other].lose_piece(self.board[x + 1][y])
                self.board[x + 1][y] = None
            print('Get wrecked, noob!')

        # removing double jump from pawn
        if self.players[self.move] and isinstance(piece, pieces.Pawn):
            piece.unset_start()

        if self.players[other]:
            self.players[other].lose_piece(self.board[x][y])

        self.board[ord_x][ord_y] = None
        self.board[x][y] = piece
        piece.set_cell(x, y)
        self.set_move()

    def get_move(self):
        return self.move

    def set_move(self):
        self.move = self.move * (-1) + 1

    def get_players(self):
        return self.players

    def set_players(self, player_w, player_b):
        self.players[0] = player_w
        self.players[1] = player_b

    def update_available_moves(self):
        other = self.move * (-1) + 1
        nr_pieces = self.players[self.move].get_nr_pieces()
        for i in range(nr_pieces):
            self.players[self.move].get_piece(i).check_moves(self)
            # for j in self.players[self.move].get_piece(i).get_available_moves():
            #     work in progress
        nr_pieces = self.players[other].get_nr_pieces()
        for i in range(nr_pieces):
            self.players[other].get_piece(i).check_moves(self)

    def check_check(self):
        other = self.move * (-1) + 1
        king = self.players[self.move].get_piece(0).get_coords()
        nr_pieces = self.players[other].get_nr_pieces()
        for i in nr_pieces:
            moves = self.players[other].get_piece(i).get_available_moves()
            if king in moves:
                return True
        return False

    def draw_check(self):
        if self.check_check():
            return False
        for i in range(self.players[self.move].get_nr_pieces()):
            moves = self.players[self.move].get_piece(i).get_available_moves()
            if moves:
                return False
        return True

    def checkmate_check(self):
        if not self.check_check():
            return False
        for i in range(self.players[self.move].get_nr_pieces()):
            moves = self.players[self.move].get_piece(i).get_available_moves()
            if moves:
                return False
        return True
