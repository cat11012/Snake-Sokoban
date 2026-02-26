import pygame

import python.setting.images.box_images as images
from python.setting.global_enums import Colors

class Box:
    def __init__(self, topleft: tuple[int, int], color: Colors):
        self.image = images.images[color]
        self.rect = self.image.get_rect(topleft=topleft)
        self.rect.topleft = topleft
        
    def update(self, topleft: tuple[int, int]):
        self.rect.topleft = topleft

