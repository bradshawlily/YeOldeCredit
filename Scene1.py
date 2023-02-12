import pygame
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

Scene_Screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
Scene_Screen.fill((0, 0, 0))  # Fills screen with specified colour
pygame.display.set_caption("Scene One")

background = pygame.image.load('Sprites/FieldBckgrnd.png')
villager = pygame.image.load("Sprites/villager_noTransparent.png")
hero = pygame.image.load("Sprites/hero_transparent.png")
speechBubble = pygame.image.load("Sprites/SpeechBubble_Transparent.png")
#Method to scale the background to the size of the image was found on CodeSpeedy "Scale image to fit screen in Pygame Python" (https://www.codespeedy.com/scale-image-to-fit-screen-in-pygame-python/)
background = pygame.transform.scale(background, (SCREEN_HEIGHT, SCREEN_WIDTH))
villager = pygame.transform.scale(villager, (350, 300))
hero = pygame.transform.scale(hero, (500, 400))
speechBubble = pygame.transform.scale(speechBubble, (320, 220))
#Method to flip an image was found on GeeksForGeeks "Pygame – Flip the image" (https://www.geeksforgeeks.org/pygame-flip-the-image/)
villager = pygame.transform.flip(villager, True, False)
#speechBubble = pygame.transform.flip(speechBubble, True, False)
background_rect = background.get_rect()
currentX = 50

#https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('msgothic', 12)
text_surface1 = my_font.render('Save us from it! ',False, (0, 0, 0))
text_surface2 = my_font.render('The Bad Credit Dragon!', False, (0, 0, 0))


# Game loop
while True:
    Scene_Screen.fill((0, 0, 0))
    Scene_Screen.blit(background, background_rect)
    Scene_Screen.blit(villager, (500,100))
    Scene_Screen.blit(speechBubble, (350, 50))
    Scene_Screen.blit(text_surface1, (440,120))
    Scene_Screen.blit(text_surface2, (440,145))
    Scene_Screen.blit(hero, (currentX,100))



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        keys = pygame.key.get_pressed() #Method to move image across the screen was found on Stack Overflow "How to move an image in pygame with key press?" (https://stackoverflow.com/questions/67230513/how-to-move-an-image-in-pygame-with-key-press)
        if keys[pygame.K_LEFT]:
            currentX -= 20
        elif keys[pygame.K_RIGHT]:
            currentX += 20
       
        if currentX == 670:
            import Scene2

        pygame.display.update()