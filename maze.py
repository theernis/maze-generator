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
I_piece = pygame.image.load("I_piece.png").convert_alpha()
L_piece = pygame.image.load("L_piece.png").convert_alpha()
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
I_piece = create_rotations(I_piece)
L_piece = create_rotations(L_piece)
end_piece = create_rotations(end_piece)


#compares two surfaces returns true or false
def compare_surface(piece1, piece2):
    return (str(pygame.PixelArray(piece1)) == str(pygame.PixelArray(piece2)))

#adds two pieces to form another
def add_pieces(piece1, piece2):
    #basic adding
    if (compare_surface(piece1, piece2)):
        return piece1
    if (compare_surface(piece1, X_piece[0]) or compare_surface(piece2, X_piece[0])):
        return X_piece[math.floor(random.random() * 4)]
    if (compare_surface(piece1, empty_piece)):
        return piece2
    if (compare_surface(piece2, empty_piece)):
        return piece1
    
    #making sure there end piece at the start
    if (compare_surface(piece2, end_piece[0]) or compare_surface(piece2, end_piece[1]) or compare_surface(piece2, end_piece[2]) or compare_surface(piece2, end_piece[3])):
        if not(compare_surface(piece1, end_piece[0]) or compare_surface(piece1, end_piece[1]) or compare_surface(piece1, end_piece[2]) or compare_surface(piece1, end_piece[3])):
            return add_pieces(piece2, piece1)

    #end-end adding
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, end_piece[1])):
        return L_piece[3]
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, end_piece[2])):
        return I_piece[round(random.random()) * 2]
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, end_piece[3])):
        return L_piece[2]
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, end_piece[0])):
        return L_piece[3]
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, end_piece[2])):
        return L_piece[0]
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, end_piece[3])):
        return I_piece[round(random.random()) * 2 + 1]
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, end_piece[0])):
        return I_piece[round(random.random()) * 2]
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, end_piece[1])):
        return L_piece[0]
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, end_piece[3])):
        return L_piece[1]
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, end_piece[0])):
        return L_piece[2]
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, end_piece[1])):
        return I_piece[round(random.random()) * 2 + 1]
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, end_piece[2])):
        return L_piece[1]

    #end-L adding
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, L_piece[0])):
        return T_piece[1]
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, L_piece[1])):
        return T_piece[3]
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, L_piece[2])):
        return piece2
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, L_piece[3])):
        return piece2
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, L_piece[0])):
        return piece2
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, L_piece[1])):
        return T_piece[2]
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, L_piece[2])):
        return T_piece[0]
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, L_piece[3])):
        return piece2
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, L_piece[0])):
        return piece2
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, L_piece[1])):
        return piece2
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, L_piece[2])):
        return T_piece[3]
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, L_piece[3])):
        return T_piece[1]
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, L_piece[0])):
        return T_piece[2]
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, L_piece[1])):
        return piece2
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, L_piece[2])):
        return piece2
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, L_piece[3])):
        return T_piece[0]
                                                              
    #end-I adding
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, I_piece[0])):
        return piece2
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, I_piece[1])):
        return T_piece[0]
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, I_piece[2])):
        return piece2
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, I_piece[3])):
        return T_piece[0]
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, I_piece[0])):
        return T_piece[1]
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, I_piece[1])):
        return piece2
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, I_piece[2])):
        return T_piece[1]
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, I_piece[3])):
        return piece2
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, I_piece[0])):
        return piece2
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, I_piece[1])):
        return T_piece[2]
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, I_piece[2])):
        return piece2
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, I_piece[3])):
        return T_piece[2]
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, I_piece[0])):
        return T_piece[3]
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, I_piece[1])):
        return piece2
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, I_piece[2])):
        return T_piece[3]
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, I_piece[3])):
        return piece2

    #end-T adding
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, T_piece[0])):
        return piece2
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, T_piece[1])):
        return piece2
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, T_piece[2])):
        return X_piece[math.floor(random.random() * 4)]
    if (compare_surface(piece1, end_piece[0]) and compare_surface(piece2, T_piece[3])):
        return piece2
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, T_piece[0])):
        return piece2
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, T_piece[1])):
        return piece2
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, T_piece[2])):
        return piece2
    if (compare_surface(piece1, end_piece[1]) and compare_surface(piece2, T_piece[3])):
        return X_piece[math.floor(random.random() * 4)]
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, T_piece[0])):
        return X_piece[math.floor(random.random() * 4)]
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, T_piece[1])):
        return piece2
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, T_piece[2])):
        return piece2
    if (compare_surface(piece1, end_piece[2]) and compare_surface(piece2, T_piece[3])):
        return piece2
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, T_piece[0])):
        return piece2
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, T_piece[1])):
        return X_piece[math.floor(random.random() * 4)]
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, T_piece[2])):
        return piece2
    if (compare_surface(piece1, end_piece[3]) and compare_surface(piece2, T_piece[3])):
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

def gameLoop():
    game_over = False
    
    for x in range(4):
        for y in range(4):
            grid[x * 2 + 1][y * 4 + 1] = add_pieces(T_piece[x], end_piece[y])
            grid[x * 2 + 1][y * 4 + 2] = T_piece[x]
            grid[x * 2 + 1][y * 4 + 3] = end_piece[y]
    
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
                dis.blit(grid[x][y], [x  * cell_size, y * cell_size])

        pygame.display.update()
        clock.tick(30)
    pygame.quit()
    quit()
gameLoop()