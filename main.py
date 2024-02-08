import pygame
import requests

scale = 25

pygame.init()
screen = pygame.display.set_mode((600, 480))
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()