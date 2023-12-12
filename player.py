import pieces


class Player:
    def __init__(self, game_board, color):
        self.game_board = game_board
        self.color = color
        self.pieces = []
        if color == 'w':
            x1 = 1
            x2 = 2
        else:
            x1 = 8
            x2 = 7
        self.pieces.append(game_board.get_cell(x1, 5))  # king
        self.pieces.append(game_board.get_cell(x1, 4))  # queen
        self.pieces.append(game_board.get_cell(x1, 1))  # rook 1
        self.pieces.append(game_board.get_cell(x1, 8))  # rook 2
        self.pieces.append(game_board.get_cell(x1, 3))  # bishop 1
        self.pieces.append(game_board.get_cell(x1, 6))  # bishop 2
        self.pieces.append(game_board.get_cell(x1, 2))  # knight 1
        self.pieces.append(game_board.get_cell(x1, 7))  # knight 2

        self.pieces.append(game_board.get_cell(x2, 1))  # pawn 1
        self.pieces.append(game_board.get_cell(x2, 2))  # pawn 2
        self.pieces.append(game_board.get_cell(x2, 3))  # pawn 3
        self.pieces.append(game_board.get_cell(x2, 4))  # pawn 4
        self.pieces.append(game_board.get_cell(x2, 5))  # pawn 5
        self.pieces.append(game_board.get_cell(x2, 6))  # pawn 6
        self.pieces.append(game_board.get_cell(x2, 7))  # pawn 7
        self.pieces.append(game_board.get_cell(x2, 8))  # pawn 8

    def get_locations(self):
        locations = []
        for i in self.pieces:
            locations.append(i.get_coords())
        return locations

    def get_piece(self, index: int):
        return self.pieces[index]

    def get_pieces(self):
        return self.pieces

    def get_nr_pieces(self):
        return len(self.pieces)

    def lose_piece(self, piece):
        for i in range(len(self.pieces)):
            if self.pieces[i] == piece:
                del self.pieces[i]
                return

    def add_piece(self, piece):
        self.pieces.append(piece)

    def promote(self, x, y, choice):
        for i in range(len(self.pieces)):
            if (x, y) == self.pieces[i].get_coords():
                if choice == 'Q':
                    self.pieces[i] = pieces.Queen(self.game_board, x, y, self.color)
                elif choice == 'R':
                    self.pieces[i] = pieces.Rook(self.game_board, x, y, self.color)
                elif choice == 'B':
                    self.pieces[i] = pieces.Bishop(self.game_board, x, y, self.color)
                elif choice == 'N':
                    self.pieces[i] = pieces.Knight(self.game_board, x, y, self.color)
                return self.pieces[i]
