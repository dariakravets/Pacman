import heapq
import math
import pygame
import random


class GreedyGhost:
    def __init__(self, maze, pacman_position):
        self.maze = maze
        self.position = self.find_starting_position()
        self.pacman_position = pacman_position

    def find_starting_position(self):
        while True:
            x = random.randint(0, len(self.maze[0]) - 1)
            y = random.randint(0, len(self.maze) - 1)
            if self.maze[y][x] == " ":
                return x * 60, y * 60

    def move(self):
        x, y = self.position
        px, py = self.pacman_position

        dx = px - x
        dy = py - y

        if abs(dx) > abs(dy):
            if dx > 0 and self.is_valid_move(x + 60, y):
                self.position = (x + 60, y)
            elif dx < 0 and self.is_valid_move(x - 60, y):
                self.position = (x - 60, y)
        else:
            if dy > 0 and self.is_valid_move(x, y + 60):
                self.position = (x, y + 60)
            elif dy < 0 and self.is_valid_move(x, y - 60):
                self.position = (x, y - 60)

        return self.position

    def is_valid_move(self, x, y):
        row, col = y // 60, x // 60
        return 0 <= row < len(self.maze) and 0 <= col < len(self.maze[0]) and self.maze[row][col] != "#"


class AStarGhost:
    def __init__(self, maze, pacman_position, current_position):
        self.maze = maze
        self.pacman_position = pacman_position
        self.current_position = current_position

    def move(self):
        path = self.astar()

        if path:
            next_position = path[0]
            self.current_position = next_position

    def astar(self):
        def heuristic(position):
            return abs(position[0] - self.pacman_position[0]) + abs(position[1] - self.pacman_position[1])

        def is_valid(position):
            x, y = position
            return 0 <= x < len(self.maze[0]) and 0 <= y < len(self.maze) and self.maze[y][x] == ' '

        open_set = []
        heapq.heappush(open_set, (0, self.current_position))
        came_from = {}
        g_score = {self.current_position: 0}

        while open_set:
            _, current = heapq.heappop(open_set)

            if current == self.pacman_position:
                # Reconstruct the path
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                path.reverse()
                return path

            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                neighbor = (current[0] + dx, current[1] + dy)
                if is_valid(neighbor):
                    tentative_g_score = g_score[current] + 1
                    if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                        came_from[neighbor] = current
                        g_score[neighbor] = tentative_g_score
                        f_score = tentative_g_score + heuristic(neighbor)
                        heapq.heappush(open_set, (f_score, neighbor))

        return None  # No path found
