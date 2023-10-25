import pygame


class StraightMovingGhost:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = (1, 0)  # Initial direction
        self.speed = 1

    def move(self, maze_layout):
        new_x = self.x + self.direction[0] * self.speed
        new_y = self.y + self.direction[1] * self.speed

        grid_x = int(new_x // 60)
        grid_y = int(new_y // 60)

        if (0 <= grid_x < len(maze_layout[0])) and (0 <= grid_y < len(maze_layout)):
            if maze_layout[grid_y][grid_x] == '#':
                # If the new position is a wall, turn left
                self.direction = (-self.direction[1], self.direction[0])

        self.x = new_x
        self.y = new_y


class LoopedPathGhost:
    def __init__(self, waypoints):
        self.waypoints = waypoints
        self.waypoint_index = 0
        self.speed = 1  # Adjust the speed as needed
        self.x, self.y = waypoints[self.waypoint_index]

    def move(self):
        target_x, target_y = self.waypoints[self.waypoint_index]
        dx = target_x - self.x
        dy = target_y - self.y

        length = (dx ** 2 + dy ** 2) ** 0.5
        if length != 0:
            dx /= length
            dy /= length

        self.x += dx * self.speed
        self.y += dy * self.speed

        if abs(self.x - target_x) < self.speed and abs(self.y - target_y) < self.speed:
            self.waypoint_index = (self.waypoint_index + 1) % len(self.waypoints)
