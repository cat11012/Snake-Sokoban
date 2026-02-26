import os
import sys
import pygame

from python.setting.setting import *
from python.setting.global_enums import Colors

end_point_images_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'images', 'checkpoints', 'end_points')

blue =              pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'blue_end_point.png'))              .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
bright_dark_blue =  pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'bright_dark_blue_end_point.png'))  .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
bright_green_blue = pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'bright_green_blue_end_point.png')) .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
bright_green =      pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'bright_green_end_point.png'))      .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
bright_light_blue = pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'bright_light_blue_end_point.png')) .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
bright_orange =     pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'bright_orange_end_point.png'))     .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
pink =              pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'pink_end_point.png'))              .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
bright_red =        pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'bright_red_end_point.png'))        .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
bright_yellow =     pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'bright_yellow_end_point.png'))     .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
dark_blue =         pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'dark_blue_end_point.png'))         .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
dark_green =        pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'dark_green_end_point.png'))        .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
dark_orange =       pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'dark_orange_end_point.png'))       .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
dark_red =          pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'dark_red_end_point.png'))          .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
dark_yellow =       pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'dark_yellow_end_point.png'))       .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
green =             pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'green_end_point.png'))             .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))
purple =            pygame.transform.smoothscale(pygame.image.load(os.path.join(end_point_images_path, 'purple_end_point.png'))            .convert_alpha(), (SCREEN_HEIGHT/14, SCREEN_HEIGHT/14))

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
    Colors.PURPLE:              purple, 
}
