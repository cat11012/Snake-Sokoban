import os
import sys
import pygame

from python.setting.setting import *

portal_images_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'images', 'portals')

blue =              pygame.image.load(os.path.join(portal_images_path, 'blue_portal.png'))              .convert_alpha()
bright_dark_blue =  pygame.image.load(os.path.join(portal_images_path, 'bright_dark_blue_portal.png'))  .convert_alpha()
bright_green_blue = pygame.image.load(os.path.join(portal_images_path, 'bright_green_blue_portal.png')) .convert_alpha()
bright_green =      pygame.image.load(os.path.join(portal_images_path, 'bright_green_portal.png'))      .convert_alpha()
bright_light_blue = pygame.image.load(os.path.join(portal_images_path, 'bright_light_blue_portal.png')) .convert_alpha()
bright_orange =     pygame.image.load(os.path.join(portal_images_path, 'bright_orange_portal.png'))     .convert_alpha()
pink =              pygame.image.load(os.path.join(portal_images_path, 'pink_portal.png'))              .convert_alpha()
bright_red =        pygame.image.load(os.path.join(portal_images_path, 'bright_red_portal.png'))        .convert_alpha()
bright_yellow =     pygame.image.load(os.path.join(portal_images_path, 'bright_yellow_portal.png'))     .convert_alpha()
dark_blue =         pygame.image.load(os.path.join(portal_images_path, 'dark_blue_portal.png'))         .convert_alpha()
dark_green =        pygame.image.load(os.path.join(portal_images_path, 'dark_green_portal.png'))        .convert_alpha()
dark_orange =       pygame.image.load(os.path.join(portal_images_path, 'dark_orange_portal.png'))       .convert_alpha()
dark_red =          pygame.image.load(os.path.join(portal_images_path, 'dark_red_portal.png'))          .convert_alpha()
dark_yellow =       pygame.image.load(os.path.join(portal_images_path, 'dark_yellow_portal.png'))       .convert_alpha()
green =             pygame.image.load(os.path.join(portal_images_path, 'green_portal.png'))             .convert_alpha()
purple =            pygame.image.load(os.path.join(portal_images_path, 'purple_portal.png'))            .convert_alpha()
sliver_gelatin =    pygame.image.load(os.path.join(portal_images_path, 'sliver_gelatin_portal.png'))    .convert_alpha()

images = [
    blue, 
    bright_dark_blue, 
    bright_green_blue, 
    bright_green, 
    bright_light_blue, 
    bright_orange, 
    pink, 
    bright_red, 
    bright_yellow, 
    dark_blue, 
    dark_green, 
    dark_orange, 
    dark_red, 
    dark_yellow, 
    green, 
    purple, 
    sliver_gelatin
]
