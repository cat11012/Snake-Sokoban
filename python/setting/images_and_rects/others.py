import os
import pygame

from python.setting.setting import *

path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'images')

level_complete_image = pygame.image.load(os.path.join(path, 'level_complete5.png')).convert_alpha()
    #(SCREEN_HEIGHT/10*4.5/69*124, SCREEN_HEIGHT/10*4.5)
level_complete_rect = level_complete_image.get_rect(centerx = SCREEN_WIDTH/2, bottom = SCREEN_HEIGHT / 5 * 3)

red_apple_image = pygame.image.load(os.path.join(path, 'red_apple.png')).convert_alpha()

title_image = pygame.transform.smoothscale(
    pygame.image.load(os.path.join(path, 'title.png')).convert_alpha(),
    (SCREEN_HEIGHT/15*17, SCREEN_HEIGHT/5)
)
title_rect = title_image.get_rect(centerx = SCREEN_WIDTH/2, top = SCREEN_HEIGHT / 10)

background_image = pygame.transform.smoothscale(
    pygame.image.load(
        os.path.join(path, "backgrounds", f'{SCREEN_SIZE_RATIO[0]}x{SCREEN_SIZE_RATIO[1]}.png')
    ).convert_alpha(), (SCREEN_WIDTH, SCREEN_HEIGHT)
)
background_rect = background_image.get_rect(topleft = (0, 0))
