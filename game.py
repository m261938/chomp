import pygame
import sys

# dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 500
SAND_HEIGHT = 20
TILE_SIZE = 64  # tiles are square height == width

# colors
WATER_COLOR = (101, 178, 255)
SAND_COLOR = (246, 230, 178)
pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)

pygame.draw.rect(screen, SAND_COLOR, (0, SCREEN_HEIGHT - SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))  # sand
sand = pygame.image.load("assets/images/sand.png").convert()
screen.blit(sand, (SCREEN_WIDTH / 2 - TILE_SIZE / 2, SCREEN_HEIGHT / 2 - TILE_SIZE / 2))
pygame.display.flip()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('thanks for playing!')
            pygame.quit()
            sys.exit()
