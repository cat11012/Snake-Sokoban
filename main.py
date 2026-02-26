import pygame

from python.setting.setting import *

def handle_events() -> bool:
    """return True if the game should continue, False if it should quit"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return False
    return True

def main():
    running = True
    while running:
        running = handle_events()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
