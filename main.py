import pygame
import pieces

pygame.init()

# window properties
width = 640
height = 640
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('PyChess')

# fonts
font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

timer = pygame.time.Clock()
fps = 60

# loading images - taken from cburnett
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

run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    screen.blit(black_queen_light, (20, 30))
    screen.blit(black_queen_dark, (90, 30))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
