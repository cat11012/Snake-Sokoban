import pygame
import logging
import copy
from enum import Enum
from typing import Callable

from python.setting import setting
import python.setting.images_and_rects.buttons as image_rect
import python.setting.global_enums as global_enums
import python.classes.chessboard as chessboard_module

class ButtonsType(Enum):
    HOME = image_rect.home_images
    FORWARD = image_rect.forward_images
    BACKWARD = image_rect.backward_images
    RETRY = image_rect.retry_images
    OPEN_MENU = image_rect.open_menu_images
    ENDLESS_MODE_START = image_rect.endless_mode_start_images
    ORIG_CIRCLE = image_rect.orig_circle_button_images
    ORIG_SQUARE = image_rect.orig_square_button_images
    LEVEL = image_rect.level_button_template_images

class ButtonState(Enum):
    NORMAL = 'normal'
    HOVERED = 'hovered'
    CLICKED = 'clicked'

class Button(pygame.sprite.Sprite):
    def __init__(
            self, 
            button_type: ButtonsType, 
            rect: pygame.Rect, 
            command: Callable[..., any], 
            interface_status: global_enums.InterfaceStatus, 
            only_draw_interface_status: global_enums.InterfaceStatus = global_enums.InterfaceStatus.NONE,
            level_button_num: int|None = None
        ) -> None:
        """
        :param rect: only works when argument is come from setting.images_and_rects.buttons module.
        :param level_button_num: only for level button.
        """
        super().__init__()
        self.button_type = button_type
        self.image = button_type.value['normal']
        self.rect = rect
        self.state = ButtonState.NORMAL
        self.command = command
        self.interface_status = interface_status
        self.only_draw_interface_status = only_draw_interface_status
        if self.button_type == ButtonsType.LEVEL:
            self.level_button_num = level_button_num
        
        logging.debug(f"Initialized button with type {self.button_type}, interface status {self.interface_status}, and rect {self.rect}.")
    
    def update(self, mouse_pos: tuple[int, int], interface_status: global_enums.InterfaceStatus):
        if self.interface_status != interface_status:
            self.state = ButtonState.NORMAL
            self.image = self.button_type.value['normal']
            return

        if self.rect.collidepoint(mouse_pos):
            if self.state != ButtonState.CLICKED:
                self.image = self.button_type.value['hovered']
                self.state = ButtonState.HOVERED
        else:
            if self.state == ButtonState.HOVERED:
                self.image = self.button_type.value['normal']
                self.state = ButtonState.NORMAL

    def draw(self, surface: pygame.Surface):
        if self.interface_status != setting.interface_status and self.only_draw_interface_status != setting.interface_status:
            self.state = ButtonState.NORMAL
            self.image = self.button_type.value['normal']
            return
        
        surface.blit(self.image, self.rect)

    def mouse_click(self, mouse_pos: tuple[int, int], interface_status: global_enums.InterfaceStatus):
        if self.interface_status != interface_status:
            logging.debug(f"Button {self.button_type} click ignored: interface mismatch. Expected {self.interface_status} got {interface_status}")
            return
        
        logging.debug(f"Button {self.button_type} received mouse click at position {mouse_pos} self.state: {self.state}")

        if self.rect.collidepoint(mouse_pos):
            self.image = self.button_type.value['clicked']
            self.state = ButtonState.CLICKED
            logging.debug(f"Button {self.button_type} state changed to CLICKED.")
        else:
            logging.debug(f"Button {self.button_type} click missed: mouse not over button rect {self.rect}")
    
    def mouse_release(self, mouse_pos: tuple[int, int], interface_status: global_enums.InterfaceStatus):
        if self.interface_status != interface_status:
            logging.debug(f"Button {self.button_type} release ignored: interface mismatch. Expected {self.interface_status} got {interface_status}")
            return
        
        logging.debug(f"Button {self.button_type} received mouse release at position {mouse_pos} self.state: {self.state}")

        if self.state == ButtonState.CLICKED:
            self.image = self.button_type.value['normal']
            self.state = ButtonState.NORMAL
            self.draw(setting.screen)

            if self.rect.collidepoint(mouse_pos):
                logging.debug(f"Button {self.button_type} executing command: {self.command}")
                self.command()
            else:
                logging.debug(f"Button {self.button_type} command not executed: mouse moved off button")
            logging.debug(f"Button {self.button_type} state changed to NORMAL.")
        else:
            logging.debug(f"Button {self.button_type} command not executed: state is {self.state}, not CLICKED")

def back_to_lobby():
    setting.set_interface_status(global_enums.InterfaceStatus.LOBBY)

def open_menu():
    setting.set_interface_status(global_enums.InterfaceStatus.LEVEL_SELECTION)

def start_endless_mode():
    pass

def next_level():
    logging.debug("next_level() function called!")
    chessboard_module.chessboard = chessboard_module.Chessboard()
    chessboard_module.chessboard_backup = chessboard_module.chessboard.copy_static_self()
    setting.set_interface_status(global_enums.InterfaceStatus.GAMEPLAY)
    logging.debug(f"New chessboard created, interface status set to: {setting.interface_status}")

def retry_level():
    chessboard_module.chessboard = chessboard_module.chessboard_backup.copy_static_self()
    setting.set_interface_status(global_enums.InterfaceStatus.GAMEPLAY)

buttons: pygame.sprite.Group = pygame.sprite.Group()
buttons.add(
    # Button(ButtonsType.HOME, image_rect.level_select_home_rect, back_to_lobby, global_enums.InterfaceStatus.LEVEL_SELECTION),
    # Button(ButtonsType.HOME, image_rect.level_playing_home_rect, back_to_lobby, global_enums.InterfaceStatus.GAMEPLAY),
    # Button(ButtonsType.HOME, image_rect.level_complete_home_rect, back_to_lobby, global_enums.InterfaceStatus.LEVEL_COMPLETE),
    
    # # forward

    # # backward

    # # retry

    # Button(ButtonsType.OPEN_MENU, image_rect.lobby_open_menu_rect, open_menu, global_enums.InterfaceStatus.LOBBY)

    # endless mode start

    Button(ButtonsType.FORWARD, image_rect.level_playing_next_level_rect, next_level, global_enums.InterfaceStatus.GAMEPLAY, global_enums.InterfaceStatus.LEVEL_COMPLETE),
    Button(ButtonsType.RETRY, image_rect.level_playing_retry_rect2, retry_level, global_enums.InterfaceStatus.GAMEPLAY, global_enums.InterfaceStatus.LEVEL_COMPLETE),

    Button(ButtonsType.FORWARD, image_rect.level_complete_next_level_rect2, next_level, global_enums.InterfaceStatus.LEVEL_COMPLETE)
)   



