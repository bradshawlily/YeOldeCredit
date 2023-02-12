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
speechBubble = pygame.image.load("Sprites/SpeechBubble_Transparent.png")
speechBubble = pygame.transform.scale(speechBubble, (330, 220))
rect = background.get_rect()
currentX = -100

#https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('msgothic', 12)

text_1 = 'Hello Valiant Knight! '
text_2 = 'You have a choice to make...'
text_3 = 'Will you take a loan'
text_4 = 'for upgraded armour and ...'
text_5 ='a potion of strength?'
text_6 = '*There is a 40%APR and Terms and Conditions Apply*'
text_7 ='*Including you must pay the loan back within 24 hours.*'
text_8 = 'or will you brave the dragon yourself?'
text_9 ='Press Y or N to make a decision my hero!'

title_lines = [text_1, text_2, text_3, text_4, text_5, text_6, text_7, text_8, text_9]


text_10 = my_font.render( "Here is your upgrade!", False, (0,0,0))
text_11 = my_font.render("Well I wish you luck....", False, (0,0,0))

#https://stackoverflow.com/questions/71243696/how-to-make-text-rects-appear-one-after-another-after-a-delay-in-pygame
title_delay     = 2000  # Milliseconds between title advances
title_count     = 9     # How many titles are in the animation
title_index     = 0     # what is the currently displayed title
title_next_time = title_delay  # clock starts at 0, time for first title



def blit_text(surface, text, pos, font, color=pygame.Color('black')):
    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width = 500
    max_height = 300
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            Scene_Screen.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.

while True:

    Scene_Screen.fill((0, 0, 0))
    Scene_Screen.blit(background, (0, 0))
    Scene_Screen.blit(jester, (420,210))
    Scene_Screen.blit(speechBubble,(300,100))
    
    clock = pygame.time.get_ticks()   # time now

    

    Scene_Screen.blit(hero, (currentX,170))

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_y:
                Scene_Screen.blit( text_10, ( 400, 170 ))
            if event.key == pygame.K_n:
                Scene_Screen.blit(text_11, (400,170))

    
        keys = pygame.key.get_pressed()
        
        
        if keys[pygame.K_LEFT]:
            currentX -= 20
            print(currentX)
        elif keys[pygame.K_RIGHT]:
            currentX += 20
            print(currentX)

        if currentX == 640:
            import Scene3
            
        if ( title_index < title_count ):
             blit_text(Scene_Screen, title_lines[ title_index ], ( 400, 170 ),my_font )
             #https://stackoverflow.com/questions/71243696/how-to-make-text-rects-appear-one-after-another-after-a-delay-in-pygame
             # Is it time to update to the next title?
             if ( clock > title_next_time ):
                 title_next_time = clock + title_delay  # some seconds in the future
                 title_index += 1 # advance to next title-image  
                       

        pygame.display.update()