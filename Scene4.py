import pygame
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

Scene_Screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
Scene_Screen.fill((0, 0, 0))  # Fills screen with specified colour
pygame.display.set_caption("Scene Four")

background = pygame.image.load('Sprites/throne-room.png')
background = pygame.transform.scale(background, (SCREEN_HEIGHT, SCREEN_WIDTH))
background = pygame.transform.flip(background, True, False)
hero = pygame.image.load("Sprites/hero_transparent.png")
hero = pygame.transform.scale(hero, (350, 300))
jester = pygame.image.load("Sprites/Jester_Transparent.png")
jester = pygame.transform.scale(jester, (350, 300))
rect = background.get_rect()
currentX = -210

while True:
    Scene_Screen.fill((0, 0, 0))
    Scene_Screen.blit(background, (0, 0))
    Scene_Screen.blit(hero, (currentX,170))
    Scene_Screen.blit(jester, (400,170))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            currentX -= 20
            print(currentX)
        elif keys[pygame.K_RIGHT]:
            currentX += 20
            print(currentX)
       
        if currentX == 650:
            import Scene3

        pygame.display.update()