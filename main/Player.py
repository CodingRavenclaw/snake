class Player:
  def __init__(self, str_name, col_color, int_lives):
    self.str_name = str_name
    self.int_score = 0
    self.col_color = col_color
    self.int_lives = int_lives

  def increase_score(self, int_points):
    self.int_score += int_points

  def reset_score(self):
    self.int_score = 0

  def __str__(self):
    return f"Player {self.str_name}, Score: {self.int_score}, Color: {self.col_color}"