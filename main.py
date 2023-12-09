import pygame

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('PyChess')

font = pygame.font.Font('freesansbold.ttf', 20)
medium_font = pygame.font.Font('freesansbold.ttf', 40)
big_font = pygame.font.Font('freesansbold.ttf', 50)

timer = pygame.time.Clock()
fps = 60

run = True
while run:
    timer.tick(fps)
    screen.fill('dark gray')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
