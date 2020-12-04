import pygame
from random import randrange
from character import Character
from level_manager import LevelManager

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
fps_value = 60

# Load background image
background = pygame.image.load("images/background.png")

##########################################################################

# Game Initialization (Background, images, position, font)

# Initialize the sound
pygame.mixer.music.load("music/bgm.mp3")
pygame.mixer.music.play(-1)

drop_sound = pygame.mixer.Sound("music/poop-drop.mp3")
death_sound = pygame.mixer.Sound("music/death.mp3")

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
poops = []
poop_start_time = pygame.time.get_ticks()

# Game manager object
game_manager = LevelManager()

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
      pygame.mixer.Sound.play(drop_sound)
      poops.pop(index)
      game_manager.setScore()
    poop.setPosition(x, y + game_manager.game_speed*dt)
    index += 1

    # Collision process
    if player.isCollidingWith(poop):
      # print("Hit by poop!")
      pygame.mixer.Sound.play(death_sound)
      pygame.time.delay(1000)
      game_running = False

  # Create poop every 2 seconds
  current_time = pygame.time.get_ticks()
  if (current_time - poop_start_time) >= game_manager.spawn_interval:
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
  
  game_manager.displayCurrScore(screen)
  
  pygame.display.update() # Draw Game screen

game_manager.gameover(screen)
pygame.display.update()
pygame.time.delay(1000)

# pygame exit
pygame.quit()