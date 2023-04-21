from asyncio.windows_events import NULL
from tarfile import NUL
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
empty_piece = pygame.Surface((grid_x, grid_y), flags = pygame.SRCALPHA)

#fill in grid
for x in range(grid_x):
    grid.append([])
    for y in range(grid_y):
        grid[x].append(empty_piece)


#creates easily accesible rotations for sprites
def create_rotations(sprite):
    temp = [NULL, NULL, NULL, NULL]
    temp[0] = sprite
    temp[1] = pygame.transform.rotate(sprite, 90)
    temp[2] = pygame.transform.rotate(sprite, 180)
    temp[3] = pygame.transform.rotate(sprite, 270)
    return temp

X_piece = create_rotations(X_piece)
T_piece = create_rotations(T_piece)
L_piece = create_rotations(L_piece)
I_piece = create_rotations(I_piece)
end_piece = create_rotations(end_piece)

#generates a new entrance
def new_entrance():
    if (round(random.random()) == 1):
        a = round(random.random())
        grid[a * (grid_x - 1)][math.floor(random.random() * grid_y)] = end_piece[(1 - a) * 2 + 1]
    else:
        a = round(random.random())
        grid[math.floor(random.random() * grid_x)][a * (grid_y - 1)] = end_piece[(1 - a) * 2]


def gameLoop():
    game_over = False
    
    new_entrance()
    new_entrance()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                
        dis.fill((0, 0, 0))

        #Your Code
        for x in range(grid_x):
            for y in range(grid_y):
                dis.blit(grid[x][y], [x  * 24, y * 24])

        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()
gameLoop()