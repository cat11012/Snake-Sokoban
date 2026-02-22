import pygame

pygame.init()

screen_info = pygame.display.Info()

MAX_SCREEN_WIDTH = screen_info.current_w
MAX_SCREEN_HEIGHT = screen_info.current_h

MIN_SCREEN_WIDTH = 10
MIN_SCREEN_HEIGHT = 10

screen_width = MAX_SCREEN_WIDTH/2
screen_height = MAX_SCREEN_HEIGHT/2

screen = pygame.display.set_mode((screen_width, screen_height), pygame.RESIZABLE)
clock = pygame.time.Clock()

