def borders(x, y):
    if 1 <= x <= 8 and 1 <= y <= 8:
        return True
    else:
        return False


class Piece:
    def __init__(self, board, ord_x, ord_y, color):
        self.ord_x = ord_x
        self.ord_y = ord_y
        self.color = color
        board.set_cell(ord_x, ord_y, self)
        self.available_moves = []

    def check_moves(self, board): pass

    def get_available_moves(self):
        return self.available_moves

    def set_cell(self, x, y):
        self.ord_x = x
        self.ord_y = y

    def get_coords(self):
        return self.ord_x, self.ord_y

    def get_color(self):
        return self.color


class Pawn(Piece):
    def __init__(self, board, ord_x, ord_y, color):
        Piece.__init__(self, board, ord_x, ord_y, color)
        self.en_pass = False
        self.start = True

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


class King(Piece):
    def __init__(self, board, ord_x, ord_y, color):
        Piece.__init__(self, board, ord_x, ord_y, color)
        self.castle_king = True
        self.castle_queen = True
        self.move_coords_x = [-1, -1, 0, 1, 1, 1, 0, -1]
        self.move_coords_y = [0, 1, 1, 1, 0, -1, -1, -1]

    def check_moves(self, game_board):
        for i in range(8):
            new_x = self.ord_x + self.move_coords_x[i]
            new_y = self.ord_y + self.move_coords_y[i]
            if not borders(new_x, new_y):
                continue
            if not game_board.board[new_x][new_y] or game_board.board[new_x][new_y].color != self.color:
                self.available_moves.append((new_x, new_y))
        if (self.castle_king and not game_board.board[self.ord_x + 1][self.ord_y]
                and not game_board.board[self.ord_x + 2][self.ord_y]):
            self.available_moves.append((self.ord_x + 2, self.ord_y))
        if (self.castle_queen and not game_board.board[self.ord_x - 1][self.ord_y]
                and not game_board.board[self.ord_x - 2][self.ord_y]
                and not game_board.board[self.ord_x - 3][self.ord_y]):
            self.available_moves.append((self.ord_x - 2, self.ord_y))


class Rook(Piece):
    def __init__(self, board, ord_x, ord_y, color):
        Piece.__init__(self, board, ord_x, ord_y, color)

    def check_moves(self, game_board):
        def moving(new_x, new_y):
            if not borders(new_x, new_y):
                return False
            if not game_board.board[new_x][new_y]:
                self.available_moves.append((new_x, new_y))
                return True
            elif game_board.board[new_x][new_y].color != self.color:
                self.available_moves.append((new_x, new_y))
                return False
            else:
                return False

        for i_left in range(1, 8):
            new_x = self.ord_x - i_left
            new_y = self.ord_y
            if not moving(new_x, new_y):
                break

        for i_right in range(1, 8):
            new_x = self.ord_x + i_right
            new_y = self.ord_y
            if not moving(new_x, new_y):
                break

        for j_down in range(1, 8):
            new_x = self.ord_x
            new_y = self.ord_y - j_down
            if not moving(new_x, new_y):
                break

        for j_up in range(1, 8):
            new_x = self.ord_x
            new_y = self.ord_y + j_up
            if not moving(new_x, new_y):
                break


class Bishop(Piece):
    def __init__(self, board, ord_x, ord_y, color):
        Piece.__init__(self, board, ord_x, ord_y, color)

    def check_moves(self, game_board):
        def moving(new_x, new_y):
            if not borders(new_x, new_y):
                return False
            if not game_board.board[new_x][new_y]:
                self.available_moves.append((new_x, new_y))
                return True
            elif game_board.board[new_x][new_y].color != self.color:
                self.available_moves.append((new_x, new_y))
                return False
            else:
                return False

        for left_down in range(1, 8):
            new_x = self.ord_x - left_down
            new_y = self.ord_y - left_down
            if not moving(new_x, new_y):
                break

        for left_up in range(1, 8):
            new_x = self.ord_x - left_up
            new_y = self.ord_y + left_up
            if not moving(new_x, new_y):
                break

        for right_up in range(1, 8):
            new_x = self.ord_x + right_up
            new_y = self.ord_y + right_up
            if not moving(new_x, new_y):
                break

        for right_down in range(1, 8):
            new_x = self.ord_x + right_down
            new_y = self.ord_y - right_down
            if not moving(new_x, new_y):
                break


class Queen(Piece):
    def __init__(self, board, ord_x, ord_y, color):
        Piece.__init__(self, board, ord_x, ord_y, color)

    def check_moves(self, game_board):
        def moving(new_x, new_y):
            if not borders(new_x, new_y):
                return False
            if not game_board.board[new_x][new_y]:
                self.available_moves.append((new_x, new_y))
                return True
            elif game_board.board[new_x][new_y].color != self.color:
                self.available_moves.append((new_x, new_y))
                return False
            else:
                return False

        for i_left in range(1, 8):
            new_x = self.ord_x - i_left
            new_y = self.ord_y
            if not moving(new_x, new_y):
                break

        for i_right in range(1, 8):
            new_x = self.ord_x + i_right
            new_y = self.ord_y
            if not moving(new_x, new_y):
                break

        for j_down in range(1, 8):
            new_x = self.ord_x
            new_y = self.ord_y - j_down
            if not moving(new_x, new_y):
                break

        for j_up in range(1, 8):
            new_x = self.ord_x
            new_y = self.ord_y + j_up
            if not moving(new_x, new_y):
                break

        for left_down in range(1, 8):
            new_x = self.ord_x - left_down
            new_y = self.ord_y - left_down
            if not moving(new_x, new_y):
                break

        for left_up in range(1, 8):
            new_x = self.ord_x - left_up
            new_y = self.ord_y + left_up
            if not moving(new_x, new_y):
                break

        for right_up in range(1, 8):
            new_x = self.ord_x + right_up
            new_y = self.ord_y + right_up
            if not moving(new_x, new_y):
                break

        for right_down in range(1, 8):
            new_x = self.ord_x + right_down
            new_y = self.ord_y - right_down
            if not moving(new_x, new_y):
                break


class Knight(Piece):
    def __init__(self, board, ord_x, ord_y, color):
        Piece.__init__(self, board, ord_x, ord_y, color)
        self.coord_x = [-2, -1, 1, 2, 2, 1, -1, -2]
        self.coord_y = [1, 2, 2, 1, -1, -2, -2, -1]

    def check_moves(self, game_board):
        for i in range(8):
            new_x = self.ord_x + self.coord_x[i]
            new_y = self.ord_x + self.coord_y[i]

            if borders(new_x, new_y):
                if not game_board.board[new_x][new_y] or game_board.board[new_x][new_y].color != self.color:
                    self.available_moves.append((new_x, new_y))
