import pygame
import sys

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

# Sets screen size and colour
Menu_Screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
Menu_Screen.fill((105, 86, 58))  # Fills screen with specified colour
pygame.display.set_caption("Start Menu")
start_btn = pygame.image.load('Sprites/StartButton.png').convert_alpha()
quit_btn = pygame.image.load('Sprites/QuitButton.png').convert_alpha()
gameLogo = pygame.image.load("Sprites/LogoSign-removebg-preview.png").convert_alpha()

pygame.init()
class Button:
    def __init__(self, x, y, image):
        self.image = image #100x241
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.x = x
        self.y = y

    def draw(self):
        Menu_Screen.blit(self.image, (self.rect.x, self.rect.y))

class Logo:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        Menu_Screen.blit(self.image, (self.rect.x, self.rect.y))


logo = Logo(100, 1, gameLogo)
start_button = Button(100, 375, start_btn)
quit_button = Button(450, 375, quit_btn)
# Game loop
while True:

    Menu_Screen.fill((202, 228, 241))
    logo.draw()
    start_button.draw()
    quit_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if (start_button.x < x and x < start_button.x+241) and (start_button.y < y and y < start_button.y+100):
                import Scene1
                
            if (quit_button.x < x and x < quit_button.x+241) and (quit_button.y < y and y < quit_button.y+100):
                pygame.quit()

    pygame.display.update()
