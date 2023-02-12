import pygame
import dragonBossFight
import random
pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 800

Scene_Screen = pygame.display.set_mode((SCREEN_HEIGHT, SCREEN_WIDTH))
Scene_Screen.fill((0, 0, 0))  # Fills screen with specified colour
pygame.display.set_caption("Scene Five")

#https://stackoverflow.com/questions/71243696/how-to-make-text-rects-appear-one-after-another-after-a-delay-in-pygame
title_delay     = 2000  # Milliseconds between title advances
title_count     = 8    # How many titles are in the animation
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

background = pygame.image.load('Sprites/castleGate.png')
background = pygame.transform.scale(background, (SCREEN_HEIGHT, SCREEN_WIDTH))
hero = pygame.image.load("Sprites/hero_transparent.png")
hero = pygame.transform.scale(hero, (350, 300))
dragon = pygame.image.load("Sprites/image__3_-removebg-preview.png")
dragon = pygame.transform.scale(dragon, (700,500))
speechBubble = pygame.image.load("Sprites/SpeechBubble_Transparent.png")
speechBubble = pygame.transform.scale(speechBubble, (330, 220))
speechBubble = pygame.transform.flip(speechBubble, True, False)
rect = background.get_rect()
currentX = -210

#https://stackoverflow.com/questions/20842801/how-to-display-text-in-pygame
pygame.font.init() # you have to call this at the start, 
                   # if you want to use this module.
my_font = pygame.font.SysFont('msgothic', 12)
Phase2 = False
phase2Data = {}

text_1 = 'You dare challenge me, human?'
text_2 = 'Very well, mortal.'
text_3 = 'I challenge you to a battle!'
text_4 = 'But first...'
text_5 ='Do you know about credit scores?'
accounts = dragonBossFight.phase1_setup()
text_6 = 'Here is an account that I found in these dungeons...\nTell me, does it have a good credit score?'
text_7 = "Answer with y or n"
account = random.choice(accounts)
account_verdict = account["accountCreditScore"]
account_data = account["account"]

texts = [text_1,text_2,text_3,text_4,text_5,text_6,account_data,text_7]
displayedBanner = False

while True:
    if Phase2 == True:
        text_8 = 'Final Challenge!'
        text_9 = 'This account has some transactions'
        text_10 = 'Are any of them fraudulent?'
        text_11 = 'Answer A or B'
        transactions = phase2Data["transactions"]
        text_12 = transactions[0]
        text_13 = transactions[1]
        text_14 = transactions[2]
        texts.append(text_8)
        texts.append(text_9)
        texts.append(text_10)
        texts.append(text_11)
        texts.append(text_12)
        texts.append(text_13)
        texts.append(text_14)
        title_count = 15
    Scene_Screen.fill((0, 0, 0))
    Scene_Screen.blit(background, (0, 0))
    Scene_Screen.blit(hero, (currentX,170))
    Scene_Screen.blit(dragon, (150,25))
    Scene_Screen.blit(speechBubble,(300,100))
    clock = pygame.time.get_ticks()   # time now

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            currentX -= 20
        elif keys[pygame.K_RIGHT]:
            currentX += 20
        elif keys[pygame.K_y]:
            if account_verdict == "bad":
                failureText = my_font.render("Wrong! Hahaha", False, (0,0,0))
                Scene_Screen.blit(failureText, (400,170))
                import Scene7

            else:
                correctText = my_font.render("Hmm...Correct...", False, (0,0,0))
                Scene_Screen.blit(correctText, (400,170))
                phase2Data = dragonBossFight.phase2_setup()
                Phase2 = True
        elif keys[pygame.K_n]:
            if account_verdict == "good":
                failureText = my_font.render("Wrong! Hahaha", False, (0,0,0))
                Scene_Screen.blit(failureText, (400,170))
                import Scene7
            else:
                correctText = my_font.render("Hmm...Correct...", False, (0,0,0))
                Scene_Screen.blit(correctText, (400,170))
                phase2Data = dragonBossFight.phase2_setup()
                Phase2 = True
        elif keys[pygame.K_a]:
            correctText = my_font.render("HOW DID YOU KNOW??\nI AM DEFEATED!", False, (0,0,0))
            Scene_Screen.blit(correctText, (400,170))
            import Scene6
        elif keys[pygame.K_b]:
            failureText = my_font.render("Wrong! Hahaha", False, (0,0,0))
            Scene_Screen.blit(failureText, (400,170))
            import Scene7
        if ( title_index < title_count ):
            blit_text(Scene_Screen, texts[ title_index ], ( 400, 170 ),my_font )
            #https://stackoverflow.com/questions/71243696/how-to-make-text-rects-appear-one-after-another-after-a-delay-in-pygame
            # Is it time to update to the next title?
            if ( clock > title_next_time ):
                title_next_time = clock + title_delay  # some seconds in the future
                title_index += 1 # advance to next title-image  

        pygame.display.update()