import os
import sys
import pygame

from python.setting.setting import *
from python.setting.global_enums import Colors

checkpoint_images_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'images', 'checkpoints', 'check_points')

blue =              pygame.image.load(os.path.join(checkpoint_images_path, 'blue_check_point.png'))              .convert_alpha()
bright_dark_blue =  pygame.image.load(os.path.join(checkpoint_images_path, 'bright_dark_blue_check_point.png'))  .convert_alpha()
bright_green_blue = pygame.image.load(os.path.join(checkpoint_images_path, 'bright_green_blue_check_point.png')) .convert_alpha()
bright_green =      pygame.image.load(os.path.join(checkpoint_images_path, 'bright_green_check_point.png'))      .convert_alpha()
bright_light_blue = pygame.image.load(os.path.join(checkpoint_images_path, 'bright_light_blue_check_point.png')) .convert_alpha()
bright_orange =     pygame.image.load(os.path.join(checkpoint_images_path, 'bright_orange_check_point.png'))     .convert_alpha()
pink =              pygame.image.load(os.path.join(checkpoint_images_path, 'pink_check_point.png'))              .convert_alpha()
bright_red =        pygame.image.load(os.path.join(checkpoint_images_path, 'bright_red_check_point.png'))        .convert_alpha()
bright_yellow =     pygame.image.load(os.path.join(checkpoint_images_path, 'bright_yellow_check_point.png'))     .convert_alpha()
dark_blue =         pygame.image.load(os.path.join(checkpoint_images_path, 'dark_blue_check_point.png'))         .convert_alpha()
dark_green =        pygame.image.load(os.path.join(checkpoint_images_path, 'dark_green_check_point.png'))        .convert_alpha()
dark_orange =       pygame.image.load(os.path.join(checkpoint_images_path, 'dark_orange_check_point.png'))       .convert_alpha()
dark_red =          pygame.image.load(os.path.join(checkpoint_images_path, 'dark_red_check_point.png'))          .convert_alpha()
dark_yellow =       pygame.image.load(os.path.join(checkpoint_images_path, 'dark_yellow_check_point.png'))       .convert_alpha()
green =             pygame.image.load(os.path.join(checkpoint_images_path, 'green_check_point.png'))             .convert_alpha()
purple =            pygame.image.load(os.path.join(checkpoint_images_path, 'purple_check_point.png'))            .convert_alpha()

images = {
    Colors.BLUE:                blue, 
    Colors.BRIGHT_DARK_BLUE:    bright_dark_blue, 
    Colors.BRIGHT_GREEN_BLUE:   bright_green_blue, 
    Colors.BRIGHT_GREEN:        bright_green, 
    Colors.BRIGHT_LIGHT_BLUE:   bright_light_blue, 
    Colors.BRIGHT_ORANGE:       bright_orange, 
    Colors.PINK:                pink, 
    Colors.BRIGHT_RED:          bright_red, 
    Colors.BRIGHT_YELLOW:       bright_yellow, 
    Colors.DARK_BLUE:           dark_blue, 
    Colors.DARK_GREEN:          dark_green, 
    Colors.DARK_ORANGE:         dark_orange, 
    Colors.DARK_RED:            dark_red, 
    Colors.DARK_YELLOW:         dark_yellow, 
    Colors.GREEN:               green, 
    Colors.PURPLE:              purple
}
