import pygame, sys
from pygame.examples.video import y
from pygame.locals import *
import random

pygame.init()

class Button:
    def_init_(self, x, y, width, height, buttonText='Button', onclick):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int)width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
