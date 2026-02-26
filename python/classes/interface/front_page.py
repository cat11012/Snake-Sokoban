import pygame

from python.setting.setting import *
import python.setting.images.images as images
import python.setting.images.button_images as button_images

class FrontPage:
    def __init__(self):
        self.image = pygame.Surface(SCREEN_SIZE_RATIO)
        self.image.fill(("#60bfff"))
        self.rect = self.image.get_rect(topleft=(0, 0))
        