import pygame
pygame.init()

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

Scene_Screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
Scene_Screen.fill((0, 0, 0))  # Fills screen with specified colour
pygame.display.set_caption("Scene Two")

background = pygame.image.load('Sprites/CastleBackground.png')
background = pygame.transform.scale(background, (300, 300))
rect = background.get_rect()

while True:
    Scene_Screen.fill((0, 0, 0))
    Scene_Screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pygame.display.update()