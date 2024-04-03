import numpy as np
import random 

def print_dict(dict):
    for key in dict.keys():
        print(key, " --> " , dict[key])
    print()

def print_maze(maze):
    for row in maze:
        print(" ".join(["#" if cell == 1 else " " for cell in row]))

# # #

def load_maze():
    return np.loadtxt(r'C:\Users\Luis\Desktop\Portfolio\Pathfinder\src\maze_loader\maze.txt', dtype=int, delimiter=" ")

def save_maze(maze):

    #ensure border
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if y == 0 or y == len(maze)-1 or x == 0 or x == len(row)-1:
                maze[y][x] = 1

    np.savetxt(r'C:\Users\Luis\Desktop\Portfolio\Pathfinder\src\maze_loader\maze.txt', maze, fmt='%d', delimiter=" ")

# # #

def maze_to_graph(maze):

    rows = maze.shape[0]
    cols = maze.shape[1]
    graph = {}

    for y in range(1, rows-1):
        for x in range(1, cols-1):
            if maze[y, x] != 1: #check if not on wall
                adj = []
                dirs = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
                random.shuffle(dirs)
                for dir in dirs:
                    if maze[dir[1], dir[0]] != 1:
                        adj.append((dir[0], dir[1]))

                graph[(x,y)] = adj

    return graph

def generate_maze(rows, cols):
    
    maze = np.array([[1] * cols for _ in range(rows)])
    start_row, start_col = 1, 1

    def is_valid(row, col):
        return 0 < row < rows-1 and 0 < col < cols-1 and maze[row][col] == 1

    def explore(row, col):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dr, dc in directions:
            new_row, new_col = row + dr * 2, col + dc * 2

            if is_valid(new_row, new_col):
                maze[new_row][new_col] = 0
                maze[row + dr][col + dc] = 0
                explore(new_row, new_col)

    explore(start_row, start_col)

    return maze

def random_empty(maze):

    rows = len(maze)
    cols = len(maze[0])

    x, y = random.randint(1, cols-1), random.randint(1, rows-1)
    while maze[y, x] != 0:
        x, y = random.randint(1, cols-1), random.randint(1, rows-1)
        
    return (x, y)

def random_wall(maze):

    x, y = random.randint(1, len(maze)-1), random.randint(1, len(maze)-1)
    while maze[y, x] != 1:
        x, y = random.randint(1, len(maze)-1), random.randint(1, len(maze)-1)
        
    return (x, y)