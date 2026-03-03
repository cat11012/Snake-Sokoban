import pygame
import logging

from python.utility.convert_tools import *
from python.setting.global_enums import *

logging.basicConfig(level=logging.DEBUG)

pygame.init()

screen_info = pygame.display.Info()

w = screen_info.current_w
h = screen_info.current_h
logging.info(f"Screen width: {w}, Screen height: {h}")
# size, SCREEN_SIZE_RATIO = find_screen_size((w, h))
# SCREEN_WIDTH, SCREEN_HEIGHT = size
size = (939, 704)
SCREEN_SIZE_RATIO = (4, 3)
SCREEN_WIDTH, SCREEN_HEIGHT = size
logging.info(f"Window size ratio: {SCREEN_SIZE_RATIO}")
logging.info(f"Window width: {size[0]}, Window height: {size[1]}")

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

interface_status = InterfaceStatus.GAMEPLAY