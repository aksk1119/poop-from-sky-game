import pygame

class Character:
  def __init__(self, image):
    self.x = 0
    self.y = 0
    self.image = pygame.image.load(image) # Loading the image
    self.spriteSize = self.image.get_rect().size # Character image size
    self.width = self.spriteSize[0] # Width
    self.height = self.spriteSize[1] # Height

  def setPosition(self, x: int, y: int):
    self.x = x
    self.y = y

  def getPosition(self)->(int,int):
    return (self.x, self.y)
  
  def draw(self, screen):
    screen.blit(self.image, (self.x, self.y))
  
  def getImage(self):
    return self.image
  
  def isCollidingWith(self, other)->bool:
    character_rect = self.image.get_rect()
    character_rect.left = self.x
    character_rect.top = self.y

    other_rect = other.getImage().get_rect()
    other_rect.left = other.x
    other_rect.top = other.y

    iscoliding = character_rect.colliderect(other_rect)
    return iscoliding
