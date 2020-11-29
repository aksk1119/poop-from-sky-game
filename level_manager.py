import pygame

class LevelManager:
  def __init__(self):
    self.score = 0
    self.level = 0
    self.font = pygame.font.Font(None, 30)
    self.game_speed = 2
    self.spawn_interval = 2000

  def setScore(self):
    self.score += 1
    if self.score == 5:
      self.game_speed += 4
      self.spawn_interval -= 400
    elif self.score == 10:
      self.game_speed += 4
      self.spawn_interval -= 400
    elif self.score == 20:
      self.game_speed += 4
      self.spawn_interval -= 500
    elif self.score == 40:
      self.game_speed += 4
      self.spawn_interval -= 500

  def getLevel(self)-> int:
    return self.level

  def displayCurrScore(self, screen):
    score_obj = self.font.render("Score: " + str(self.score), True, (255,255,255))
    screen.blit(score_obj,(10, 10))

    score_obj = self.font.render("Level: " + str(self.level), True, (255,255,255))
    screen.blit(score_obj,(10, 50))