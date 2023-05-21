import ez_profile
import generator
import pygame
import math
import os

pygame.init()

#random
seed = 123
state = 0
def random(a, b):
    if (a > b):
        return random(b, a)
    if (a != 0):
        return a + random(0, b+a)

    global state
    result = b + 1
    i = state
    while (result == b+1):
        result = ((seed + seed * state ** 3) ^ i) % (b+1)
        i += 1
        
    state += 1
    return result

def shuffle(temp_list):
    temp = []
    while (len(temp_list) != 0):
        i = random(0, len(temp_list) - 1)
        temp.append(temp_list[i])
        temp_list.pop(i)
    return temp

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

X_piece = [[5,0],[5,1],[5,2],[5,3]]
T_piece = [[4,0],[4,1],[4,2],[4,3]]
I_piece = [[3,0],[3,1],[3,2],[3,3]]
L_piece = [[2,0],[2,1],[2,2],[2,3]]
end_piece = [[1,0],[1,1],[1,2],[1,3]]
empty_piece = None


#fill in grid
for x in range(grid_x):
    grid.append([])
    for y in range(grid_y):
        grid[x].append(empty_piece)


#adds two pieces to form another
def add_pieces(piece1, piece2):
    #basic adding
    if (piece1 == piece2):
        return piece1
    if (piece1 == None):
        return piece2
    if (piece2 == None):
        return piece1
    if (piece1[0] == 5 or piece2[0] == 5):
        return X_piece[random(0, 3)]
    
    #making sure there end piece at the start
    if (piece2[0] == 1):
        if not(piece1[0] == 1):
            piece1, piece2 = piece2, piece1

    #end-smth adding
    if (piece1[0] == 1):
        #end-end adding
        if (piece2[0] == 1):
            #result is I piece
            if (abs(piece1[1] - piece2[1]) == 2):
                return I_piece[random(0, 1) * 2 + piece1[1] % 2]
            #result is L piece
            return L_piece[(2 if (max(piece1[1], piece2[1])-min(piece1[1], piece2[1]) == 3) else (0 if (min(piece1[1], piece2[1]) == 1) else 3-min(piece1[1], piece2[1])))]

        #end-L adding
        if (piece2[0] == 2):
            #result is T piece
            if (piece1[1] == 3 and piece2[1] == 0):
                return T_piece[2]
            if (piece2[1]-piece1[1]==0 or piece2[1]-piece1[1]==1):
                return T_piece[(((1+piece1[1])%4) if piece1[1]==piece2[1] else (0 if (piece2[1]==2) else (4-piece2[1])))]
            #result is original L piece
            return piece2
                                                                  
        #end-I adding
        if (piece2[0] == 3):
            #results in T piece
            if (abs(piece1[1]-piece2[1]) % 2 == 1):
                return T_piece[piece1[1]]
            #results in original I piece
            return piece2

        #end-T adding
        if(piece2[0] == 4):
            #results in X piece
            if (abs(piece1[1] - piece2[1]) == 2):
                return X_piece[random(0, 3)]
            #results in original T piece
            return piece2

    #making sure there L piece at the start
    if (piece2[0] == 2):
        if not(piece1[0] == 2):
            piece1, piece2 = piece2, piece1
    
    #L-smth adding
    if (piece1[0] == 2):
        #L-L adding
        if (piece2[0] == 2):
            if (abs(piece1[1]-piece2[1]) == 2):
                return X_piece[random(0, 3)]
            return T_piece[(1+max(piece1[1], piece2[1]))%4 + (1 if (max(piece1[1],piece2[1])-min(piece1[1],piece2[1])==3) else 0)]
        #L-I adding
        if (piece2[0] == 3):
            return T_piece[1-piece2[1]%2+(2 if (piece1[1]+piece2[1]%2==1 or piece1[1]+piece2[1]%2==2) else 0)]
        #L-T adding
        if (piece2[0] == 4):
            if (piece1[1] == piece2[1] or piece1[1]==(piece2[1]+1)%4):
                return X_piece[random(0, 3)]
            return piece2
    
    #making sure there I piece at the start
    if (piece2[0] == 3):
        if not(piece1[0] == 3):
            piece1, piece2 = piece2, piece1
            
    #I-smth adding
    if (piece1[0] == 3):
        pass
        #I-I adding
        if (piece2[0] == 3):
            if (piece1[1]%2 == piece2[1]%2):
                return I_piece[random(0, 1) * 2 + piece1[1] % 2]
            return X_piece[random(0, 3)]
        #I-T adding
        if (piece2[0] == 4):
            if (piece1[1]%2 == piece2[1]%2):
                return X_piece[random(0, 3)]
            return piece2

    #T-smth adding
    if (piece1[0] == 4):
        pass
        #T-T adding
        return X_piece[random(0, 3)]

    return empty_piece


#generates a new entrance
def new_entrance():
    if (random(0, 1) == 1):
        a = random(0, 1)
        x = a * (grid_x - 1)
        y = random(0, grid_y)
        grid[x][y] = add_pieces(grid[x][y], end_piece[(1 - a) * 2 + 1])
    else:
        a = random(0, 1)
        x = random(0, grid_x)
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

#generates map
def generation():
    stack = [[random(0, grid_x), random(0, grid_y)]]
    moves = [0, 1, 2, 3]

    while (len(stack) != 0):
        current = stack[len(stack) - 1]
        stack.pop(-1)

        moves = shuffle(moves)
        for i in moves:
            mod_x = current[0] + (i % 2) * (1 - 2 * (i > 1))
            mod_y = current[1] + (1 - i % 2) * (1 - i)
            if (mod_x < 0 or mod_x >= grid_x or mod_y < 0 or mod_y >= grid_y):
                continue
            if (grid[mod_x][mod_y] == None):
                stack.append(current)
                path(current[0], current[1], i)
                stack.append([mod_x, mod_y])
                break

#load images
empty_tile = pygame.Surface((cell_size, cell_size), flags = pygame.SRCALPHA)
X_tile = []
T_tile = []
I_tile = []
L_tile = []
end_tile = []

for root, dirs, files in os.walk(".\Images", topdown=False):
    for name in files:
        item = name.split(".")
        root1 = root[2:]
        if (item[-1] == "png"):
            item_path = root1 + "\\" + name
            if (item[0].startswith("X_piece")):
                X_tile.append(pygame.image.load(item_path).convert_alpha())
                continue
            if (item[0].startswith("T_piece")):
                T_tile.append(pygame.image.load(item_path).convert_alpha())
                continue
            if (item[0].startswith("I_piece")):
                I_tile.append(pygame.image.load(item_path).convert_alpha())
                continue
            if (item[0].startswith("L_piece")):
                L_tile.append(pygame.image.load(item_path).convert_alpha())
                continue
            if (item[0].startswith("end_piece")):
                end_tile.append(pygame.image.load(item_path).convert_alpha())
                continue
            print(item[0])


#creates easily accesible rotations for sprites
def create_rotations(sprite):
    temp = []
    for item in sprite:
        temp1 = []
        for angle in range(4):
            temp1.append(pygame.transform.rotate(item, angle * 90))
        temp.append(temp1)
    return temp

X_tile = create_rotations(X_tile)
T_tile = create_rotations(T_tile)
I_tile = create_rotations(I_tile)
L_tile = create_rotations(L_tile)
end_tile = create_rotations(end_tile)

#returns sprite based on input piece
def piece_to_sprite(tile):
    if (tile[0] == 1):
        return end_tile[random(0, len(end_tile)-1)][tile[1]]
    if (tile[0] == 2):
        return L_tile[random(0, len(L_tile)-1)][tile[1]]
    if (tile[0] == 3):
        return I_tile[random(0, len(I_tile)-1)][tile[1]]
    if (tile[0] == 4):
        return T_tile[random(0, len(T_tile)-1)][tile[1]]
    if (tile[0] == 5):
        return X_tile[random(0, len(X_tile)-1)][tile[1]]
    return empty_tile

def gameLoop():
    game_over = False
    
    generation()

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