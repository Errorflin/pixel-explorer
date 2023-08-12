import pygame
import sys, os

pygame.init()

# Display settings
screen_size = (1920, 1080)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pixel Explorer")
fps_limit = 60

# Color settings
background_color = (20, 20, 20)
foreground_color = (255, 255, 255)
text_color = (255, 255, 255)
select_color = (255, 170, 0)

# States
main_menu = True
settings_menu = True

# Utils functions
def exit():
    pygame.quit()
    sys.exit()