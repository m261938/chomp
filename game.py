import pygame
import time

print(f'the quit event is type {pygame.QUIT}')
pygame.init()

screen = pygame.display.set_mode((400,400))
pygame.display.set_caption("Chomp!")
screen.fill((101,178,255))
pygame.draw.rect(screen,(246,230,178),(0,380,400,400))
pygame.draw.rect(screen,(0,255,0),(200,200,40,20))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('not today! this game runs forrrreverrrr')
