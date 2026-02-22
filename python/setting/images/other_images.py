import os
import sys
import pygame

from ..setting import *

path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'images')

level_complete = pygame.image.load(os.path.join(path, 'level_complete.png')).convert_alpha()
red_apple = pygame.image.load(os.path.join(path, 'red_apple.png')).convert_alpha()
title = pygame.image.load(os.path.join(path, 'title.png')).convert_alpha()
