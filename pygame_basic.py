# pip : Python Installer Packages
# pip install pygame
import pygame
import sys

# Initialization
pygame.init()
# Error Output

#(5,0) :-> 5 Functions, 0 Errors.

# Creating a new window

game_window = pygame.display.set_mode(size = (1000 ,1000))

pygame.display.set_caption('My first game...')

# fps: Frames Per Second..
fps = 30
game_clock = pygame.time.Clock() # Game Clock

random_color = pygame.Color(255,0,255)
background_image = pygame.image.load('download.jpeg')
real_bg_img = pygame.transform.scale(background_image,(1000,1000))
snake_position = [[100, 50],[90,50],[80,50]]
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # Cancel button on game window.
            pygame.quit()
            sys.exit()
    game_window.blit(real_bg_img,(0,0))
    pygame.draw.rect(game_window, random_color, [200, 200, 30, 30])

    # game_window.fill(random_color)
    pygame.display.update()
    game_clock.tick(fps)






