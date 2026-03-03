import os
import sys
import pygame

from python.setting.setting import *

snake_images_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'images', 'snake')

snake_head = pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head.png')).convert_alpha(), (64, 64))
snake_body = pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_body.png')).convert_alpha(), (64, 64))
snake_curly_body = pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body.png')).convert_alpha(), (64, 64))
snake_tail = pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail.png')).convert_alpha(), (64, 64))

snake_half_curly_body = pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_half_curly_body.png')).convert_alpha(), (64, 64))
snake_head_only = pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_only.png')).convert_alpha(), (64, 64))

snake_curly_body_head_move_out_process = {
    1:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body-head_move_out_process1.png')).convert_alpha(), (64, 64)),
    2:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body-head_move_out_process2.png')).convert_alpha(), (64, 64)),
    3:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body-head_move_out_process3.png')).convert_alpha(), (64, 64)),
    4:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body-head_move_out_process4.png')).convert_alpha(), (64, 64)),
    5:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body-head_move_out_process5.png')).convert_alpha(), (64, 64)),
    6:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body-head_move_out_process6.png')).convert_alpha(), (64, 64)),
    7:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body-head_move_out_process7.png')).convert_alpha(), (64, 64)),
    8:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body-head_move_out_process8.png')).convert_alpha(), (64, 64)),
    9:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body-head_move_out_process9.png')).convert_alpha(), (64, 64)),
    10: pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body-head_move_out_process10.png')).convert_alpha(), (64, 64)),
    11: pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body-head_move_out_process11.png')).convert_alpha(), (64, 64)),
}

snake_curly_tail_entry_process = {
    1:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body.png')).convert_alpha(), (64, 64)),
    2:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body.png')).convert_alpha(), (64, 64)),
    3:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body.png')).convert_alpha(), (64, 64)),
    4:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_body.png')).convert_alpha(), (64, 64)),
    5:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_tail_entry_process5.png')).convert_alpha(), (64, 64)),
    6:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_tail_entry_process6.png')).convert_alpha(), (64, 64)),
    7:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_tail_entry_process7.png')).convert_alpha(), (64, 64)),
    8:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_tail_entry_process8.png')).convert_alpha(), (64, 64)),
    9:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_tail_entry_process9.png')).convert_alpha(), (64, 64)),
    10: pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_tail_entry_process10.png')).convert_alpha(), (64, 64)),
    11: pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_curly_tail_entry_process11.png')).convert_alpha(), (64, 64)),
}

snake_head_entry_process = {
    1:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_entry_process1.png')).convert_alpha(), (64, 64)),
    2:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_entry_process2.png')).convert_alpha(), (64, 64)),
    3:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_entry_process3.png')).convert_alpha(), (64, 64)),
    4:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_entry_process4.png')).convert_alpha(), (64, 64)),
    5:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_entry_process5.png')).convert_alpha(), (64, 64)),
    6:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_entry_process6.png')).convert_alpha(), (64, 64)),
    7:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_entry_process7.png')).convert_alpha(), (64, 64)),
    8:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_entry_process8.png')).convert_alpha(), (64, 64)),
    9:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_entry_process9.png')).convert_alpha(), (64, 64)),
    10: pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_entry_process10.png')).convert_alpha(), (64, 64)),
    11: pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_entry_process11.png')).convert_alpha(), (64, 64)),
}

snake_head_move_out_process = {
    1:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_move_out_process1.png')).convert_alpha(), (64, 64)),
    2:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_move_out_process2.png')).convert_alpha(), (64, 64)),
    3:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_move_out_process3.png')).convert_alpha(), (64, 64)),
    4:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_move_out_process4.png')).convert_alpha(), (64, 64)),
    5:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_move_out_process5.png')).convert_alpha(), (64, 64)),
    6:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_move_out_process6.png')).convert_alpha(), (64, 64)),
    7:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_move_out_process7.png')).convert_alpha(), (64, 64)),
    8:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_move_out_process8.png')).convert_alpha(), (64, 64)),
    9:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_move_out_process9.png')).convert_alpha(), (64, 64)),
    10: pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_move_out_process10.png')).convert_alpha(), (64, 64)),
    11: pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_head_move_out_process11.png')).convert_alpha(), (64, 64)),
}

snake_tail_entry_process = {
    1:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_body.png')).convert_alpha(), (64, 64)),
    2:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_body.png')).convert_alpha(), (64, 64)),
    3:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_body.png')).convert_alpha(), (64, 64)),
    4:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_body.png')).convert_alpha(), (64, 64)),
    5:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_entry_process5.png')).convert_alpha(), (64, 64)),
    6:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_entry_process6.png')).convert_alpha(), (64, 64)),
    7:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_entry_process7.png')).convert_alpha(), (64, 64)),
    8:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_entry_process8.png')).convert_alpha(), (64, 64)),
    9:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_entry_process9.png')).convert_alpha(), (64, 64)),
    10: pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_entry_process10.png')).convert_alpha(), (64, 64)),
    11: pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_entry_process11.png')).convert_alpha(), (64, 64)),
}

snake_tail_move_out_process = {
    1:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_move_out_process1.png')).convert_alpha(), (64, 64)),
    2:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_move_out_process2.png')).convert_alpha(), (64, 64)),
    3:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_move_out_process3.png')).convert_alpha(), (64, 64)),
    4:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_move_out_process4.png')).convert_alpha(), (64, 64)),
    5:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_move_out_process5.png')).convert_alpha(), (64, 64)),
    6:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_move_out_process6.png')).convert_alpha(), (64, 64)),
    7:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_move_out_process7.png')).convert_alpha(), (64, 64)),
    8:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_move_out_process8.png')).convert_alpha(), (64, 64)),
    9:  pygame.transform.smoothscale(pygame.image.load(os.path.join(snake_images_path, 'snake_tail_move_out_process9.png')).convert_alpha(), (64, 64)),
    10: pygame.Surface((0, 0)).convert_alpha(),
    11: pygame.Surface((0, 0)).convert_alpha(),
}

