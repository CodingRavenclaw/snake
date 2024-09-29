from random import randint
from main.utils.constants import INT_WINDOW_HEIGHT, INT_BLOCK_SIZE, INT_WINDOW_WIDTH

def generate_random_position():
  int_x = randint(0, (INT_WINDOW_WIDTH - INT_BLOCK_SIZE) // INT_BLOCK_SIZE) * INT_BLOCK_SIZE
  int_y = randint(0, (INT_WINDOW_HEIGHT - INT_BLOCK_SIZE) // INT_BLOCK_SIZE) * INT_BLOCK_SIZE
  return int_x, int_y