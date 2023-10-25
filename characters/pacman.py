import pygame


class Pacman:
    def __init__(self, x, y, maze_width, maze_height, maze_layout):
        self.image = pygame.image.load("data/images/pacman.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.speed = 6

        self.maze_width = maze_width
        self.maze_height = maze_height
        self.maze_layout = maze_layout

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def resize(self, width, height):
        self.image = pygame.transform.scale(self.image, (width, height))

    def move(self, dx, dy):
        new_x = self.rect.x + dx * self.speed
        new_y = self.rect.y + dy * self.speed

        grid_x = new_x // 60
        grid_y = new_y // 60

        if (0 <= grid_x < self.maze_width) and (0 <= grid_y < self.maze_height):
            # Check if the new position is a path (not a wall)
            if self.maze_layout[grid_y][grid_x] == '.':
                self.rect.x = new_x
                self.rect.y = new_y

    def get_position(self):
        return (self.rect.x, self.rect.y)
