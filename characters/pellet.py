import pygame


class Pellet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.collected = False
        self.image = pygame.image.load("data/images/pellet.png")
        self.image = pygame.transform.scale(self.image, (20, 20))

    def collect(self):
        self.collected = True
