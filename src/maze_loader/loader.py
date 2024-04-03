import numpy as np
import random

directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

def load_maze():
    return np.loadtxt(r'C:\Users\Luis\Desktop\Portfolio\Pathfinder\src\maze_loader\maze.txt', dtype=int, delimiter=" ")

def save_maze(maze):

    #ensure border
    for y, row in enumerate(maze):
        for x, cell in enumerate(row):
            if y == 0 or y == len(maze)-1 or x == 0 or x == len(row)-1:
                maze[y][x] = 1

    np.savetxt(r'C:\Users\Luis\Desktop\Portfolio\Pathfinder\src\maze_loader\maze.txt', maze, fmt='%d', delimiter=" ")

def generate_maze(rows, cols):

    grid = np.array([[0] * cols for _ in range(rows)])
    for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if y == 0 or y == len(grid)-1 or x == 0 or x == len(row)-1:
                    grid[y, x] = 1

def generate_maze(rows, cols):
    
    maze = np.array([[0] * cols for _ in range(rows)])
    start_row, start_col = 0, 0
    end_row, end_col = rows - 1, cols - 1

    def is_valid(row, col):
        return 0 <= row < rows and 0 <= col < cols and maze[row][col] == 0

    def explore(row, col):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        random.shuffle(directions)

        for dr, dc in directions:
            new_row, new_col = row + dr * 2, col + dc * 2

            if is_valid(new_row, new_col):
                maze[row + dr][col + dc] = 1  # Mark the wall as part of the maze
                maze[new_row][new_col] = 1
                explore(new_row, new_col)

    maze[start_row][start_col] = 1  # Mark the start
    maze[end_row][end_col] = 1  # Mark the end
    explore(start_row, start_col)

    return maze