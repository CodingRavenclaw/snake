import pygame.draw

from main.utils.constants import INT_BLOCK_SIZE


class Food:
  def __init__(self, str_name, col_color, int_points, int_block_size, tpl_position):
    self.str_name = str_name
    self.col_color = col_color
    self.int_points = int_points
    self.int_block_size = int_block_size
    self.tpl_position = tpl_position

  def draw(self, a_screen, a_col_color):
    pygame.draw.rect(a_screen, a_col_color, pygame.Rect(
      self.tpl_position[0], self.tpl_position[1], INT_BLOCK_SIZE, INT_BLOCK_SIZE
    ))

  def __str__(self):
    return f"Food {self.str_name}, Color: {self.col_color}, Points: {self.int_points}, Position: {self.tpl_position}"