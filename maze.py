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
X_tile = pygame.image.load("X_piece.png").convert_alpha()
T_tile = pygame.image.load("T_piece.png").convert_alpha()
I_tile = pygame.image.load("I_piece.png").convert_alpha()
L_tile = pygame.image.load("L_piece.png").convert_alpha()
end_tile = pygame.image.load("end_piece.png").convert_alpha()
empty_tile = pygame.Surface((grid_x, grid_y), flags = pygame.SRCALPHA)

X_piece = [[5,0],[5,1],[5,2],[5,3]]
T_piece = [[4,0],[4,1],[4,2],[4,3]]
I_piece = [[3,0],[3,1],[3,2],[3,3]]
L_piece = [[2,0],[2,1],[2,2],[2,3]]
end_piece = [[1,0],[1,1],[1,2],[1,3]]
empty_piece = [0,0]


#fill in grid
for x in range(grid_x):
    grid.append([])
    for y in range(grid_y):
        grid[x].append(empty_piece)


#creates easily accesible rotations for sprites
def create_rotations(sprite):
    temp = []
    for angle in range(4):
      temp.append(pygame.transform.rotate(sprite, angle * 90))
    return temp

X_tile = create_rotations(X_tile)
T_tile = create_rotations(T_tile)
I_tile = create_rotations(I_tile)
L_tile = create_rotations(L_tile)
end_tile = create_rotations(end_tile)


#adds two pieces to form another
def add_pieces(piece1, piece2):
    #basic adding
    if (piece1 == piece2):
        return piece1
    if (piece1[0] == 5 or piece2[0] == 5):
        return X_piece[math.floor(random.random() * 4)]
    if (piece1[0] == 0):
        return piece2
    if (piece2[0] == 0):
        return piece1
    
    #making sure there end piece at the start
    if (piece2[0] == 1):
        if not(piece1[0] == 1):
            return add_pieces(piece2, piece1)

    #end-end adding
    if (piece1 == end_piece[0] and piece2 == end_piece[1]):
        return L_piece[3]
    if (piece1 == end_piece[0] and piece2 == end_piece[2]):
        return I_piece[round(random.random()) * 2]
    if (piece1 == end_piece[0] and piece2 == end_piece[3]):
        return L_piece[2]
    if (piece1 == end_piece[1] and piece2 == end_piece[0]):
        return L_piece[3]
    if (piece1 == end_piece[1] and piece2 == end_piece[2]):
        return L_piece[0]
    if (piece1 == end_piece[1] and piece2 == end_piece[3]):
        return I_piece[round(random.random()) * 2 + 1]
    if (piece1 == end_piece[2] and piece2 == end_piece[0]):
        return I_piece[round(random.random()) * 2]
    if (piece1 == end_piece[2] and piece2 == end_piece[1]):
        return L_piece[0]
    if (piece1 == end_piece[2] and piece2 == end_piece[3]):
        return L_piece[1]
    if (piece1 == end_piece[3] and piece2 == end_piece[0]):
        return L_piece[2]
    if (piece1 == end_piece[3] and piece2 == end_piece[1]):
        return I_piece[round(random.random()) * 2 + 1]
    if (piece1 == end_piece[3] and piece2 == end_piece[2]):
        return L_piece[1]

    #end-L adding
    if (piece1 == end_piece[0] and piece2 == L_piece[0]):
        return T_piece[1]
    if (piece1 == end_piece[0] and piece2 == L_piece[1]):
        return T_piece[3]
    if (piece1 == end_piece[0] and piece2 == L_piece[2]):
        return piece2
    if (piece1 == end_piece[0] and piece2 == L_piece[3]):
        return piece2
    if (piece1 == end_piece[1] and piece2 == L_piece[0]):
        return piece2
    if (piece1 == end_piece[1] and piece2 == L_piece[1]):
        return T_piece[2]
    if (piece1 == end_piece[1] and piece2 == L_piece[2]):
        return T_piece[0]
    if (piece1 == end_piece[1] and piece2 == L_piece[3]):
        return piece2
    if (piece1 == end_piece[2] and piece2 == L_piece[0]):
        return piece2
    if (piece1 == end_piece[2] and piece2 == L_piece[1]):
        return piece2
    if (piece1 == end_piece[2] and piece2 == L_piece[2]):
        return T_piece[3]
    if (piece1 == end_piece[2] and piece2 == L_piece[3]):
        return T_piece[1]
    if (piece1 == end_piece[3] and piece2 == L_piece[0]):
        return T_piece[2]
    if (piece1 == end_piece[3] and piece2 == L_piece[1]):
        return piece2
    if (piece1 == end_piece[3] and piece2 == L_piece[2]):
        return piece2
    if (piece1 == end_piece[3] and piece2 == L_piece[3]):
        return T_piece[0]
                                                              
    #end-I adding
    if (piece1 == end_piece[0] and piece2 == I_piece[0]):
        return piece2
    if (piece1 == end_piece[0] and piece2 == I_piece[1]):
        return T_piece[0]
    if (piece1 == end_piece[0] and piece2 == I_piece[2]):
        return piece2
    if (piece1 == end_piece[0] and piece2 == I_piece[3]):
        return T_piece[0]
    if (piece1 == end_piece[1] and piece2 == I_piece[0]):
        return T_piece[1]
    if (piece1 == end_piece[1] and piece2 == I_piece[1]):
        return piece2
    if (piece1 == end_piece[1] and piece2 == I_piece[2]):
        return T_piece[1]
    if (piece1 == end_piece[1] and piece2 == I_piece[3]):
        return piece2
    if (piece1 == end_piece[2] and piece2 == I_piece[0]):
        return piece2
    if (piece1 == end_piece[2] and piece2 == I_piece[1]):
        return T_piece[2]
    if (piece1 == end_piece[2] and piece2 == I_piece[2]):
        return piece2
    if (piece1 == end_piece[2] and piece2 == I_piece[3]):
        return T_piece[2]
    if (piece1 == end_piece[3] and piece2 == I_piece[0]):
        return T_piece[3]
    if (piece1 == end_piece[3] and piece2 == I_piece[1]):
        return piece2
    if (piece1 == end_piece[3] and piece2 == I_piece[2]):
        return T_piece[3]
    if (piece1 == end_piece[3] and piece2 == I_piece[3]):
        return piece2

    #end-T adding
    if (piece1 == end_piece[0] and piece2 == T_piece[0]):
        return piece2
    if (piece1 == end_piece[0] and piece2 == T_piece[1]):
        return piece2
    if (piece1 == end_piece[0] and piece2 == T_piece[2]):
        return X_piece[math.floor(random.random() * 4)]
    if (piece1 == end_piece[0] and piece2 == T_piece[3]):
        return piece2
    if (piece1 == end_piece[1] and piece2 == T_piece[0]):
        return piece2
    if (piece1 == end_piece[1] and piece2 == T_piece[1]):
        return piece2
    if (piece1 == end_piece[1] and piece2 == T_piece[2]):
        return piece2
    if (piece1 == end_piece[1] and piece2 == T_piece[3]):
        return X_piece[math.floor(random.random() * 4)]
    if (piece1 == end_piece[2] and piece2 == T_piece[0]):
        return X_piece[math.floor(random.random() * 4)]
    if (piece1 == end_piece[2] and piece2 == T_piece[1]):
        return piece2
    if (piece1 == end_piece[2] and piece2 == T_piece[2]):
        return piece2
    if (piece1 == end_piece[2] and piece2 == T_piece[3]):
        return piece2
    if (piece1 == end_piece[3] and piece2 == T_piece[0]):
        return piece2
    if (piece1 == end_piece[3] and piece2 == T_piece[1]):
        return X_piece[math.floor(random.random() * 4)]
    if (piece1 == end_piece[3] and piece2 == T_piece[2]):
        return piece2
    if (piece1 == end_piece[3] and piece2 == T_piece[3]):
        return piece2

    #in future you might need to add:
    #L-L addition
    #L-I addition
    #L-T addition
    #I-I addition
    #I-T addition
    #T-T addition

    return empty_piece


#generates a new entrance
def new_entrance():
    if (round(random.random()) == 1):
        a = round(random.random())
        x = a * (grid_x - 1)
        y = math.floor(random.random() * grid_y)
        grid[x][y] = add_pieces(grid[x][y], end_piece[(1 - a) * 2 + 1])
    else:
        a = round(random.random())
        x = math.floor(random.random() * grid_x)
        y = a * (grid_y - 1)
        grid[x][y] = add_pieces(grid[x][y], end_piece[(1 - a) * 2])

#generates a path between two conecting tiles
#rot value is for rotation (0 - down; 1 - right; 2 - up; 3 - left)
def path(x, y, rot):
    if (rot < 0 or rot >= 4 or x < 0 or x >= grid_x or y < 0 or y >= grid_y):
        return
    if (rot >= 2):
        path(x+(2-rot), y+(rot-3), rot - 2)
        return

    grid[x][y] = add_pieces(grid[x][y], end_piece[rot])
    grid[x+rot][y+(1-rot)] = add_pieces(grid[x+rot][y+(1-rot)], end_piece[rot+2])

#returns sprite based on input piece
def piece_to_sprite(tile):
    if (tile[0] == 1):
        return end_tile[tile[1]]
    if (tile[0] == 2):
        return L_tile[tile[1]]
    if (tile[0] == 3):
        return I_tile[tile[1]]
    if (tile[0] == 4):
        return T_tile[tile[1]]
    if (tile[0] == 5):
        return X_tile[tile[1]]
    return empty_tile

def gameLoop():
    game_over = False
    
    #for x in range(4):
    #    for y in range(4):
    #        grid[x * 2 + 1][y * 4 + 1] = add_pieces(T_piece[x], end_piece[y])
    #        grid[x * 2 + 1][y * 4 + 2] = T_piece[x]
    #        grid[x * 2 + 1][y * 4 + 3] = end_piece[y]
    
    path(1,1,0)
    path(1,2,1)
    path(2,2,0)
    path(2,3,3)

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
                dis.blit(piece_to_sprite(grid[x][y]), [x  * cell_size, y * cell_size])

        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()
gameLoop()