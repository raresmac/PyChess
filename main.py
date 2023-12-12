import pygame

import pieces
import board
import player

pygame.init()

# window properties
width = 640
height = 640
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('PyChess')
screen.fill('dark gray')

# image coordinates
coords_x = [45 + (i - 1) * 68 for i in range(9)]
coords_y = [520 - (i - 1) * 68 for i in range(9)]

# fonts
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

timer = pygame.time.Clock()
fps = 60


# loading images - taken from cburnett
def image_array():
    images = [] # [color][piece][background]
    for i in range(2):
        lst1 = []
        for j in range(6):
            lst2 = []
            for k in range(2):
                lst2.append(None)
            lst1.append(lst2)
        images.append(lst1)
    images.append([None, None])

    # white pieces
    images[0][0][0] = pygame.image.load('assets/images/king_white_dark.png')
    images[0][0][1] = pygame.image.load('assets/images/king_white_light.png')
    images[0][1][0] = pygame.image.load('assets/images/queen_white_dark.png')
    images[0][1][1] = pygame.image.load('assets/images/queen_white_light.png')
    images[0][2][0] = pygame.image.load('assets/images/rook_white_dark.png')
    images[0][2][1] = pygame.image.load('assets/images/rook_white_light.png')
    images[0][3][0] = pygame.image.load('assets/images/bishop_white_dark.png')
    images[0][3][1] = pygame.image.load('assets/images/bishop_white_light.png')
    images[0][4][0] = pygame.image.load('assets/images/knight_white_dark.png')
    images[0][4][1] = pygame.image.load('assets/images/knight_white_light.png')
    images[0][5][0] = pygame.image.load('assets/images/pawn_white_dark.png')
    images[0][5][1] = pygame.image.load('assets/images/pawn_white_light.png')

    # black pieces
    images[1][0][0] = pygame.image.load('assets/images/king_black_dark.png')
    images[1][0][1] = pygame.image.load('assets/images/king_black_light.png')
    images[1][1][0] = pygame.image.load('assets/images/queen_black_dark.png')
    images[1][1][1] = pygame.image.load('assets/images/queen_black_light.png')
    images[1][2][0] = pygame.image.load('assets/images/rook_black_dark.png')
    images[1][2][1] = pygame.image.load('assets/images/rook_black_light.png')
    images[1][3][0] = pygame.image.load('assets/images/bishop_black_dark.png')
    images[1][3][1] = pygame.image.load('assets/images/bishop_black_light.png')
    images[1][4][0] = pygame.image.load('assets/images/knight_black_dark.png')
    images[1][4][1] = pygame.image.load('assets/images/knight_black_light.png')
    images[1][5][0] = pygame.image.load('assets/images/pawn_black_dark.png')
    images[1][5][1] = pygame.image.load('assets/images/pawn_black_light.png')

    # empty square
    images[2][0] = dark_square = pygame.image.load('assets/images/square_dark.png')
    images[2][1] = light_square = pygame.image.load('assets/images/square_light.png')

    return images


images = image_array()
game_board = board.Board()
player_w = player.Player(game_board, 'w')
player_b = player.Player(game_board, 'b')
game_board.set_players(player_w, player_b)
game_board.update_available_moves()


def board_draw(screen, game_board, images, rectang=None, sel_piece=None):
    circles = []
    if sel_piece:
        moves = sel_piece.get_available_moves()
    for i in range(1, 9):
        for j in range(1, 9):
            piece = game_board.get_cell(i, j)
            back = (i + j) % 2
            if piece:
                color = 0
                piece_type = 5
                if piece.get_color() == 'b':
                    color = 1
                if isinstance(piece, pieces.King):
                    piece_type = 0
                elif isinstance(piece, pieces.Queen):
                    piece_type = 1
                elif isinstance(piece, pieces.Rook):
                    piece_type = 2
                elif isinstance(piece, pieces.Bishop):
                    piece_type = 3
                elif isinstance(piece, pieces.Knight):
                    piece_type = 4
                screen.blit(images[color][piece_type][back], (coords_x[j], coords_y[i]))

                # selected piece highlighting
                if rectang == (i, j):
                    pygame.draw.rect(screen, (0, 0, 0), [coords_x[j], coords_y[i], 68, 68], 3)

                # available moves pointing
                if sel_piece and (i, j) in moves:
                    ord_x = coords_x[j] + 34
                    ord_y = coords_y[i] + 34
                    circles.append((ord_x, ord_y))
            else:
                screen.blit(images[2][back], (coords_x[j], coords_y[i]))
                if sel_piece and (i, j) in moves:
                    ord_x = coords_x[j] + 34
                    ord_y = coords_y[i] + 34
                    circles.append((ord_x, ord_y))
    for i in range(len(circles)):
        pygame.draw.circle(screen, (100, 250, 0), (circles[i][0], circles[i][1]), 8)


def get_player_pieces():
    print('-------------')
    print('white:')
    print(game_board.get_players()[0].get_locations())
    print('black:')
    print(game_board.get_players()[1].get_locations())


run = True
select = False
selected_piece = None
rectang = None
board_draw(screen, game_board, images)
while run:
    timer.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = ((588 - event.pos[1]) // 68 + 1, (event.pos[0] - 45) // 68 + 1)
            if game_board.get_move() == 0:
                pos_w = player_w.get_locations()
                if mouse_pos in pos_w:
                    if not select:
                        select = True
                    selected_piece = game_board.get_cell(mouse_pos[0], mouse_pos[1])
                    rectang = (mouse_pos[0], mouse_pos[1])
                else:
                    if select and mouse_pos in selected_piece.get_available_moves():
                        selected_coords = selected_piece.get_coords()
                        game_board.set_cell(mouse_pos[0], mouse_pos[1], selected_piece)
                        select = False
                        selected_piece = None
                        game_board.update_available_moves()
                        if game_board.check_check():
                            print('Check!')
                        rectang = None
            else:
                pos_b = player_b.get_locations()
                if mouse_pos in pos_b:
                    if not select:
                        select = True
                    selected_piece = game_board.get_cell(mouse_pos[0], mouse_pos[1])
                    rectang = (mouse_pos[0], mouse_pos[1])
                else:
                    if select and mouse_pos in selected_piece.get_available_moves():
                        selected_coords = selected_piece.get_coords()
                        game_board.set_cell(mouse_pos[0], mouse_pos[1], selected_piece)
                        select = False
                        selected_piece = None
                        game_board.update_available_moves()
                        game_board.set_check(game_board.check_check())
                        rectang = None
            # if selected_piece:
            #     print(selected_piece.get_available_moves())
            screen.fill('dark gray')
            board_draw(screen, game_board, images, rectang, selected_piece)
    pygame.display.flip()
pygame.quit()
