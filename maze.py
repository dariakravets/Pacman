import pygame


def load_maze(file_path):
    with open(file_path, 'r') as file:
        maze_layout = [line.strip() for line in file]
    return maze_layout


def draw_maze(screen, maze_layout, cell_width, cell_height):
    wall_color = (7, 4, 30)  # Dark-blue color for walls
    path_color = (27, 21, 118)  # Neon-blue color for paths

    for row, line in enumerate(maze_layout):
        for col, char in enumerate(line):
            x = col * cell_width
            y = row * cell_height

            if char == '#':
                pygame.draw.rect(screen, wall_color, (x, y, cell_width, cell_height))
            elif char == '.':
                pygame.draw.rect(screen, path_color, (x, y, cell_width, cell_height))
