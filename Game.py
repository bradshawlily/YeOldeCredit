import pygame

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

# Sets screen size and colour
Menu_Screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
Menu_Screen.fill((105, 86, 58))  # Fills screen with specified colour
pygame.display.set_caption("Start Menu")
start_btn = pygame.image.load('Sprites/StartButton.png').convert_alpha()
quit_btn = pygame.image.load('Sprites/QuitButton.png').convert_alpha()


from Game import start_btn, quit_btn, Menu_Screen

pygame.init()
class Button:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        Menu_Screen.blit(self.image, (self.rect.x, self.rect.y))


start_button = Button(300, 100, start_btn)
quit_button = Button(300, 300, quit_btn)
# Game loop
while True:

    Menu_Screen.fill((202, 228, 241))
    start_button.draw()
    quit_button.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
