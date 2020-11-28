import pygame
from random import randrange
from character import Character

##########################################################################
# Initialization
pygame.init()

# Screen size setting
screen_width = 480
screen_height = 640
screen = pygame.display.set_mode((screen_width, screen_height))

# Screen title setting
pygame.display.set_caption("똥피하기") # The name of the game

# FPS Setting
clock = pygame.time.Clock()
fps_value = 30

# Load background image
background = pygame.image.load("images/background.png")
##########################################################################

# Game Initialization (Background, images, position, font)
# Instantiate and initialize the player
player = Character("images/character.png")
character_x_pos = (screen_width / 2) - (player.width / 2)
character_y_pos = screen_height - player.height
player.setPosition(character_x_pos, character_y_pos)
character_velocity = 0.8 # Player movement speed
x_change = 0 # Variable for the change of position

# Poops prefab
poop_image_file = "images/poop1.png"
poop_image = pygame.image.load(poop_image_file)
poop_size = poop_image.get_rect().size
poop_width = poop_size[0] # Width
poop_height = poop_size[1] # Height
poop_speed = 2
poops = []
poop_start_time = pygame.time.get_ticks()
poop_create_interval = 2000

# Font setting
game_font = pygame.font.Font(None, 40) # Creating Font Object

# Other variables
score = 0


# Event loop
game_running = True
while game_running:
  dt = clock.tick(fps_value) # Setting FPS for the screen
  
  # Event processing
  for event in pygame.event.get():
    if event.type == pygame.QUIT: # Is screen window closed?
      game_running = False
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT: # Left key
        x_change -= character_velocity
      elif event.key == pygame.K_RIGHT: # Right key
        x_change += character_velocity
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT and x_change < 0: # Left key
        x_change = 0
      elif event.key == pygame.K_RIGHT  and x_change > 0: # Right key
        x_change = 0
  
  # Set game Character position
  character_x_pos += x_change*dt

  # Set the boundaries
  if character_x_pos < 0:
    character_x_pos = 0
  elif character_x_pos > (screen_width - player.width):
    character_x_pos = (screen_width - player.width)
  
  player.setPosition(character_x_pos, character_y_pos)

  index = 0
  for poop in poops:
    x, y = poop.getPosition()
    if y > screen_height: # Removing the poop when it hits the floor
      poops.pop(index)
      score += 1
      if score == 5:
        poop_speed += 4
        poop_create_interval -= 300
      elif score == 10:
        poop_speed += 4
        poop_create_interval -= 300
      elif score == 20:
        poop_speed += 4
        poop_create_interval -= 300
      elif score == 40:
        poop_speed += 4
        poop_create_interval -= 300
    poop.setPosition(x, y + poop_speed)
    index += 1

    # Collision process
    if player.isCollidingWith(poop):
      print("Hit by poop!")
      game_running = False

  # Create poop every 2 seconds
  current_time = pygame.time.get_ticks()
  if (current_time - poop_start_time) >= poop_create_interval:
    poop_start_time = current_time
    pos = randrange(screen_width - poop_width)
    poop = Character(poop_image_file)
    poop.setPosition(pos,0)
    poops.append(poop)
  
  # Draw on the screen
  screen.blit(background, (0, 0)) # Insert background

  player.draw(screen)

  for poop in poops:
    poop.draw(screen)
  
  score_obj = game_font.render(str(score), True, (255,255,255))
  screen.blit(score_obj,(10, 10))
  
  pygame.display.update() # Draw Game screen

# print(pygame.font.get_fonts())
pygame.time.delay(2000)

# pygame exit
pygame.quit()