import pygame
from enum import Enum

import python.setting.images_and_rects.buttons as images

class ButtonNames(Enum):
    HOME = images.home_images
    FORWARD = images.forward_images
    BACKWARD = images.backward_images
    RETRY = images.retry_images
    OPEN_MENU = images.open_menu_images
    ENDLESS_MODE_START = images.endless_mode_start_images
    ORIG_CIRCLE = images.orig_circle_button_images
    ORIG_SQUARE = images.orig_square_button_images
    LEVEL = images.level_button_template_images

class Button(pygame.sprite.Sprite):
    def __init__(self, name: ButtonNames, state: str, rect: pygame.Rect):
        super().__init__()
        self.name = name
        self.image = images.__dict__[name.value]['normal']
        self.rect = rect
