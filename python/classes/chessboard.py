import pygame
import random
import logging
from collections import deque
from enum import Enum

from python.setting import global_enums
from python.setting.setting import *
from python.setting.global_enums import Colors
from python.setting.images_and_rects.boxes import images as box_images
from python.setting.images_and_rects.checkpoints import images as checkpoint_images
from python.setting.images_and_rects.end_points import images as end_point_images
from python.setting.images_and_rects.portals import images as portal_images
import python.setting.images_and_rects.snake as snake_images
from python.setting.images_and_rects.others import red_apple_image

class Chessboard:
    class Direction(Enum):
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3

    class BlockTypes(Enum):
        BLANK = 0
        UNMOVEABLE = 1
        NONE = -1
        UP_SNAKE_HEAD = 2
        DOWN_SNAKE_HEAD = 3
        LEFT_SNAKE_HEAD = 4
        RIGHT_SNAKE_HEAD = 5
        BOX = 6
        CHECKPOINT = 7
        END_POINT = 8
        PORTAL = 9
        SNAKE_BODY = 10
        SNAKE_TAIL = 11
        SNAKE_CURLY_BODY = 12
        APPLE = 13

    class Block:
        def __init__(self, image: pygame.Surface, x: int, y: int, block_type: 'Chessboard.BlockTypes', rotate: int = 0, color: Colors | None = None):
            self.image = image
            self.rect = self.image.get_rect(center = (x*64 + 32, y*64 + 32))
            self.pos = (x, y)
            self.block_type = block_type
            self.rotate = rotate
            self.color = color

    def __init__(self):
        self.image = pygame.Surface((640, 640))
        self.rect = self.image.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
        self.moving = False
        self.moving_box: None | Chessboard.Block = None
        self.moving_direction: None | Chessboard.Direction = None
        self.moving_process: None | int = 1 # 1~12 normal, -5~0 head turn
        self.snake_tail_move: bool = True
        self.snake_move_trun = False
        self.eat_apple: None | Chessboard.Block = None

        self.__random_gen_map()
        self.draw_chessboard()
    
    def __random_gen_map(self):
        self.map: list[list[Chessboard.Block]] = [[self.Block(pygame.Surface((0,0)), x, y, self.BlockTypes.BLANK) for y in range(10)] for x in range(10)]
        self.snake_body: list[Chessboard.Block] = []
        self.checkpoints: dict[Colors, list[Chessboard.Block]] = {}

        self.map[7][3] = self.Block(pygame.transform.rotate(snake_images.snake_tail, -90), 7, 3, self.BlockTypes.SNAKE_TAIL, 270)
        self.snake_body.append(self.map[7][3])
        self.map[7][4] = self.Block(pygame.transform.rotate(snake_images.snake_body, -90), 7, 4, self.BlockTypes.SNAKE_BODY, 270)
        self.snake_body.append(self.map[7][4])
        self.map[7][5] = self.Block(pygame.transform.rotate(snake_images.snake_body, -90), 7, 5, self.BlockTypes.SNAKE_BODY, 270)
        self.snake_body.append(self.map[7][5])
        self.map[7][6] = self.Block(pygame.transform.rotate(snake_images.snake_head, -90), 7, 6, self.BlockTypes.DOWN_SNAKE_HEAD, 270)
        self.snake_body.append(self.map[7][6])

        for _ in range(4): # unmoveable boxes
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.map[x][y].block_type != self.BlockTypes.BLANK:
                continue
            if (x > 0 and y > 0 and self.map[x-1][y-1].block_type == self.BlockTypes.UNMOVEABLE) or \
                (x > 0 and self.map[x-1][y].block_type == self.BlockTypes.UNMOVEABLE) or \
                (x > 0 and y < 9 and self.map[x-1][y+1].block_type == self.BlockTypes.UNMOVEABLE) or \
                (y > 0 and self.map[x][y-1].block_type == self.BlockTypes.UNMOVEABLE) or \
                (y < 9 and self.map[x][y+1].block_type == self.BlockTypes.UNMOVEABLE) or \
                (x < 9 and y > 0 and self.map[x+1][y-1].block_type == self.BlockTypes.UNMOVEABLE) or \
                (x < 9 and self.map[x+1][y].block_type == self.BlockTypes.UNMOVEABLE) or \
                (x < 9 and y < 9 and self.map[x+1][y+1].block_type == self.BlockTypes.UNMOVEABLE) \
            :
                continue
            self.map[x][y] = self.Block(box_images[Colors.SILVER_GELATIN], x, y, self.BlockTypes.UNMOVEABLE)

        for _ in range(15): # apple
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.map[x][y].block_type != self.BlockTypes.BLANK:
                continue
            self.map[x][y] = self.Block(red_apple_image, x, y, self.BlockTypes.APPLE)

        for _ in range(3): # moveable boxes and checkpoints
            color = random.choice(list(Colors))
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.map[x][y].block_type != self.BlockTypes.BLANK:
                continue
            if color not in box_images:
                continue
            self.map[x][y] = self.Block(box_images[color], x, y, self.BlockTypes.BOX, color = color)
            self.checkpoints[color] = []

            for _ in range(2):
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if self.map[x][y].block_type != self.BlockTypes.BLANK:
                    continue
                if color not in checkpoint_images:
                    continue
                self.map[x][y] = self.Block(checkpoint_images[color], x, y, self.BlockTypes.CHECKPOINT, color = color)
                self.checkpoints[color].append(self.map[x][y])
            
            x = random.randint(0, 9)
            y = random.randint(0, 9)
            if self.map[x][y].block_type != self.BlockTypes.BLANK:
                continue
            if color not in end_point_images:
                continue
            self.map[x][y] = self.Block(end_point_images[color], x, y, self.BlockTypes.END_POINT, color = color)
            self.checkpoints[color].append(self.map[x][y])

    def draw_chessboard(self):
        self.image.fill(("#036300"))
        for x in range(0, 577, 128):
            for y in range(0, 577, 128):
                pygame.draw.rect(self.image, ("#3df037"), (x, y, 64, 64))
            for y in range(64, 577, 128):
                pygame.draw.rect(self.image, ("#3df037"), (x+64, y, 64, 64))
        
        for checkpoint_list in self.checkpoints.values():
            for checkpoint in checkpoint_list:
                self.image.blit(checkpoint.image, checkpoint.rect)

        if self.eat_apple != None:
                    self.image.blit(self.eat_apple.image, self.eat_apple.rect)

        # logging.debug("\nmap:")
        for row in self.map:
            for block in row:
                self.image.blit(block.image, block.rect)
                # if block.block_type != self.BlockTypes.BLANK:
                    # logging.debug(f"block pos: {block.pos}, type: {block.block_type}, rotate: {block.rotate}, equal snake: {block.image in {snake_images.snake_body, snake_images.snake_curly_body, snake_images.snake_head, snake_images.snake_tail}}")
        # logging.debug("")
        self.__log_snake_body()

        if self.moving_box != None:
            self.image.blit(self.moving_box.image, self.moving_box.rect)
        
    def update(self):
        if self.moving:
            self.moving_process += 1

            head = self.snake_body[-1]

            match self.moving_direction:
                case self.Direction.UP:
                    direct = 90
                    flip = False
                    angle = 90
                    if head.block_type == self.BlockTypes.LEFT_SNAKE_HEAD:
                        angle = 270
                        flip = False
                    elif head.block_type == self.BlockTypes.RIGHT_SNAKE_HEAD:
                        angle = 270
                        flip = True
                case self.Direction.DOWN:
                    direct = 270
                    flip = False
                    angle = 270
                    if head.block_type == self.BlockTypes.LEFT_SNAKE_HEAD:
                        angle = 90
                        flip = True
                    elif head.block_type == self.BlockTypes.RIGHT_SNAKE_HEAD:
                        angle = 90
                        flip = False
                case self.Direction.LEFT:
                    direct = 180
                    flip = False
                    angle = 180
                    if head.block_type == self.BlockTypes.UP_SNAKE_HEAD:
                        angle = 0
                        flip = True
                    elif head.block_type == self.BlockTypes.DOWN_SNAKE_HEAD:
                        angle = 0
                        flip = False
                case self.Direction.RIGHT:
                    direct = 0
                    flip = False
                    angle = 0
                    if head.block_type == self.BlockTypes.UP_SNAKE_HEAD:
                        angle = 180
                        flip = False
                    elif head.block_type == self.BlockTypes.DOWN_SNAKE_HEAD:
                        angle = 180
                        flip = True

            if self.moving_process == 1:
                match self.moving_direction:
                    case self.Direction.UP:
                        self.map[head.pos[0]][head.pos[1]-1] = self.Block(pygame.transform.rotate(snake_images.snake_head_entry_process[1], direct), head.pos[0], head.pos[1]-1, self.BlockTypes.UP_SNAKE_HEAD, direct)
                        self.snake_body.append(self.map[head.pos[0]][head.pos[1]-1])
                    case self.Direction.DOWN:
                        self.map[head.pos[0]][head.pos[1]+1] = self.Block(pygame.transform.rotate(snake_images.snake_head_entry_process[1], direct), head.pos[0], head.pos[1]+1, self.BlockTypes.DOWN_SNAKE_HEAD, direct)
                        self.snake_body.append(self.map[head.pos[0]][head.pos[1]+1])
                    case self.Direction.LEFT:
                        self.map[head.pos[0]-1][head.pos[1]] = self.Block(pygame.transform.rotate(snake_images.snake_head_entry_process[1], direct), head.pos[0]-1, head.pos[1], self.BlockTypes.LEFT_SNAKE_HEAD, direct)
                        self.snake_body.append(self.map[head.pos[0]-1][head.pos[1]])
                    case self.Direction.RIGHT:
                        self.map[head.pos[0]+1][head.pos[1]] = self.Block(pygame.transform.rotate(snake_images.snake_head_entry_process[1], direct), head.pos[0]+1, head.pos[1], self.BlockTypes.RIGHT_SNAKE_HEAD, direct)
                        self.snake_body.append(self.map[head.pos[0]+1][head.pos[1]])

            head = self.snake_body[-1]
            second_head = self.snake_body[-2]
            third_head = self.snake_body[-3]
            tail = self.snake_body[0]
            second_tail = self.snake_body[1]
            rotate = 15 * (self.moving_process + 5) 
            second_head_rotate = second_head.rotate
            if second_head_rotate == 0: second_head_rotate = 360
            if second_head.rotate - direct == 90:
                rotate = direct + 90 - rotate
            else:
                rotate = direct - 90 + rotate

            # logging.debug(f"rotate: {rotate}, moving_process: {self.moving_process}, angle: {angle}, direct: {direct}, flip: {flip}")

            if self.moving_process <= 0:
                self.moving_process = 0
                
                # if flip:
                #     head.image = pygame.transform.flip(snake_images.snake_half_curly_body, False, True)
                #     head.image = pygame.transform.rotate(head.image, head.rotate)
                # else:
                #     head.image = pygame.transform.rotate(snake_images.snake_half_curly_body, head.rotate)
                # head.image.blit(pygame.transform.rotate(snake_images.snake_head_only, rotate), pygame.Rect(0, 0, 64, 64))
                # logging.debug(f"head image: {head.image}")
                
            elif self.moving_process <= 11:
                head.image = pygame.transform.rotate(snake_images.snake_head_entry_process[self.moving_process], direct)
                if self.snake_move_trun:
                    previous_block_rotate = third_head.rotate 
                    if previous_block_rotate == 0: previous_block_rotate = 360
                    if previous_block_rotate-direct == 90:
                        second_head.image = pygame.transform.rotate(pygame.transform.flip(snake_images.snake_curly_body_head_move_out_process[self.moving_process], False, True), direct-270)
                    else:
                        second_head.image = pygame.transform.rotate(snake_images.snake_curly_body_head_move_out_process[self.moving_process], direct-90)
                else:
                    second_head.image = pygame.transform.rotate(snake_images.snake_head_move_out_process[self.moving_process], direct)
                
                if self.eat_apple == None:
                    tail.image = pygame.transform.rotate(snake_images.snake_tail_move_out_process[self.moving_process], tail.rotate)
                    if second_tail.rotate == tail.rotate:
                        second_tail.image = pygame.transform.rotate(snake_images.snake_tail_entry_process[self.moving_process], second_tail.rotate)
                    else:
                        previous_block_rotate = tail.rotate 
                        if previous_block_rotate == 0: previous_block_rotate = 360
                        if previous_block_rotate-second_tail.rotate == 90:
                            second_tail.image = pygame.transform.rotate(pygame.transform.flip(snake_images.snake_curly_tail_entry_process[self.moving_process], False, True), second_tail.rotate-270)
                        else:
                            second_tail.image = pygame.transform.rotate(snake_images.snake_curly_tail_entry_process[self.moving_process], second_tail.rotate-90)
                    # if second_tail.block_type == self.BlockTypes.SNAKE_CURLY_BODY:
                    #     second_tail.image = pygame.transform.rotate(snake_images.snake_curly_tail_entry_process[self.moving_process], second_tail.rotate)
                    # else:
                    #     second_tail.image = pygame.transform.rotate(snake_images.snake_tail_entry_process[self.moving_process], second_tail.rotate)

                if self.moving_box != None:
                    if self.moving_direction == self.Direction.UP:
                        self.moving_box.rect.y -= 64 / 12
                    elif self.moving_direction == self.Direction.DOWN:
                        self.moving_box.rect.y += 64 / 12
                    elif self.moving_direction == self.Direction.LEFT:
                        self.moving_box.rect.x -= 64 / 12
                    elif self.moving_direction == self.Direction.RIGHT:
                        self.moving_box.rect.x += 64 / 12

            else: # 12
                if self.moving_box != None:
                    self.moving_box.rect = self.moving_box.image.get_rect(center = (self.moving_box.pos[0]*64 + 32, self.moving_box.pos[1]*64 + 32))
                    self.map[self.moving_box.pos[0]][self.moving_box.pos[1]] = self.moving_box
                    for checkpoint in self.checkpoints[self.moving_box.color]:
                        if checkpoint.block_type == self.BlockTypes.END_POINT and len(self.checkpoints[self.moving_box.color]) > 1:
                            logging.debug(f"len checkpoints: {len(self.checkpoints[self.moving_box.color])}")
                            break
                        if checkpoint.pos == self.moving_box.pos:
                            self.checkpoints[self.moving_box.color].remove(checkpoint)
                            if len(self.checkpoints[self.moving_box.color]) == 0:
                                self.moving_box.image = box_images[Colors.SILVER_GELATIN]
                                self.moving_box.block_type = self.BlockTypes.UNMOVEABLE
                                self.moving_box.color = None
                            break
                if self.snake_tail_move:
                    self.map[tail.pos[0]][tail.pos[1]] = self.Block(pygame.Surface((0,0)), tail.pos[0], tail.pos[1], self.BlockTypes.BLANK)
                    self.snake_body.pop(0)
                
                if self.snake_body[-1].rotate == self.snake_body[-2].rotate:
                    self.snake_body[-2].block_type = self.BlockTypes.SNAKE_BODY
                else:
                    self.snake_body[-2].block_type = self.BlockTypes.SNAKE_CURLY_BODY

                for block in self.snake_body:
                    if block.block_type in (self.BlockTypes.UP_SNAKE_HEAD, self.BlockTypes.DOWN_SNAKE_HEAD, self.BlockTypes.LEFT_SNAKE_HEAD, self.BlockTypes.RIGHT_SNAKE_HEAD):
                        block.block_type = self.BlockTypes.SNAKE_BODY
                match self.moving_direction:
                    case self.Direction.UP:
                        head.block_type = self.BlockTypes.UP_SNAKE_HEAD
                    case self.Direction.DOWN:
                        head.block_type = self.BlockTypes.DOWN_SNAKE_HEAD
                    case self.Direction.LEFT:
                        head.block_type = self.BlockTypes.LEFT_SNAKE_HEAD
                    case self.Direction.RIGHT:
                        head.block_type = self.BlockTypes.RIGHT_SNAKE_HEAD

                self.snake_body[-2].rotate = self.snake_body[-1].rotate
                self.snake_body[0].block_type = self.BlockTypes.SNAKE_TAIL

                for i in range(len(self.snake_body)-1):
                    block = self.snake_body[i]
                    match block.block_type:
                        case self.BlockTypes.UP_SNAKE_HEAD:
                            block.image = pygame.transform.rotate(snake_images.snake_head, 90)
                        case self.BlockTypes.DOWN_SNAKE_HEAD:
                            block.image = pygame.transform.rotate(snake_images.snake_head, 270)
                        case self.BlockTypes.LEFT_SNAKE_HEAD:
                            block.image = pygame.transform.rotate(snake_images.snake_head, 180)
                        case self.BlockTypes.RIGHT_SNAKE_HEAD:
                            block.image = snake_images.snake_head
                        case self.BlockTypes.SNAKE_BODY:
                            block.image = pygame.transform.rotate(snake_images.snake_body, block.rotate)
                        case self.BlockTypes.SNAKE_CURLY_BODY:
                            previous_block_rotate = self.snake_body[i-1].rotate # the idx 0 can never be curly body, so i-1 is always valid
                            if previous_block_rotate == 0: previous_block_rotate = 360
                            if previous_block_rotate-block.rotate == 90:
                                block.image = pygame.transform.rotate(pygame.transform.flip(snake_images.snake_curly_body, False, True), block.rotate-270)
                            else:
                                block.image = pygame.transform.rotate(snake_images.snake_curly_body, block.rotate-90)
                        case self.BlockTypes.SNAKE_TAIL:
                            block.image = pygame.transform.rotate(snake_images.snake_tail, block.rotate)

                self.__log_snake_body()

                self.moving_process = None
                self.moving = False
                self.moving_box = None
                self.moving_direction = None
                self.snake_tail_move = True
                self.snake_move_trun = False
                self.eat_apple = None

        for key, value in list(self.checkpoints.items()):
            if len(value) == 0:
                self.checkpoints.pop(key)
        
        self.draw_chessboard()

        if len(self.checkpoints) == 0:
            global interface_status
            interface_status = global_enums.InterfaceStatus.LEVEL_COMPLETE
    
    def key_press(self, key: int):
        if not self.moving:
            match key:
                case pygame.K_UP | pygame.K_w:
                    if self.snake_body[-1].pos[1] == 0:
                        return
                    if self.snake_body[-1].block_type == self.BlockTypes.DOWN_SNAKE_HEAD:
                        return
                    if self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]-1].block_type == self.BlockTypes.UNMOVEABLE:
                        return
                    if self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]-1].block_type == self.BlockTypes.APPLE:
                        self.snake_tail_move = False
                        self.eat_apple = self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]-1]
                        self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]-1] = self.Block(pygame.Surface((0,0)), self.snake_body[-1].pos[0], self.snake_body[-1].pos[1]-1, self.BlockTypes.BLANK)
                    if self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]-1].block_type == self.BlockTypes.BOX:
                        if self.snake_body[-1].pos[1] == 1:
                            return
                        if self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]-2].block_type not in [self.BlockTypes.BLANK, self.BlockTypes.CHECKPOINT, self.BlockTypes.END_POINT]:
                            return
                        self.moving_box = self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]-1]
                        self.moving_box.pos = (self.moving_box.pos[0], self.moving_box.pos[1]-1)
                        self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]-1] = self.Block(pygame.Surface((0,0)), self.snake_body[-1].pos[0], self.snake_body[-1].pos[1]-1, self.BlockTypes.BLANK)
                    
                    want_head = self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]-1]
                    if want_head.block_type not in [self.BlockTypes.BLANK, self.BlockTypes.APPLE, self.BlockTypes.BOX, self.BlockTypes.CHECKPOINT, self.BlockTypes.END_POINT]:
                        return

                    self.moving = True
                    self.moving_direction = self.Direction.UP

                    self.moving_process = 0
                    if self.snake_body[-1].block_type != self.BlockTypes.UP_SNAKE_HEAD:
                        self.moving_process = -6
                        self.snake_move_trun = True

                case pygame.K_DOWN | pygame.K_s:
                    if self.snake_body[-1].pos[1] == len(self.map[0]) - 1:
                        return
                    if self.snake_body[-1].block_type == self.BlockTypes.UP_SNAKE_HEAD:
                        return
                    if self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]+1].block_type == self.BlockTypes.UNMOVEABLE:
                        return
                    if self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]+1].block_type == self.BlockTypes.APPLE:
                        self.snake_tail_move = False
                        self.eat_apple = self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]+1]
                        self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]+1] = self.Block(pygame.Surface((0,0)), self.snake_body[-1].pos[0], self.snake_body[-1].pos[1]+1, self.BlockTypes.BLANK)
                    if self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]+1].block_type == self.BlockTypes.BOX:
                        if self.snake_body[-1].pos[1] == len(self.map[0]) - 2:
                            return
                        if self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]+2].block_type not in [self.BlockTypes.BLANK, self.BlockTypes.CHECKPOINT, self.BlockTypes.END_POINT]:
                            return
                        self.moving_box = self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]+1]
                        self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]+1] = self.Block(pygame.Surface((0,0)), self.snake_body[-1].pos[0], self.snake_body[-1].pos[1]+1, self.BlockTypes.BLANK)
                        self.moving_box.pos = (self.moving_box.pos[0], self.moving_box.pos[1]+1)
                    
                    want_head = self.map[self.snake_body[-1].pos[0]][self.snake_body[-1].pos[1]+1]
                    if want_head.block_type not in [self.BlockTypes.BLANK, self.BlockTypes.APPLE, self.BlockTypes.BOX, self.BlockTypes.CHECKPOINT, self.BlockTypes.END_POINT]:
                        return

                    self.moving = True
                    self.moving_direction = self.Direction.DOWN

                    self.moving_process = 0
                    if self.snake_body[-1].block_type != self.BlockTypes.DOWN_SNAKE_HEAD:
                        self.moving_process = -6
                        self.snake_move_trun = True
                    
                case pygame.K_LEFT | pygame.K_a:
                    if self.snake_body[-1].pos[0] == 0:
                        return
                    if self.snake_body[-1].block_type == self.BlockTypes.RIGHT_SNAKE_HEAD:
                        return
                    if self.map[self.snake_body[-1].pos[0]-1][self.snake_body[-1].pos[1]].block_type == self.BlockTypes.UNMOVEABLE:
                        return
                    if self.map[self.snake_body[-1].pos[0]-1][self.snake_body[-1].pos[1]].block_type == self.BlockTypes.APPLE:
                        self.snake_tail_move = False
                        self.eat_apple = self.map[self.snake_body[-1].pos[0]-1][self.snake_body[-1].pos[1]]
                        self.map[self.snake_body[-1].pos[0]-1][self.snake_body[-1].pos[1]] = self.Block(pygame.Surface((0,0)), self.snake_body[-1].pos[0]-1, self.snake_body[-1].pos[1], self.BlockTypes.BLANK)
                    if self.map[self.snake_body[-1].pos[0]-1][self.snake_body[-1].pos[1]].block_type == self.BlockTypes.BOX:
                        if self.snake_body[-1].pos[0] == 1:
                            return
                        if self.map[self.snake_body[-1].pos[0]-2][self.snake_body[-1].pos[1]].block_type not in [self.BlockTypes.BLANK, self.BlockTypes.CHECKPOINT, self.BlockTypes.END_POINT]:
                            return
                        self.moving_box = self.map[self.snake_body[-1].pos[0]-1][self.snake_body[-1].pos[1]]
                        self.moving_box.pos = (self.moving_box.pos[0]-1, self.moving_box.pos[1])
                        self.map[self.snake_body[-1].pos[0]-1][self.snake_body[-1].pos[1]] = self.Block(pygame.Surface((0,0)), self.snake_body[-1].pos[0]-1, self.snake_body[-1].pos[1], self.BlockTypes.BLANK)

                        want_head = self.map[self.snake_body[-1].pos[0]-1][self.snake_body[-1].pos[1]]
                        if want_head.block_type not in [self.BlockTypes.BLANK, self.BlockTypes.APPLE, self.BlockTypes.BOX, self.BlockTypes.CHECKPOINT, self.BlockTypes.END_POINT]:
                            return

                    self.moving = True
                    self.moving_direction = self.Direction.LEFT

                    self.moving_process = 0
                    if self.snake_body[-1].block_type != self.BlockTypes.LEFT_SNAKE_HEAD:
                        self.moving_process = -6
                        self.snake_move_trun = True

                case pygame.K_RIGHT | pygame.K_d:
                    if self.snake_body[-1].pos[0] == len(self.map) - 1:
                        return
                    if self.snake_body[-1].block_type == self.BlockTypes.LEFT_SNAKE_HEAD:
                        return
                    if self.map[self.snake_body[-1].pos[0]+1][self.snake_body[-1].pos[1]].block_type == self.BlockTypes.UNMOVEABLE:
                        return
                    if self.map[self.snake_body[-1].pos[0]+1][self.snake_body[-1].pos[1]].block_type == self.BlockTypes.APPLE:
                        self.snake_tail_move = False
                        self.eat_apple = self.map[self.snake_body[-1].pos[0]+1][self.snake_body[-1].pos[1]]
                        self.map[self.snake_body[-1].pos[0]+1][self.snake_body[-1].pos[1]] = self.Block(pygame.Surface((0,0)), self.snake_body[-1].pos[0]+1, self.snake_body[-1].pos[1], self.BlockTypes.BLANK)
                    if self.map[self.snake_body[-1].pos[0]+1][self.snake_body[-1].pos[1]].block_type == self.BlockTypes.BOX:
                        if self.snake_body[-1].pos[0] == len(self.map) - 2:
                            return
                        if self.map[self.snake_body[-1].pos[0]+2][self.snake_body[-1].pos[1]].block_type not in [self.BlockTypes.BLANK, self.BlockTypes.CHECKPOINT, self.BlockTypes.END_POINT]:
                            return
                        self.moving_box = self.map[self.snake_body[-1].pos[0]+1][self.snake_body[-1].pos[1]]
                        self.moving_box.pos = (self.moving_box.pos[0]+1, self.moving_box.pos[1])
                        self.map[self.snake_body[-1].pos[0]+1][self.snake_body[-1].pos[1]] = self.Block(pygame.Surface((0,0)), self.snake_body[-1].pos[0]+1, self.snake_body[-1].pos[1], self.BlockTypes.BLANK)
                    
                    want_head = self.map[self.snake_body[-1].pos[0]+1][self.snake_body[-1].pos[1]]
                    if want_head.block_type not in [self.BlockTypes.BLANK, self.BlockTypes.APPLE, self.BlockTypes.BOX, self.BlockTypes.CHECKPOINT, self.BlockTypes.END_POINT]:
                        return

                    self.moving = True
                    self.moving_direction = self.Direction.RIGHT

                    self.moving_process = 0
                    if self.snake_body[-1].block_type != self.BlockTypes.RIGHT_SNAKE_HEAD:
                        self.moving_process = -6
                        self.snake_move_trun = True
                    
    def key_release(self, key: int):
        match key:
            case pygame.K_UP | pygame.K_w:
                pass
            case pygame.K_DOWN | pygame.K_s:
                pass
            case pygame.K_LEFT | pygame.K_a:
                pass
            case pygame.K_RIGHT | pygame.K_d:
                pass
    
    def __log_snake_body(self):
        # logging.debug("\nsnake body:")
        # for block in self.snake_body:
        #     logging.debug(f"pos: {block.pos}, type: {block.block_type}, rotate: {block.rotate}")
        # logging.debug("")
        pass

chessboard = Chessboard()