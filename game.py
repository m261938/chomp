import pygame
import sys
import random

from settings import *

pygame.init()

game_font = pygame.font.Font("assets/fonts/GistLight.otf", 85)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Chomp!")
screen.fill(WATER_COLOR)

pygame.draw.rect(screen, SAND_COLOR, (0, SCREEN_HEIGHT - SAND_HEIGHT, SCREEN_WIDTH, SAND_HEIGHT))  # old sand
sand = pygame.image.load("assets/images/sand.png").convert()
sand_top = pygame.image.load("assets/images/sand_top.png").convert()
seagrass = pygame.image.load("assets/images/seagrass.png").convert()
sand_top.set_colorkey((0, 0, 0))
seagrass.set_colorkey((0, 0, 0))

# blit sand tiles across bottom of screen
for i in range(SCREEN_WIDTH // TILE_SIZE):  # double divide cuts off decimals (quotient)
    screen.blit(sand, (i * TILE_SIZE, SCREEN_HEIGHT - TILE_SIZE))
    screen.blit(sand_top, (i * TILE_SIZE, SCREEN_HEIGHT - 2 * TILE_SIZE))
# randomly place 4 pieces of seagrass along sand
for i in range(4):
    x = random.randint(0, SCREEN_WIDTH)
    y = random.randint(SCREEN_HEIGHT-2*TILE_SIZE, SCREEN_HEIGHT)-(0.5*TILE_SIZE)  # offset seaweed to be on screen
    screen.blit(seagrass, (x, y))
# draw the CHOMP title
text = game_font.render("Chomp!",True, (0,69,200))
screen.blit(text, (SCREEN_WIDTH//2-text.get_width()//2,SCREEN_HEIGHT//2-TILE_SIZE))
pygame.display.flip()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('thanks for playing!')
            pygame.quit()
            sys.exit()
