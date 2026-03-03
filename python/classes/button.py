import pygame
import logging
from enum import Enum
from typing import Callable

from python.setting.setting import *
import python.setting.images_and_rects.buttons as image_rect
import python.setting.global_enums as global_enums
from python.classes.chessboard import chessboard, Chessboard

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
        if self.button_type == ButtonsType.LEVEL:
            self.level_button_num = level_button_num
        
        logging.debug(f"Initialized button with type {self.button_type}, interface status {self.interface_status}, and rect {self.rect}.")
    
    def update(self, mouse_pos: tuple[int, int], interface_status: global_enums.InterfaceStatus):
        if self.interface_status != interface_status:
            return

        if self.rect.collidepoint(mouse_pos):
            self.image = self.button_type.value['hovered']
            self.state = ButtonState.HOVERED
        else:
            if self.state == ButtonState.HOVERED:
                self.image = self.button_type.value['normal']
                self.state = ButtonState.NORMAL

    def draw(self, surface: pygame.Surface):
        if self.interface_status != interface_status:
            return
        
        surface.blit(self.image, self.rect)

    def mouse_click(self, mouse_pos: tuple[int, int], interface_status: global_enums.InterfaceStatus):
        if self.interface_status != interface_status:
            return
        
        if self.rect.collidepoint(mouse_pos):
            self.image = self.button_type.value['clicked']
            self.state = ButtonState.CLICKED
    
    def mouse_release(self, mouse_pos: tuple[int, int], interface_status: global_enums.InterfaceStatus):
        if self.interface_status != interface_status:
            return
        
        if self.state == ButtonState.CLICKED:
            if self.rect.collidepoint(mouse_pos):
                return self.command()
            self.image = self.button_type.value['hovered']
            self.state = ButtonState.HOVERED

def back_to_lobby():
    global interface_status
    interface_status = global_enums.InterfaceStatus.LOBBY

def open_menu():
    global interface_status
    interface_status = global_enums.InterfaceStatus.LEVEL_SELECTION

def start_endless_mode():
    pass

def next_level():
    global chessboard, interface_status
    chessboard = Chessboard()
    interface_status = global_enums.InterfaceStatus.GAMEPLAY

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

    Button(ButtonsType.FORWARD, image_rect.level_complete_next_level_rect2, next_level, global_enums.InterfaceStatus.LEVEL_COMPLETE)
)   


