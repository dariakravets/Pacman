import pygame
import sys
import pygame.font

from characters.ghosts import GreedyGhost
from characters.pacman import Pacman
from characters.pellet import Pellet
from maze import load_maze, draw_maze

pygame.init()
font = pygame.font.Font(None, 48)

screen = pygame.display.set_mode((900, 780))
pygame.display.set_caption("Pac-Man Game")

maze_layout = load_maze("data/maze_layout.txt")
pellet_image = pygame.image.load("data/images/pellet.png")

pacman = Pacman(360, 360, 450, 350, maze_layout)
pacman.resize(60, 60)

pink_ghost = GreedyGhost(maze_layout, pacman.get_position())

pellet_image = pygame.transform.scale(pellet_image, (20, 20))
pellets = []
for y, row in enumerate(maze_layout):
    for x, tile in enumerate(row):
        if tile == ".":
            pellet = Pellet(x * 60 + 20, y * 60 + 20)
            pellets.append(pellet)

# Score
score = -1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # Move Pac-Man up
                pacman.move(0, -10)
            elif event.key == pygame.K_DOWN:
                # Move Pac-Man down
                pacman.move(0, 10)
            elif event.key == pygame.K_LEFT:
                # Move Pac-Man left
                pacman.move(-10, 0)
            elif event.key == pygame.K_RIGHT:
                # Move Pac-Man right
                pacman.move(10, 0)

    screen.fill((0, 0, 0))

    draw_maze(screen, maze_layout, 60, 60)

    for pellet in pellets:
        if pacman.rect.topleft == (pellet.x - 20, pellet.y - 20):
            pellet.collect()
            score += 1
            pellets.remove(pellet)

    for pellet in pellets:
        screen.blit(pellet.image, (pellet.x, pellet.y))

    pacman.draw(screen)

    ghost_position = pink_ghost.move()

    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    score_text_rect = score_text.get_rect()
    score_text_rect.topleft = (5, 730)
    screen.blit(score_text, score_text_rect)

    pygame.display.update()

pygame.quit()
sys.exit()
