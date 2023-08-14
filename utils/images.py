import pygame

from utils.shared import *

pygame.init()

# Load images
if theme_dark:
    title_img = pygame.image.load("data/gfx/title_light.png")
else:
    title_img = pygame.image.load("data/gfx/title_dark.png")
