import random

import pygame
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

        self.images = None

    def get_image(self, color, piece, back):
        return self.images[color][piece][back]

    def set_images(self, images):
        self.images = images

    def get_check(self):
        return self.check

    def set_check(self, value):
        self.check = value

    def get_cell(self, x, y):
        return self.board[x][y]

    def set_cell(self, x, y, piece, promo='h'):
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

        # capturing the rook removes castling option
        if self.players[self.move] and x in (1, 8) and y in (1, 8):
            if (x, y) == (1, 1):
                self.players[0].get_piece(0).no_castle_queen()
            elif (x, y) == (1, 8):
                self.players[0].get_piece(0).no_castle_king()
            elif (x, y) == (8, 1):
                self.players[1].get_piece(0).no_castle_queen()
            elif (x, y) == (8, 8):
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

        # removing all en passants from the other player
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

        # removing double jump from pawn
        if self.players[self.move] and isinstance(piece, pieces.Pawn):
            piece.unset_start()

        # promoting
        if isinstance(piece, pieces.Pawn) and x in (1, 8):
            if promo == 'h':
                run = True
                timer = pygame.time.Clock()
                font = pygame.font.Font('freesansbold.ttf', 20)
                fps = 60
                screen = pygame.display.get_surface()
                pygame.draw.rect(screen, (255, 255, 255), [145, 195, 345, 165])
                promotion = font.render('Choose your piece:', True, (0, 0, 0))
                screen.blit(promotion, (220, 215))
                piece_pics = []
                for i in range(1, 5):
                    image = self.images[self.move][i][(x + y) % 2]
                    piece_pics.append(image)
                screen.blit(promotion, (220, 215))
                for i in range(4):
                    screen.blit(piece_pics[i], (175 + 68 * i, 250))
                pygame.display.update()
                while run:
                    timer.tick(fps)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                            pygame.quit()
                            exit()
                        elif event.type == pygame.MOUSEBUTTONDOWN:
                            if 175 <= event.pos[0] <= 175 + 68 * 4 and 250 <= event.pos[1] <= 318:
                                mouse_pos = (event.pos[0] - 175) // 68
                                choice = 'Q'
                                if mouse_pos == 1:
                                    choice = 'R'
                                elif mouse_pos == 2:
                                    choice = 'B'
                                elif mouse_pos == 3:
                                    choice = 'N'
                                piece = self.players[self.move].promote(ord_x, ord_y, choice)
                                run = False
                                self.set_move()
            else:
                choices = ['Q', 'R', 'B', 'N']
                choice = choices[random.randint(0, 3)]
                piece = self.players[self.move].promote(ord_x, ord_y, choice)
                self.set_move()

        if self.players[other] and self.board[x][y]:
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

    def set_cell_simulation(self, x, y, piece):
        ord_x, ord_y = piece.get_coords()
        aux_piece = self.board[x][y]
        other = self.move * (-1) + 1

        # simulation
        self.players[other].lose_piece(self.board[x][y])
        self.board[x][y] = piece
        piece.set_cell(x, y)
        self.board[ord_x][ord_y] = None
        self.update_available_moves(rec=False, mine=False)
        if self.check_check():
            self.board[x][y] = aux_piece
            if aux_piece:
                self.players[other].add_piece(aux_piece)
            self.board[ord_x][ord_y] = piece
            piece.set_cell(ord_x, ord_y)
            self.update_available_moves(rec=False, mine=False)
            return False
        self.board[x][y] = aux_piece
        if aux_piece:
            self.players[other].add_piece(aux_piece)
        self.board[ord_x][ord_y] = piece
        piece.set_cell(ord_x, ord_y)
        self.update_available_moves(rec=False, mine=False)
        return True

    def update_available_moves(self, rec=True, mine=True, oppo=True):
        other = self.move * (-1) + 1
        if mine:
            nr_pieces = self.players[self.move].get_nr_pieces()
            for i in range(nr_pieces):
                piece = self.players[self.move].get_piece(i)
                piece.check_moves(self)

        if oppo:
            nr_pieces = self.players[other].get_nr_pieces()
            for i in range(nr_pieces):
                piece = self.players[other].get_piece(i)
                piece.check_moves(self)

        if rec:
            nr_pieces = self.players[self.move].get_nr_pieces()
            for i in range(nr_pieces):
                piece = self.players[self.move].get_piece(i)
                moves = piece.get_available_moves()
                to_be_removed = []
                for j in moves:
                    if not self.set_cell_simulation(j[0], j[1], piece):
                        to_be_removed.append(j)
                if to_be_removed:
                    piece.remove_moves(to_be_removed)

    def check_check(self):
        other = self.move * (-1) + 1
        king = self.players[self.move].get_piece(0).get_coords()
        nr_pieces = self.players[other].get_nr_pieces()
        for i in range(nr_pieces):
            piece = self.players[other].get_piece(i)
            moves = piece.get_available_moves()
            if king in moves:
                return True
        return False


    def draw_check1(self):
        if self.check_check():
            return False
        for i in range(self.players[self.move].get_nr_pieces()):
            moves = self.players[self.move].get_piece(i).get_available_moves()
            if moves:
                return False
        return True


    def draw_check2(self):
        print('-----')
        print(self.players[0].get_nr_pieces())
        if self.players[0].get_nr_pieces() > 1:
            print(self.players[0].get_piece(1))
        print(self.players[1].get_nr_pieces())
        if self.players[1].get_nr_pieces() > 1:
            print(self.players[1].get_piece(1))
        if self.players[0].get_nr_pieces() == 1 and self.players[1].get_nr_pieces() == 1:
            return True
        elif self.players[0].get_nr_pieces() == 2 and self.players[1].get_nr_pieces() == 1:
            if isinstance(self.players[0].get_piece(1), pieces.Knight) or isinstance(self.players[0].get_piece(1), pieces.Bishop):
                return True
        elif self.players[0].get_nr_pieces() == 1 and self.players[1].get_nr_pieces() == 2:
            if isinstance(self.players[1].get_piece(1), pieces.Knight) or isinstance(self.players[1].get_piece(1), pieces.Bishop):
                return True
        return False


    def draw_check(self):
        if self.draw_check2():
            return True
        else:
            return self.draw_check1()


    def checkmate_check(self):
        if not self.check_check():
            return False
        for i in range(self.players[self.move].get_nr_pieces()):
            moves = self.players[self.move].get_piece(i).get_available_moves()
            if moves:
                return False
        return True
