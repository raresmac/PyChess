import pieces


class Board:
    def __init__(self):
        self.board = []
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
        self.check = False
        self.checkmate = False
        self.move = 'w'

    @staticmethod
    def check_check(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] is pieces.King:
                    if self.board[i][j].color == 'w':
                        white_king = (i, j)
                    else:
                        black_king = (i, j)


    def get_cell(self, x, y):
        return self.board[x][y]

    def set_cell(self, x, y, piece):
        self.board[x][y] = piece
        piece.set_cell(x, y)
