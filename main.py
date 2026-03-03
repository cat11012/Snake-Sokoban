import pygame

from python.setting.setting import *
from python.classes.button import buttons
from python.classes.chessboard import chessboard
import python.setting.images_and_rects.others as images_rects
from python.setting.global_enums import InterfaceStatus

def handle_events() -> bool:
    """return True if the game should continue, False if it should quit"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button down
            for button in buttons:
                button.mouse_click(pygame.mouse.get_pos(), interface_status)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left mouse button up
            for button in buttons:
                button.mouse_release(pygame.mouse.get_pos(), interface_status)
        if event.type == pygame.KEYDOWN:
            if interface_status == InterfaceStatus.GAMEPLAY:
                chessboard.key_press(event.key)
        if event.type == pygame.KEYUP:
            if interface_status == InterfaceStatus.GAMEPLAY:
                chessboard.key_release(event.key)
    return True

def update() -> None:
    buttons.update(pygame.mouse.get_pos(), interface_status)
    if interface_status == InterfaceStatus.GAMEPLAY:
        chessboard.update()

def draw() -> None:
    if interface_status == InterfaceStatus.LOBBY:
        screen.blit(images_rects.background_image, images_rects.background_rect)
        screen.blit(images_rects.title_image, images_rects.title_rect)
    elif interface_status == InterfaceStatus.GAMEPLAY:
        screen.blit(chessboard.image, chessboard.rect)

    for button in buttons:
        button.draw(screen)

def main():
    running = True
    while running:
        running = handle_events()
        update()
        draw()
        pygame.display.flip()
        clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
