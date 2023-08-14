import pygame
import sys, os

pygame.init()

game_verision = "dev. 0.0.0"

# Display settings
screen_size = (1920, 1080)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Pixel Explorer")
fps_limit = 60

# Themes
theme_dark = True

# Color settings
if theme_dark:
    background_color = (20, 20, 20)
    foreground_color = (255, 255, 255)
    text_color = (255, 255, 255)
    select_color = (255, 170, 0)
    version_color = (40, 40, 40)
else:
    background_color = (255, 255, 255)
    foreground_color = (20, 20, 20)
    text_color = (20, 20, 20)
    select_color = (255, 170, 0)
    version_color = (200, 200, 200)

# States
main_menu = True
settings_menu = True

# Utils functions
def exit():
    pygame.quit()
    sys.exit()