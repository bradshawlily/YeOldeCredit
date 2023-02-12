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
speech = pygame.image.load("Sprites/SpeechBubble_Transparent.png")
rect = background.get_rect()
currentX = -210

#https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('msgothic', 12)
text_surface1 = my_font.render('Hello Valiant Knight! ',False, (0, 0, 0))
text_surface2 = my_font.render('You have a choice to make...', False, (0, 0, 0))
text_surface3 = my_font.render('Will you take a loan,', False, (0, 0, 0))
text_surface4 = my_font.render('for upgraded armour and ...', False, (0, 0, 0))
text_surface5 = my_font.render('a potion of strength?', False, (0, 0, 0))
text_surface6 = my_font.render('*There is a 40%APR and Terms and Conditions Apply*', False, (0, 0, 0))
text_surface7 = my_font.render('*Including you must pay the loan back within 24 hours.*', False, (0, 0, 0))
text_surface8 = my_font.render('or will you brave the dragon yourself?', False, (0, 0, 0))
text_surface9 = my_font.render('Press Y or N to make a decision my hero!', False, (0, 0, 0))

title_lines = [ text_surface1, text_surface2, text_surface3, text_surface4, text_surface5, text_surface6, text_surface7, text_surface8, text_surface9 ]
#https://stackoverflow.com/questions/71243696/how-to-make-text-rects-appear-one-after-another-after-a-delay-in-pygame
title_delay     = 2000  # Milliseconds between title advances
title_count     = 9     # How many titles are in the animation
title_index     = 0     # what is the currently displayed title
title_next_time = title_delay  # clock starts at 0, time for first title

while True:

    Scene_Screen.fill((0, 0, 0))
    Scene_Screen.blit(background, (0, 0))
    Scene_Screen.blit(hero, (currentX,170))
    Scene_Screen.blit(jester, (400,170))
    
    clock = pygame.time.get_ticks()   # time now

    if ( title_index < title_count ):
        Scene_Screen.blit( title_lines[ title_index ], ( 10, 10 ) )
#https://stackoverflow.com/questions/71243696/how-to-make-text-rects-appear-one-after-another-after-a-delay-in-pygame
        # Is it time to update to the next title?
        if ( clock > title_next_time ):
            title_next_time = clock + title_delay  # some seconds in the future
            title_index += 1 # advance to next title-image


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