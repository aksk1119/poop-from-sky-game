import pygame

class LevelManager:
  def __init__(self):
    self.score = 0
    self.level = 0
    self.font = pygame.font.Font(None, 30)
    self.game_speed = 0.5
    self.spawn_interval = 2100

  def setScore(self):
    self.score += 1
    if self.score % 10 == 0:
      self.level += 1
      self.game_speed += 0.3
      if self.spawn_interval > 100:
        self.spawn_interval -= 400
        

  def getLevel(self)-> int:
    return self.level

  def displayCurrScore(self, screen):
    score_obj = self.font.render("Score: " + str(self.score), True, (255,255,255))
    screen.blit(score_obj,(10, 10))

    score_obj = self.font.render("Level: " + str(self.level), True, (255,255,255))
    screen.blit(score_obj,(10, 50))
  
  def gameover(self, screen):
    screen.fill((0,0,0))
    message = self.font.render("Game Over", True, (255,255,255))
    screen.blit(message,(10, 320))
    pygame.display.update()