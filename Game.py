import pygame
from pygame.locals import *

pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

# Sets screen size and colour
Menu_Screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
Menu_Screen.fill((105, 86, 58))  # Fills screen with specified colour
pygame.display.set_caption("Start Menu")



# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
