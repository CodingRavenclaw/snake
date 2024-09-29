import pygame
from main.utils.constants import COLOR_BLACK, COLOR_RED, COLOR_GREEN, INT_WINDOW_WIDTH, INT_WINDOW_HEIGHT, INT_BLOCK_SIZE
from main.Food import Food
from main.Snake import Snake
from main.utils.constants import INT_FPS
from main.utils.math import generate_random_position

pygame.init()
pygame.display.set_caption("Snake à la Niederstetten")
GAME_WINDOW = pygame.display.set_mode((INT_WINDOW_WIDTH, INT_WINDOW_HEIGHT))

game_clock = pygame.time.Clock()

a_snake = Snake((100, 100), INT_BLOCK_SIZE)
a_food = Food("Strawberry", COLOR_RED, 10, INT_BLOCK_SIZE, (20, 20))
bool_is_running = True

def generate_food_position(p_a_snake):
  while True:
    tpl_food_position = generate_random_position()
    if tpl_food_position not in p_a_snake.arr_body:
      return tpl_food_position

while bool_is_running:
  for anEvent in pygame.event.get():
    if anEvent.type == pygame.KEYDOWN:
      if anEvent.key == pygame.K_w:
        a_snake.change_direction("UP")
      if anEvent.key == pygame.K_s:
        a_snake.change_direction("DOWN")
      if anEvent.key == pygame.K_a:
        a_snake.change_direction("LEFT")
      if anEvent.key == pygame.K_d:
        a_snake.change_direction("RIGHT")

  a_snake.move()

  if a_snake.has_collided_with_body() or a_snake.has_collied_with_border():
    print("GAME OVER")
    bool_is_running = False

  if a_snake.get_head_position() == a_food.tpl_position:
    a_snake.grow()
    tpl_a_food_position = generate_food_position(a_snake)
    a_food = Food("Strawberry", COLOR_RED, 5, INT_BLOCK_SIZE, tpl_a_food_position)

  GAME_WINDOW.fill(COLOR_BLACK)

  a_snake.draw(GAME_WINDOW, COLOR_GREEN)
  a_food.draw(GAME_WINDOW, COLOR_RED)

  pygame.display.update()
  game_clock.tick(INT_FPS)

pygame.quit()
