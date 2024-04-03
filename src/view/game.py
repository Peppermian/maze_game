import pygame
import sys
import numpy as np

from maze_loader.loader import save_maze, load_maze
from maze_solver.dijkstra import BF_search
from maze_solver.depth_first import DF_search
from maze_solver.utils import print_maze, print_dict, maze_to_graph, generate_maze, random_empty, random_wall
from view.game_utils import *

def run():

    # Initialize pygame
    pygame.init()

    # Constants
    WIDTH, HEIGHT = 1500,800
    CELL_WIDTH = 25

    GRID_WIDTH, GRID_HEIGHT = (WIDTH // CELL_WIDTH), HEIGHT//CELL_WIDTH

    if GRID_WIDTH % 2 == 0:
        GRID_WIDTH = GRID_WIDTH-1
    if GRID_HEIGHT % 2 == 0:
        GRID_HEIGHT = GRID_HEIGHT-1

    GRID_SIZE = WIDTH // GRID_WIDTH

    C1 = (44, 51, 51)
    C2 = (57, 91, 100)
    C3 = (165, 201, 202)
    C4 = (231, 246, 242)

    C5 = (229,31,31)
    C6 = (68,206,27)

    # Create the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Maze Game")

    # Initialize the grid
    grid = generate_maze(GRID_HEIGHT, GRID_WIDTH)
    wall_map = map_walls(grid)
    start = random_empty(grid)
    end = random_empty(grid)

    # grid = load_maze()

    DF = DF_search()
    BF = BF_search()

    # Flags
    make_walls = False
    remove_walls = False
    draw_path = -2
    draw_search = -2
    move_start, move_end = False, False
    grid_x, grid_y = (1, 1)

    delay_speed = [int(200/x) for x in range(1,21)]
    delay = 1

    # Main loop

    while True:

        # INPUT ROUTINE

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                save_maze(grid)
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Get cell that was clicked
                x, y = event.pos
                grid_x, grid_y = x // GRID_SIZE, y // GRID_SIZE
                current_cell = (grid_x, grid_y)

                # User cannot change the border of the maze
                if grid_x in [0, GRID_WIDTH-1] or grid_y in [0, GRID_WIDTH-1]:
                    break

                # If start was clicked
                if (grid_x, grid_y) == start:
                    move_start = True

                # If end was clicked
                elif (grid_x, grid_y) == end:
                    move_end = True

                # Wall was clicked
                elif grid[grid_y, grid_x] == 1:
                    grid[grid_y, grid_x] = 0
                    remove_walls = True

                # Empty was clicked
                elif grid[grid_y, grid_x] == 0:
                    grid[grid_y, grid_x] = 1
                    make_walls = True

                #Re-Calculate the Wall layout
                wall_map = map_walls(grid)

                draw_path = -2
                draw_search = -2

            elif event.type == pygame.MOUSEMOTION:
                # Get curent cell in motion
                x, y = event.pos
                grid_x, grid_y = x // GRID_SIZE, y // GRID_SIZE

                # check if mouse is within window
                if grid_x in range(1, GRID_WIDTH-1) and grid_y in range(1, GRID_HEIGHT-1): 
                    
                    if move_start:
                        #Change start
                        if grid[grid_y, grid_x] != 1: 
                            start = (grid_x, grid_y)

                    elif move_end:
                        #Change end
                        if grid[grid_y, grid_x] != 1: 
                            end = (grid_x, grid_y)

                    elif remove_walls:
                        if current_cell != (grid_x, grid_y):
                            current_cell = (grid_x, grid_y)
                            # Toggle cell state
                            grid[grid_y, grid_x] = 0

                    elif make_walls:
                        if current_cell != (grid_x, grid_y):
                            current_cell = (grid_x, grid_y)
                            # Toggle cell state
                            grid[grid_y, grid_x] = 1

                    wall_map = map_walls(grid)
                        
            elif event.type == pygame.MOUSEBUTTONUP:
                # Get curent cell
                x, y = event.pos
                grid_x, grid_y = x // GRID_SIZE, y // GRID_SIZE

                remove_walls = False
                make_walls = False
                move_start = False
                move_end = False

            elif event.type == pygame.KEYDOWN:

                if event.key == pygame.K_1:
                    
                    BF.init_graph(grid, start)
                    BF.search_maze(start, end)
                    
                    search_order = BF.order
                    path = BF.gen_path(end)

                    draw_search = len(search_order)
                    draw_path = len(path)

                elif event.key == pygame.K_2:

                    DF.init_graph(grid)
                    DF.search_maze(start, end)
                    
                    search_order = DF.order
                    path = DF.gen_path(end)

                    draw_search = len(search_order)
                    draw_path = len(path)

        # DRAWING ROUTINE
        screen.fill(C4)

        for y, row in enumerate(grid):
            for x, cell in enumerate(row):

                if (x, y) == start:
                    color = C5
                elif (x, y) == end:
                    color = C6
                elif (x, y) == (grid_x, grid_y) :
                    color = C5
                elif cell == 0:
                    color = C4
                elif cell == 1:
                    color = C1

                if (x, y) == start:
                    pygame.draw.circle(screen, color, ((x+1/2)*GRID_SIZE, (y+1/2)*GRID_SIZE ), 0.5*GRID_SIZE)
                elif (x, y) == end:
                    pygame.draw.circle(screen, color, ((x+1/2)*GRID_SIZE, (y+1/2)*GRID_SIZE ), 0.5*GRID_SIZE)
                elif cell == 0:
                    pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
                elif cell == 1:
                    draw_wall(wall_map, screen, color, (x,y), GRID_SIZE)

        # Draw search order         
        if draw_search > 0:
            delay = 1
            color = C1
            for i, node in enumerate(search_order[:-draw_search]):
                pygame.draw.circle(screen, color, ((node[0] + 1/2) * GRID_SIZE, (node[1] + 1/2) * GRID_SIZE), GRID_SIZE*0.2)
            draw_search -= 1
        elif draw_search == 0:
            color = C1
            for i, node in enumerate(search_order):
                pygame.draw.circle(screen, color, ((node[0] + 1/2) * GRID_SIZE, (node[1] + 1/2) * GRID_SIZE), GRID_SIZE*0.2)

        # Draw path
        if draw_search == 0 and draw_path >= 0:
            color = C5
            for i, node in enumerate(path[:-draw_path]):
                pygame.draw.circle(screen, color, ((node[0] + 1/2) * GRID_SIZE, (node[1] + 1/2) * GRID_SIZE), GRID_SIZE*0.3)
            
            if 0 < len(path)-draw_path < 20:
                delay = delay_speed[len(path)-draw_path]*3
            elif len(path)-20 < len(path)-draw_path <= len(path):
                delay = delay_speed[draw_path]*2
            else:
                delay = 2

            draw_path -= 1

        elif draw_path == -1:
            color = C6
            for i, node in enumerate(path):
                pygame.draw.circle(screen, color, ((node[0] + 1/2) * GRID_SIZE, (node[1] + 1/2) * GRID_SIZE), GRID_SIZE*0.3)
            delay = 1

        if draw_path >= 0 or draw_search >= 0:
            pygame.time.delay(delay)
        
        pygame.display.update()