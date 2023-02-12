import pygame
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

Scene_Screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
Scene_Screen.fill((0, 0, 0))  # Fills screen with specified colour
pygame.display.set_caption("Scene One")

background = pygame.image.load('Sprites/FieldBckgrnd.png')
#Method to scale the background to the size of the image was found on CodeSpeedy "Scale image to fit screen in Pygame Python" (https://www.codespeedy.com/scale-image-to-fit-screen-in-pygame-python/)
background = pygame.transform.scale(background, (SCREEN_HEIGHT, SCREEN_WIDTH))
rect = background.get_rect()

# Game loop
while True:
    Scene_Screen.fill((0, 0, 0))
    Scene_Screen.blit(background, rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        Scene_Screen.blit(background, (0,0))
        pygame.display.update()