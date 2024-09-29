import pygame.draw

from main.utils.constants import INT_WINDOW_WIDTH, INT_WINDOW_HEIGHT, COLOR_BLUE


class Snake:
  def __init__(self, initial_position, int_block_size):
    self.int_block_size = int_block_size
    self.str_direction = "RIGHT"
    self.arr_body = [initial_position]
    self.bool_is_growing = False

  def move(self):
    tpl_new_head = (0, 0)
    int_head_x, int_head_y = self.arr_body[0]

    if self.str_direction == "UP":
      tpl_new_head = (int_head_x, int_head_y - self.int_block_size)
    elif self.str_direction == "DOWN":
      tpl_new_head = (int_head_x, int_head_y + self.int_block_size)
    elif self.str_direction == "LEFT":
      tpl_new_head = (int_head_x - self.int_block_size, int_head_y)
    elif self.str_direction == "RIGHT":
      tpl_new_head = (int_head_x + self.int_block_size, int_head_y)

    self.arr_body = [tpl_new_head] + self.arr_body

    if not self.bool_is_growing:
      self.arr_body.pop()
    else:
      self.bool_is_growing = False

  def change_direction(self, str_new_direction):
    if (str_new_direction == "UP" and self.str_direction != "DOWN") or \
      (str_new_direction == "DOWN" and self.str_direction != "UP") or \
      (str_new_direction == "LEFT" and self.str_direction != "RIGHT") or \
      (str_new_direction == "RIGHT" and self.str_direction != "LEFT"):
        self.str_direction = str_new_direction

  def grow(self):
    self.bool_is_growing = True

  def get_head_position(self):
    return self.arr_body[0]

  def has_collided_with_body(self):
    tpl_head = self.get_head_position()
    return tpl_head in self.arr_body[1:]

  def has_collied_with_border(self):
    int_head_x, int_head_y = self.get_head_position()
    if (int_head_x < 0 or int_head_x >= INT_WINDOW_WIDTH or
        int_head_y < 0 or int_head_y >= INT_WINDOW_HEIGHT):
      return True
    return False

  def draw(self, a_screen, a_col_color):
    tpl_head = self.get_head_position()
    pygame.draw.rect(a_screen, COLOR_BLUE, pygame.Rect(
      tpl_head[0], tpl_head[1], self.int_block_size, self.int_block_size
    ))

    for tpl_a_body_segment in self.arr_body[1:]:
      pygame.draw.rect(a_screen, a_col_color, pygame.Rect(
        tpl_a_body_segment[0], tpl_a_body_segment[1], self.int_block_size, self.int_block_size
      ))
