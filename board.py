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
        self.board[ord_x][ord_y] = None
        self.board[x][y] = piece
        print(piece, x, y)
        piece.set_cell(x, y)
        print(piece.get_coords())

        # castling
        if self.players[self.move] and piece == self.players[self.move].get_piece(0):
            if y - ord_y > 1:
                if self.move == 0:
                    self.set_move()
                    self.set_cell(ord_x, ord_y + 1, self.board[1][8])
                else:
                    self.set_move()
                    self.set_cell(ord_x, ord_y + 1, self.board[8][8])
            elif ord_y - y > 1:
                if self.move == 0:
                    self.set_move()
                    self.set_cell(ord_x, ord_y - 1, self.board[1][1])
                else:
                    self.set_move()
                    self.set_cell(ord_x, ord_y - 1, self.board[8][1])

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

    def castling(self, choice):
        choice = 0
        # de facut
