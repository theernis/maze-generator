import pygame
import random
import math

pygame.init()

#set values
cell_size = 24
grid_x = 24
grid_y = 24
grid = []
dis_width = cell_size * grid_x
dis_height = cell_size * grid_y
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('maze')
clock = pygame.time.Clock()

#load images
X_piece = pygame.image.load("X_piece.png").convert_alpha()
T_piece = pygame.image.load("T_piece.png").convert_alpha()
L_piece = pygame.image.load("L_piece.png").convert_alpha()
I_piece = pygame.image.load("I_piece.png").convert_alpha()
end_piece = pygame.image.load("end_piece.png").convert_alpha()

#temporary function
def random_piece():
    a = math.floor(random.random() * 5)
    if (a == 0):
        return X_piece
    if (a == 1):
        return T_piece
    if (a == 2):
        return L_piece
    if (a == 3):
        return I_piece
    if (a == 4):
        return end_piece
    return random_piece()

#fill in grid
for x in range(grid_x):
    grid.append([])
    for y in range(grid_y):
        grid[x].append(random_piece())

def gameLoop():
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
        dis.fill((0, 0, 0))

        #Your Code
        for x in range(grid_x):
            for y in range(grid_y):
                dis.blit(pygame.transform.rotate(grid[x][y], round(math.sqrt(x  * 24 + y * 24)) * 90), [x  * 24, y * 24])

        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()
gameLoop()