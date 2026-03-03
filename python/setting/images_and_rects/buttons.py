import os
import sys
import pygame

from python.setting.setting import *

buttons_images_path = os.path.join(os.path.dirname(__file__), '..', '..', '..', 'images', 'buttons')

home_images = {
    'normal':   pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'home_button_normal.png'))  .convert_alpha(), (SCREEN_HEIGHT/10, SCREEN_HEIGHT/10)),
    'hovered':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'home_button_hovered.png')) .convert_alpha(), (SCREEN_HEIGHT/10, SCREEN_HEIGHT/10)),
    'clicked':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'home_button_clicked.png')) .convert_alpha(), (SCREEN_HEIGHT/10, SCREEN_HEIGHT/10))
}
level_select_home_rect = home_images['normal'].get_rect(topleft = (SCREEN_WIDTH/35*2, SCREEN_WIDTH/10))
level_playing_home_rect = home_images['normal'].get_rect(topleft = ((SCREEN_WIDTH-SCREEN_HEIGHT/10*3 - SCREEN_HEIGHT/7*5)/2, SCREEN_HEIGHT / 7))
level_complete_home_rect = home_images['normal'].get_rect(bottomright = (SCREEN_WIDTH/2-SCREEN_HEIGHT/40, SCREEN_HEIGHT/5*4))

# back_images = {
#     'normal':   pygame.image.load(os.path.join(buttons_images_path, 'back_button_normal.png'))  .convert_alpha(),
#     'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'back_button_hovered.png')) .convert_alpha(),
#     'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'back_button_clicked.png')) .convert_alpha()
# }

forward_images = {
    'normal':   pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'forward_button_normal.png'))  .convert_alpha(), (SCREEN_HEIGHT/10, SCREEN_HEIGHT/10)),
    'hovered':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'forward_button_hovered.png')) .convert_alpha(), (SCREEN_HEIGHT/10, SCREEN_HEIGHT/10)),
    'clicked':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'forward_button_clicked.png')) .convert_alpha(), (SCREEN_HEIGHT/10, SCREEN_HEIGHT/10))
}
level_select_forward_rect = forward_images['normal'].get_rect(right = SCREEN_WIDTH/35*33, centery = SCREEN_HEIGHT/2)
level_playing_forward_rect = forward_images['normal'].get_rect(bottomleft = ((SCREEN_WIDTH-SCREEN_HEIGHT/10*3 - SCREEN_HEIGHT/7*5)/2 + SCREEN_HEIGHT/10*1.5, SCREEN_HEIGHT / 7*6))
level_complete_next_level_rect = forward_images['normal'].get_rect(bottomleft = (SCREEN_WIDTH/2+SCREEN_HEIGHT/40, SCREEN_HEIGHT/5*4))
level_complete_next_level_rect2 = forward_images['normal'].get_rect(centerx = SCREEN_WIDTH/2, bottom = SCREEN_HEIGHT/5*4)

backward_images = {
    'normal':   pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'backward_button_normal.png'))  .convert_alpha(), (SCREEN_HEIGHT/10, SCREEN_HEIGHT/10)),
    'hovered':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'backward_button_hovered.png')) .convert_alpha(), (SCREEN_HEIGHT/10, SCREEN_HEIGHT/10)),
    'clicked':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'backward_button_clicked.png')) .convert_alpha(), (SCREEN_HEIGHT/10, SCREEN_HEIGHT/10))
}
level_select_backward_rect = backward_images['normal'].get_rect(left = SCREEN_WIDTH/10, centery = SCREEN_HEIGHT/2)
level_playing_backward_rect = backward_images['normal'].get_rect(bottomleft = ((SCREEN_WIDTH-SCREEN_HEIGHT/10*3 - SCREEN_HEIGHT/7*5)/2, SCREEN_HEIGHT / 7*6))

# circle_setting_images = {
#     'normal':   pygame.image.load(os.path.join(buttons_images_path, 'circle_setting_button_normal.png'))  .convert_alpha(),
#     'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'circle_setting_button_hovered.png')) .convert_alpha(),
#     'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'circle_setting_button_clicked.png')) .convert_alpha()
# }

# square_setting_images = {
#     'normal':   pygame.image.load(os.path.join(buttons_images_path, 'square_setting_button_normal.png'))  .convert_alpha(),
#     'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'square_setting_button_hovered.png')) .convert_alpha(),
#     'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'square_setting_button_clicked.png')) .convert_alpha()
# }

retry_images = {
    'normal':   pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'retry_button_normal.png'))  .convert_alpha(), (SCREEN_HEIGHT/10, SCREEN_HEIGHT/10)),
    'hovered':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'retry_button_hovered.png')) .convert_alpha(), (SCREEN_HEIGHT/10, SCREEN_HEIGHT/10)),
    'clicked':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'retry_button_clicked.png')) .convert_alpha(), (SCREEN_HEIGHT/10, SCREEN_HEIGHT/10))
}
level_playing_retry_rect = retry_images['normal'].get_rect(topleft = ((SCREEN_WIDTH-SCREEN_HEIGHT/10*3 - SCREEN_HEIGHT/7*5)/2 + SCREEN_HEIGHT/10*1.5, SCREEN_HEIGHT / 7))

open_menu_images = {
    'normal':   pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'open_menu_button_normal.png'))  .convert_alpha(), (SCREEN_HEIGHT/5, SCREEN_HEIGHT/5)),
    'hovered':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'open_menu_button_hovered.png')) .convert_alpha(), (SCREEN_HEIGHT/5, SCREEN_HEIGHT/5)),
    'clicked':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'open_menu_button_clicked.png')) .convert_alpha(), (SCREEN_HEIGHT/5, SCREEN_HEIGHT/5))
}
lobby_open_menu_rect = open_menu_images['normal'].get_rect(bottomleft = (SCREEN_WIDTH/2-SCREEN_HEIGHT/15*17/2, SCREEN_HEIGHT/30*27))

endless_mode_start_images = {
    'normal':   pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'endless_mode_start_button_normal.png'))  .convert_alpha(), (SCREEN_HEIGHT/5, SCREEN_HEIGHT/5)),
    'hovered':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'endless_mode_start_button_hovered.png')) .convert_alpha(), (SCREEN_HEIGHT/5, SCREEN_HEIGHT/5)),
    'clicked':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'endless_mode_start_button_clicked.png')) .convert_alpha(), (SCREEN_HEIGHT/5, SCREEN_HEIGHT/5))
}
lobby_endless_mode_start_rect = endless_mode_start_images['normal'].get_rect(bottomright = (SCREEN_HEIGHT/2+SCREEN_HEIGHT/15*17/2, SCREEN_HEIGHT/30*27))

orig_circle_button_images = {
    'normal':   pygame.image.load(os.path.join(buttons_images_path, 'circle_button_normal.png'))    .convert_alpha(),
    'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'circle_button_hovered.png'))   .convert_alpha(),
    'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'circle_button_clicked.png'))   .convert_alpha()
}

orig_square_button_images = {
    'normal':   pygame.image.load(os.path.join(buttons_images_path, 'square_button_normal.png'))    .convert_alpha(),
    'hovered':  pygame.image.load(os.path.join(buttons_images_path, 'square_button_hovered.png'))   .convert_alpha(),
    'clicked':  pygame.image.load(os.path.join(buttons_images_path, 'square_button_clicked.png'))   .convert_alpha()
}

level_button_template_images = {
    'normal':   pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'square_button_normal.png'))  .convert_alpha(), (SCREEN_HEIGHT/6, SCREEN_HEIGHT/6)),
    'hovered':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'square_button_hovered.png')) .convert_alpha(), (SCREEN_HEIGHT/6, SCREEN_HEIGHT/6)),
    'clicked':  pygame.transform.smoothscale(pygame.image.load(os.path.join(buttons_images_path, 'square_button_clicked.png')) .convert_alpha(), (SCREEN_HEIGHT/6, SCREEN_HEIGHT/6))
}
level_button_rects = (
    level_button_template_images['normal'].get_rect(centerx = SCREEN_WIDTH/35*8.5, top = SCREEN_HEIGHT/10),
    level_button_template_images['normal'].get_rect(centerx = SCREEN_WIDTH/35*14.5, top = SCREEN_HEIGHT/10),
    level_button_template_images['normal'].get_rect(centerx = SCREEN_WIDTH/35*20.5, top = SCREEN_HEIGHT/10),
    level_button_template_images['normal'].get_rect(centerx = SCREEN_WIDTH/35*26.5, top = SCREEN_HEIGHT/10),

    level_button_template_images['normal'].get_rect(centerx = SCREEN_WIDTH/35*8.5, centery = SCREEN_HEIGHT/2),
    level_button_template_images['normal'].get_rect(centerx = SCREEN_WIDTH/35*14.5, centery = SCREEN_HEIGHT/2),
    level_button_template_images['normal'].get_rect(centerx = SCREEN_WIDTH/35*20.5, centery = SCREEN_HEIGHT/2),
    level_button_template_images['normal'].get_rect(centerx = SCREEN_WIDTH/35*26.5, centery = SCREEN_HEIGHT/2),

    level_button_template_images['normal'].get_rect(centerx = SCREEN_WIDTH/35*8.5, bottom = SCREEN_HEIGHT/10*9),
    level_button_template_images['normal'].get_rect(centerx = SCREEN_WIDTH/35*14.5, bottom = SCREEN_HEIGHT/10*9),
    level_button_template_images['normal'].get_rect(centerx = SCREEN_WIDTH/35*20.5, bottom = SCREEN_HEIGHT/10*9),
    level_button_template_images['normal'].get_rect(centerx = SCREEN_WIDTH/35*26.5, bottom = SCREEN_HEIGHT/10*9),
)

