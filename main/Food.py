from random import randint

import pygame.draw

from main.constants import INT_WINDOW_WIDTH, INT_BLOCK_SIZE, INT_WINDOW_HEIGHT

class Food:
  def __init__(self, str_name, col_color, int_points):
    self.str_name = str_name
    self.col_color = col_color
    self.int_points = int_points
    self.tpl_position = self.generate_random_position()

  def generate_random_position(self):
    int_x = randint(0, (INT_WINDOW_WIDTH - INT_BLOCK_SIZE) // INT_BLOCK_SIZE) * INT_BLOCK_SIZE
    int_y = randint(0, (INT_WINDOW_HEIGHT - INT_BLOCK_SIZE) // INT_BLOCK_SIZE) * INT_BLOCK_SIZE
    return int_x, int_y

  def draw(self, a_screen, a_col_color):
    pygame.draw.rect(a_screen, a_col_color, pygame.Rect(
      self.tpl_position[0], self.tpl_position[1], INT_BLOCK_SIZE, INT_BLOCK_SIZE
    ))

  def __str__(self):
    return f"Food {self.str_name}, Color: {self.col_color}, Points: {self.int_points}, Position: {self.tpl_position}"