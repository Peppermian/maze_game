import pygame

def map_walls(maze):

    rows = maze.shape[0]
    cols = maze.shape[1]
    wall_map = [["VV"] * len(row) for row in maze]
    walls = []

    for y in range(rows):
        for x in range(cols):
            # L, R, T, B
            dirs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]

            for dir in dirs:
                try:
                    
                    if dir[0] >= 0 and dir[1] >= 0 and maze[dir[1]][dir[0]] == 1: 
                        walls.append(1)
                    else: 
                        walls.append(0)

                except IndexError:
                    walls.append(0)

            # Analyze Walls and set type in wall_map
            if walls == [0,0,0,0]: # column
                wall_map[y][x] = "CC"        

            elif walls == [0,0,1,1]: # vertical
                wall_map[y][x] = "VV"

            elif walls == [1,1,0,0]: # horizontal
                wall_map[y][x] = "HH"

            elif walls == [1,0,0,0]: # end-left
                wall_map[y][x] = "EL"
            
            elif walls == [0,0,1,0]: # end-top
                wall_map[y][x] = "ET"

            elif walls == [0,1,0,0]: # end-right
                wall_map[y][x] = "ER"

            elif walls == [0,0,0,1]: # end-left
                wall_map[y][x] = "EB"

            elif walls == [1,0,1,0]: # left-top
                wall_map[y][x] = "LT"

            elif walls == [1,0,0,1]: # left-bottom
                wall_map[y][x] = "LB"

            elif walls == [0,1,1,0]: # right-top
                wall_map[y][x] = "RT"

            elif walls == [0,1,0,1]: # right-bottom
                wall_map[y][x] = "RB"

            elif walls == [1,1,1,1]: # cross
                wall_map[y][x] = "XX"

            elif walls == [1,0,1,1]: # triangle-left
                wall_map[y][x] = "TL"

            elif walls == [1,1,1,0]: # triangle-top
                wall_map[y][x] = "TT"

            elif walls == [0,1,1,1]: # triangle-right
                wall_map[y][x] = "TR"

            elif walls == [1,1,0,1]: # triangle-bottom
                wall_map[y][x] = "TB"

            # Reset walls
            walls = []

    return wall_map

def draw_wall(wall_map, screen, color, pos, grid_size):

    w_width = 1/3

    if wall_map[pos[1]][pos[0]] == "CC":
        pygame.draw.rect(screen, color, ((pos[0] + 1/6) * grid_size, (pos[1] + 1/6) * grid_size, 2*w_width*grid_size, 2*w_width*grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "VV":
        pygame.draw.rect(screen, color, ((pos[0] + w_width) * grid_size, pos[1] * grid_size, w_width*grid_size, grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "HH":
        pygame.draw.rect(screen, color, (pos[0] * grid_size, (pos[1] + w_width) * grid_size, grid_size, w_width*grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "EL":
        pygame.draw.rect(screen, color, (pos[0] * grid_size, (pos[1] + w_width) * grid_size, (1/2)*grid_size, w_width*grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "ET":
        pygame.draw.rect(screen, color, ((pos[0] + w_width) * grid_size, pos[1] * grid_size, w_width*grid_size, (1/2)*grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "ER":
        pygame.draw.rect(screen, color, ((pos[0] + 1/2) * grid_size, (pos[1] + w_width) * grid_size, grid_size, w_width*grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "EB":
        pygame.draw.rect(screen, color, ((pos[0] + w_width) * grid_size, (pos[1] + 1/2) * grid_size, w_width*grid_size, grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "LT":
        pygame.draw.rect(screen, color, (pos[0] * grid_size, (pos[1] + w_width) * grid_size, (1/2 + 1/2*w_width)*grid_size, w_width*grid_size), 0)
        pygame.draw.rect(screen, color, ((pos[0] + w_width) * grid_size, pos[1] * grid_size, w_width*grid_size, (1/2)*grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "LB":
        pygame.draw.rect(screen, color, (pos[0] * grid_size, (pos[1] + w_width) * grid_size, (1/2)*grid_size, w_width*grid_size), 0)
        pygame.draw.rect(screen, color, ((pos[0] + w_width) * grid_size, (pos[1]+ 1/2 - 1/2*w_width) * grid_size, w_width*grid_size, grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "RT":
        pygame.draw.rect(screen, color, ((pos[0]+ 1/2 - 1/2*w_width) * grid_size, (pos[1] + w_width) * grid_size, grid_size, w_width*grid_size), 0)
        pygame.draw.rect(screen, color, ((pos[0] + w_width) * grid_size, pos[1] * grid_size, w_width*grid_size, (1/2)*grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "RB":
        pygame.draw.rect(screen, color, ((pos[0]+ 1/2 - 1/2*w_width) * grid_size, (pos[1] + w_width) * grid_size, grid_size, w_width*grid_size), 0)
        pygame.draw.rect(screen, color, ((pos[0] + w_width) * grid_size, (pos[1]+ 1/2) * grid_size, w_width*grid_size, grid_size), 0)
    
    elif wall_map[pos[1]][pos[0]] == "XX":
        pygame.draw.rect(screen, color, (pos[0] * grid_size, (pos[1] + w_width) * grid_size, grid_size, w_width*grid_size), 0)
        pygame.draw.rect(screen, color, ((pos[0] + w_width) * grid_size, pos[1] * grid_size, w_width*grid_size, grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "TL":
        pygame.draw.rect(screen, color, (pos[0] * grid_size, (pos[1] + w_width) * grid_size, (1/2)*grid_size, w_width*grid_size), 0)
        pygame.draw.rect(screen, color, ((pos[0] + w_width) * grid_size, pos[1] * grid_size, w_width*grid_size, grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "TT":
        pygame.draw.rect(screen, color, (pos[0] * grid_size, (pos[1] + w_width) * grid_size, grid_size, w_width*grid_size), 0)
        pygame.draw.rect(screen, color, ((pos[0] + w_width) * grid_size, pos[1] * grid_size, w_width*grid_size, (1/2)*grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "TR":
        pygame.draw.rect(screen, color, ((pos[0]+ 1/2) * grid_size, (pos[1] + w_width) * grid_size, grid_size, w_width*grid_size), 0)
        pygame.draw.rect(screen, color, ((pos[0] + w_width) * grid_size, pos[1] * grid_size, w_width*grid_size, grid_size), 0)

    elif wall_map[pos[1]][pos[0]] == "TB":
        pygame.draw.rect(screen, color, (pos[0] * grid_size, (pos[1] + w_width) * grid_size, grid_size, w_width*grid_size), 0)
        pygame.draw.rect(screen, color, ((pos[0] + w_width) * grid_size, (pos[1] + 1/2) * grid_size, w_width*grid_size, grid_size), 0)

    else:
        pygame.draw.rect(screen, color, (pos[0] * grid_size+grid_size*(1/4), pos[1] * grid_size+grid_size*(1/4), grid_size*0.5, grid_size*0.5), 0)