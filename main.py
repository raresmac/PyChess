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

# image coordinates
coords_y = [520 - (i - 1) * 68 for i in range(9)]
coords_x = [45 + (i - 1) * 68 for i in range(9)]

# fonts
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

timer = pygame.time.Clock()
fps = 60

# loading images - taken from cburnett
# white pieces
white_pawn_light = pygame.image.load('assets/images/pawn_white_light.png')
white_pawn_dark = pygame.image.load('assets/images/pawn_white_dark.png')
white_queen_light = pygame.image.load('assets/images/queen_white_light.png')
white_queen_dark = pygame.image.load('assets/images/queen_white_dark.png')
white_king_light = pygame.image.load('assets/images/king_white_light.png')
white_king_dark = pygame.image.load('assets/images/king_white_dark.png')
white_bishop_light = pygame.image.load('assets/images/bishop_white_light.png')
white_bishop_dark = pygame.image.load('assets/images/bishop_white_dark.png')
white_knight_light = pygame.image.load('assets/images/knight_white_light.png')
white_knight_dark = pygame.image.load('assets/images/knight_white_dark.png')
white_rook_light = pygame.image.load('assets/images/rook_white_light.png')
white_rook_dark = pygame.image.load('assets/images/rook_white_dark.png')
# black pieces
black_pawn_light = pygame.image.load('assets/images/pawn_black_light.png')
black_pawn_dark = pygame.image.load('assets/images/pawn_black_dark.png')
black_queen_light = pygame.image.load('assets/images/queen_black_light.png')
black_queen_dark = pygame.image.load('assets/images/queen_black_dark.png')
black_king_light = pygame.image.load('assets/images/king_black_light.png')
black_king_dark = pygame.image.load('assets/images/king_black_dark.png')
black_bishop_light = pygame.image.load('assets/images/bishop_black_light.png')
black_bishop_dark = pygame.image.load('assets/images/bishop_black_dark.png')
black_knight_light = pygame.image.load('assets/images/knight_black_light.png')
black_knight_dark = pygame.image.load('assets/images/knight_black_dark.png')
black_rook_light = pygame.image.load('assets/images/rook_black_light.png')
black_rook_dark = pygame.image.load('assets/images/rook_black_dark.png')
# empty square
dark_square = pygame.image.load('assets/images/square_dark.png')
light_square = pygame.image.load('assets/images/square_light.png')

game_board = board.Board()
player_w = player.Player(game_board, 'w')
player_b = player.Player(game_board, 'b')


def board_draw(game_board):
    for i in range(1, 9):
        for j in range(1, 9):
            piece = game_board.get_cell(i, j)
            if (i + j) % 2 == 0:
                if not piece:
                    screen.blit(dark_square, (coords_x[j], coords_y[i]))
                elif piece.get_color() == 'w':
                    if isinstance(piece, pieces.Pawn):
                        screen.blit(white_pawn_dark, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Bishop):
                        screen.blit(white_bishop_dark, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Knight):
                        screen.blit(white_knight_dark, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Rook):
                        screen.blit(white_rook_dark, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.King):
                        screen.blit(white_king_dark, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Queen):
                        screen.blit(white_queen_dark, (coords_x[j], coords_y[i]))
                else:
                    if isinstance(piece, pieces.Pawn):
                        screen.blit(black_pawn_dark, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Bishop):
                        screen.blit(black_bishop_dark, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Knight):
                        screen.blit(black_knight_dark, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Rook):
                        screen.blit(black_rook_dark, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.King):
                        screen.blit(black_king_dark, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Queen):
                        screen.blit(black_queen_dark, (coords_x[j], coords_y[i]))
            else:
                if not piece:
                    screen.blit(light_square, (coords_x[j], coords_y[i]))
                elif piece.get_color() == 'w':
                    if isinstance(piece, pieces.Pawn):
                        screen.blit(white_pawn_light, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Bishop):
                        screen.blit(white_bishop_light, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Knight):
                        screen.blit(white_knight_light, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Rook):
                        screen.blit(white_rook_light, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.King):
                        screen.blit(white_king_light, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Queen):
                        screen.blit(white_queen_light, (coords_x[j], coords_y[i]))
                else:
                    if isinstance(piece, pieces.Pawn):
                        screen.blit(black_pawn_light, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Bishop):
                        screen.blit(black_bishop_light, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Knight):
                        screen.blit(black_knight_light, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Rook):
                        screen.blit(black_rook_light, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.King):
                        screen.blit(black_king_light, (coords_x[j], coords_y[i]))
                    elif isinstance(piece, pieces.Queen):
                        screen.blit(black_queen_light, (coords_x[j], coords_y[i]))



# for i in range(1, 9):
#     for j in range(1, 9):
#         print(game_board.get_cell(i, j))
#     print('---')


screen.fill('dark gray')
run = True
while run:
    timer.tick(fps)
    board_draw(game_board)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
