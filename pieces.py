def borders(x, y):
    if 1 <= x <= 8 and 1 <= y <= 8:
        return True
    else:
        return False


class Piece:
    def __init__(self, ord_x, ord_y):
        self.ord_x = ord_x
        self.ord_y = ord_y
        self.available_moves = []

    def check_moves(self, board): pass


class Pawn(Piece):
    def __init__(self, ord_x, ord_y, color):
        Piece.__init__(self, ord_x, ord_y)
        self.en_pass = False
        self.start = True
        self.color = color

    def check_moves(self, game_board):
        if self.color == 'w':
            if not game_board.board[self.ord_x][self.ord_y + 1].piece:
                self.available_moves.append((self.ord_x, self.ord_y + 1))
                if self.start and game_board.board[self.ord_x][self.ord_y + 2] == '':
                    self.available_moves.append((self.ord_x, self.ord_y + 2))
            if game_board.board[self.ord_x + 1][self.ord_y + 1].piece.color and borders(self.ord_x + 1, self.ord_y + 1):
                if game_board.board[self.ord_x + 1][self.ord_y + 1].piece.color == 'b':
                    self.available_moves.append((self.ord_x + 1, self.ord_y + 1))
            if game_board.board[self.ord_x - 1][self.ord_y + 1].piece.color and borders(self.ord_x - 1, self.ord_y + 1):
                if game_board.board[self.ord_x - 1][self.ord_y + 1].piece.color == 'b':
                    self.available_moves.append((self.ord_x - 1, self.ord_y + 1))
        else:
            if not game_board.board[self.ord_x][self.ord_y - 1].piece:
                self.available_moves.append((self.ord_x, self.ord_y - 1))
                if self.start and game_board.board[self.ord_x][self.ord_y - 2] == '':
                    self.available_moves.append((self.ord_x, self.ord_y - 2))
            if game_board.board[self.ord_x + 1][self.ord_y - 1].piece.color and borders(self.ord_x + 1, self.ord_y - 1):
                if game_board.board[self.ord_x + 1][self.ord_y - 1].piece.color == 'w':
                    self.available_moves.append((self.ord_x + 1, self.ord_y + 1))
            if game_board.board[self.ord_x - 1][self.ord_y - 1].piece.color and borders(self.ord_x - 1, self.ord_y - 1):
                if game_board.board[self.ord_x - 1][self.ord_y - 1].piece.color == 'w':
                    self.available_moves.append((self.ord_x - 1, self.ord_y - 1))
