def borders(x, y):
    if 1 <= x <= 8 and 1 <= y <= 8:
        return True
    else:
        return False


class Piece:
    """Overall class for all pieces.
    """
    def __init__(self, board, ord_x, ord_y, color):
        """Initialize with the Board object, the coordinates and the color.

        Keyword arguments:
        board -- Board object that contains the piece
        ord_x -- row
        ord_y -- file
        color -- color of the piece
        """
        self.ord_x = ord_x
        self.ord_y = ord_y
        self.color = color
        board.set_cell(ord_x, ord_y, self)
        self.available_moves = []

    def __str__(self):
        """String for printing. Mainly for debugging.
        """
        return str(self.__class__) + ':' + str(self.ord_x) + ' ' + str(self.ord_y) + '-' + str(self.color)

    def check_moves(self, board): pass

    def get_available_moves(self):
        """Get all available moves from the current position.
        """
        return self.available_moves

    def clear_moves(self):
        """Remove all the moves from this piece's array.
        """
        self.available_moves.clear()

    def remove_moves(self, moves):
        """Remove specific moves from this piece's array.

        Keyword arguments:
        moves -- moves to be removed
        """
        for i in moves:
            self.available_moves.remove(i)

    def set_cell(self, x, y):
        """Change the position of the piece.

        Keyword arguments:
        x -- new row
        y -- new file
        """
        self.ord_x = x
        self.ord_y = y

    def get_coords(self):
        """Return the coordinates of the piece.
        """
        return self.ord_x, self.ord_y

    def get_color(self):
        """Return the color of the piece.
        """
        return self.color

    def get_move(self, index):
        """Return the available move of the piece in the current position from a specific index.

        Keyword arguments:
        index -- position of the move in the array
        """
        return self.available_moves[index]


class Pawn(Piece):
    """Class for the pawns.
    """
    def __init__(self, board, ord_x, ord_y, color):
        """Initializing with the super class and specific values for the pawn.
        """
        Piece.__init__(self, board, ord_x, ord_y, color)
        self.en_pass = False
        self.start = True

    def get_en_pass(self):
        """Get if the pawn can be en-passant-ed.
        """
        return self.en_pass

    def set_en_pass(self):
        """Change the value of en-passant.
        """
        self.en_pass = not self.en_pass

    def get_start(self):
        """Get if the pawn is at the starting cell.
        """
        return self.start

    def unset_start(self):
        """Set the pawn as moved.
        """
        self.start = False

    def check_moves(self, game_board):
        """Update the move array with the available moves.

        Keyword arguments:
        game_board -- Board object that contains this pawn
        """
        self.clear_moves()
        if self.color == 'w':
            if borders(self.ord_x + 1, self.ord_y) and not game_board.board[self.ord_x + 1][self.ord_y]:
                self.available_moves.append((self.ord_x + 1, self.ord_y))
                if self.start and not game_board.board[self.ord_x + 2][self.ord_y]:
                    self.available_moves.append((self.ord_x + 2, self.ord_y))
            if borders(self.ord_x + 1, self.ord_y + 1) and game_board.board[self.ord_x + 1][self.ord_y + 1]:
                if game_board.board[self.ord_x + 1][self.ord_y + 1].color:
                    if game_board.board[self.ord_x + 1][self.ord_y + 1].color == 'b':
                        self.available_moves.append((self.ord_x + 1, self.ord_y + 1))
            if borders(self.ord_x + 1, self.ord_y - 1) and game_board.board[self.ord_x + 1][self.ord_y - 1]:
                if game_board.board[self.ord_x + 1][self.ord_y - 1].color:
                    if game_board.board[self.ord_x + 1][self.ord_y - 1].color == 'b':
                        self.available_moves.append((self.ord_x + 1, self.ord_y - 1))
        else:
            if borders(self.ord_x - 1, self.ord_y) and not game_board.board[self.ord_x - 1][self.ord_y]:
                self.available_moves.append((self.ord_x - 1, self.ord_y))
                if self.start and not game_board.board[self.ord_x - 2][self.ord_y]:
                    self.available_moves.append((self.ord_x - 2, self.ord_y))
            if borders(self.ord_x - 1, self.ord_y - 1) and game_board.board[self.ord_x - 1][self.ord_y - 1]:
                if game_board.board[self.ord_x - 1][self.ord_y - 1].color:
                    if game_board.board[self.ord_x - 1][self.ord_y - 1].color == 'w':
                        self.available_moves.append((self.ord_x - 1, self.ord_y - 1))
            if borders(self.ord_x - 1, self.ord_y + 1) and game_board.board[self.ord_x - 1][self.ord_y + 1]:
                if game_board.board[self.ord_x - 1][self.ord_y + 1].color:
                    if game_board.board[self.ord_x - 1][self.ord_y + 1].color == 'w':
                        self.available_moves.append((self.ord_x - 1, self.ord_y + 1))

        # en passant
        if self.color == 'w':
            if borders(self.ord_x, self.ord_y + 1) and game_board.board[self.ord_x][self.ord_y + 1]:
                if game_board.board[self.ord_x][self.ord_y + 1].color == 'b':
                    if isinstance(game_board.board[self.ord_x][self.ord_y + 1], Pawn):
                        if game_board.board[self.ord_x][self.ord_y + 1].get_en_pass():
                            self.available_moves.append((self.ord_x + 1, self.ord_y + 1))
            if borders(self.ord_x, self.ord_y - 1) and game_board.board[self.ord_x][self.ord_y - 1]:
                if game_board.board[self.ord_x][self.ord_y - 1].color == 'b':
                    if isinstance(game_board.board[self.ord_x][self.ord_y - 1], Pawn):
                        if game_board.board[self.ord_x][self.ord_y - 1].get_en_pass():
                            self.available_moves.append((self.ord_x + 1, self.ord_y - 1))
        else:
            if borders(self.ord_x, self.ord_y + 1) and game_board.board[self.ord_x][self.ord_y + 1]:
                if game_board.board[self.ord_x][self.ord_y + 1].color == 'w':
                    if isinstance(game_board.board[self.ord_x][self.ord_y + 1], Pawn):
                        if game_board.board[self.ord_x][self.ord_y + 1].get_en_pass():
                            self.available_moves.append((self.ord_x - 1, self.ord_y + 1))
            if borders(self.ord_x, self.ord_y - 1) and game_board.board[self.ord_x][self.ord_y - 1]:
                if game_board.board[self.ord_x][self.ord_y - 1].color == 'w':
                    if isinstance(game_board.board[self.ord_x][self.ord_y - 1], Pawn):
                        if game_board.board[self.ord_x][self.ord_y - 1].get_en_pass():
                            self.available_moves.append((self.ord_x - 1, self.ord_y - 1))


class King(Piece):
    """Class for the kings.
    """
    def __init__(self, board, ord_x, ord_y, color):
        """Initializing with the super class and specific values for the king.
        """
        Piece.__init__(self, board, ord_x, ord_y, color)
        self.castle_king = True
        self.castle_queen = True
        self.move_coords_x = [-1, -1, 0, 1, 1, 1, 0, -1]
        self.move_coords_y = [0, 1, 1, 1, 0, -1, -1, -1]

    def get_castle(self):
        """Get if this king can castle.
        """
        return self.castle_king, self.castle_queen

    def no_castle_king(self):
        """Set that this king can't castle kingside.
        """
        self.castle_king = False

    def no_castle_queen(self):
        """Set that this king can't castle queenside.
        """
        self.castle_queen = False

    def check_moves(self, game_board):
        """Update the move array with the available moves.

        Keyword arguments:
        game_board -- Board object that contains this pawn
        """
        self.clear_moves()
        for i in range(8):
            new_x = self.ord_x + self.move_coords_x[i]
            new_y = self.ord_y + self.move_coords_y[i]
            if not borders(new_x, new_y):
                continue
            if not game_board.board[new_x][new_y] or game_board.board[new_x][new_y].color != self.color:
                ok = True
                # king near king
                for j in range(8):
                    new_new_x = new_x + self.move_coords_x[j]
                    new_new_y = new_y + self.move_coords_y[j]
                    if new_new_x != self.ord_x or new_new_y != self.ord_y:
                        if borders(new_new_x, new_new_y) and isinstance(game_board.board[new_new_x][new_new_y], King):
                            ok = False
                            break
                if ok:
                    self.available_moves.append((new_x, new_y))

        # castling kingside
        if (self.castle_king and borders(self.ord_x, self.ord_y + 1) and not game_board.board[self.ord_x][self.ord_y + 1]
                and borders(self.ord_x, self.ord_y + 2) and not game_board.board[self.ord_x][self.ord_y + 2]):
            self.available_moves.append((self.ord_x, self.ord_y + 2))

        # castling queenside
        if (self.castle_queen and borders(self.ord_x, self.ord_y - 1) and not game_board.board[self.ord_x][self.ord_y - 1]
                and borders(self.ord_x, self.ord_y - 2) and not game_board.board[self.ord_x][self.ord_y - 2]
                and borders(self.ord_x, self.ord_y - 3) and not game_board.board[self.ord_x][self.ord_y - 3]):
            self.available_moves.append((self.ord_x, self.ord_y - 2))


class Rook(Piece):
    def __init__(self, board, ord_x, ord_y, color):
        """Initializing with the super class.
        """
        Piece.__init__(self, board, ord_x, ord_y, color)

    def check_moves(self, game_board):
        """Update the move array with the available moves.

        Keyword arguments:
        game_board -- Board object that contains this pawn
        """
        self.clear_moves()
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
        """Initializing with the super class.
        """
        Piece.__init__(self, board, ord_x, ord_y, color)

    def check_moves(self, game_board):
        """Update the move array with the available moves.

        Keyword arguments:
        game_board -- Board object that contains this pawn
        """
        self.clear_moves()
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
        """Initializing with the super class.
        """
        Piece.__init__(self, board, ord_x, ord_y, color)

    def check_moves(self, game_board):
        """Update the move array with the available moves.

        Keyword arguments:
        game_board -- Board object that contains this pawn
        """
        self.clear_moves()
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
        """Initializing with the super class and specific values for the knight.
        """
        Piece.__init__(self, board, ord_x, ord_y, color)
        self.coord_x = [-2, -1, 1, 2, 2, 1, -1, -2]
        self.coord_y = [1, 2, 2, 1, -1, -2, -2, -1]

    def check_moves(self, game_board):
        """Update the move array with the available moves.

        Keyword arguments:
        game_board -- Board object that contains this pawn
        """
        self.clear_moves()
        for i in range(8):
            new_x = self.ord_x + self.coord_x[i]
            new_y = self.ord_y + self.coord_y[i]
            if borders(new_x, new_y):
                if not game_board.board[new_x][new_y] or game_board.board[new_x][new_y].color != self.color:
                    self.available_moves.append((new_x, new_y))
