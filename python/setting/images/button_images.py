import os
import sys
import pygame

from ..setting import *

buttons_images_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'images', 'buttons')

home = {
    'normal':   pygame.image.load(os.path.join(buttons_images_path, 'home_button_normal.png'))  .convert_alpha(),
    'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'home_button_hovered.png')) .convert_alpha(),
    'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'home_button_clicked.png')) .convert_alpha()
}

back = {
    'normal':   pygame.image.load(os.path.join(buttons_images_path, 'back_button_normal.png'))  .convert_alpha(),
    'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'back_button_hovered.png')) .convert_alpha(),
    'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'back_button_clicked.png')) .convert_alpha()
}

forward = {
    'normal':   pygame.image.load(os.path.join(buttons_images_path, 'forward_button_normal.png'))  .convert_alpha(),
    'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'forward_button_hovered.png')) .convert_alpha(),
    'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'forward_button_clicked.png')) .convert_alpha()
}

backward = {
    'normal':   pygame.image.load(os.path.join(buttons_images_path, 'backward_button_normal.png'))  .convert_alpha(),
    'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'backward_button_hovered.png')) .convert_alpha(),
    'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'backward_button_clicked.png')) .convert_alpha()
}

circle_setting = {
    'normal':   pygame.image.load(os.path.join(buttons_images_path, 'circle_setting_button_normal.png'))  .convert_alpha(),
    'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'circle_setting_button_hovered.png')) .convert_alpha(),
    'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'circle_setting_button_clicked.png')) .convert_alpha()
}

square_setting = {
    'normal':   pygame.image.load(os.path.join(buttons_images_path, 'square_setting_button_normal.png'))  .convert_alpha(),
    'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'square_setting_button_hovered.png')) .convert_alpha(),
    'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'square_setting_button_clicked.png')) .convert_alpha()
}

open_menu = {
    'normal':   pygame.image.load(os.path.join(buttons_images_path, 'open_menu_button_normal.png'))  .convert_alpha(),
    'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'open_menu_button_hovered.png')) .convert_alpha(),
    'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'open_menu_button_clicked.png')) .convert_alpha()
}

endless_mode_start = {
    'normal':   pygame.image.load(os.path.join(buttons_images_path, 'endless_mode_start_button_normal.png'))  .convert_alpha(),
    'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'endless_mode_start_button_hovered.png')) .convert_alpha(),
    'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'endless_mode_start_button_clicked.png')) .convert_alpha()
}

orig_circle_button = {
    'normal':   pygame.image.load(os.path.join(buttons_images_path, 'circle_button_normal.png'))    .convert_alpha(),
    'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'circle_button_hovered.png'))   .convert_alpha(),
    'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'circle_button_clicked.png'))   .convert_alpha()
}

orig_square_button = {
    'normal':   pygame.image.load(os.path.join(buttons_images_path, 'square_button_normal.png'))    .convert_alpha(),
    'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'square_button_hovered.png'))   .convert_alpha(),
    'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'square_button_clicked.png'))   .convert_alpha()
}

