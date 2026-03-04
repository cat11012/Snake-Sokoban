import logging

import pygame

from python.setting import setting
from python.classes.button import buttons
import python.classes.chessboard as chessboard_module
import python.setting.images_and_rects.others as images_rects
from python.setting.global_enums import InterfaceStatus

def handle_events() -> bool:
    """return True if the game should continue, False if it should quit"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:  # Left mouse button down
            for button in buttons:
                button.mouse_click(pygame.mouse.get_pos(), setting.interface_status)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # Left mouse button up
            for button in buttons:
                button.mouse_release(pygame.mouse.get_pos(), setting.interface_status)
        if event.type == pygame.KEYDOWN:
            if setting.interface_status == InterfaceStatus.GAMEPLAY:
                chessboard_module.chessboard.key_press(event.key)
        if event.type == pygame.KEYUP:
            if setting.interface_status == InterfaceStatus.GAMEPLAY:
                chessboard_module.chessboard.key_release(event.key)
    return True

def update() -> None:
    # logging.debug(f"interface status: {setting.interface_status}")

    buttons.update(pygame.mouse.get_pos(), setting.interface_status)
    if setting.interface_status == InterfaceStatus.GAMEPLAY:
        chessboard_module.chessboard.update()

def draw() -> None:
    setting.screen.fill("#21941f") 

    if setting.interface_status == InterfaceStatus.LOBBY:
        setting.screen.blit(images_rects.background_image, images_rects.background_rect)
        setting.screen.blit(images_rects.title_image, images_rects.title_rect)
    if setting.interface_status in [InterfaceStatus.GAMEPLAY, InterfaceStatus.LEVEL_COMPLETE]:
        setting.screen.blit(chessboard_module.chessboard.image, chessboard_module.chessboard.rect)
    if setting.interface_status == InterfaceStatus.LEVEL_COMPLETE:
        setting.screen.blit(images_rects.level_complete_image, images_rects.level_complete_rect)

    for button in buttons:
        button.draw(setting.screen)

def main():
    running = True
    while running:
        running = handle_events()
        update()
        draw()
        pygame.display.flip()
        setting.clock.tick(60)
    
    pygame.quit()

if __name__ == "__main__":
    main()
