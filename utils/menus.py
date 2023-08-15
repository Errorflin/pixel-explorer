import pygame

from utils.shared import *    # Shared variables
from utils.fonts import *     # Fonts
from utils.images import *    # Images

pygame.init()

# Menu items & states
main_menu_items = ["PLAY", "SETTINGS", "INFO", "QUIT"]
item_selected = 0

# MAIN MENU
def main_menu():
    # Draw menu options
    for i, item in enumerate(main_menu_items):
        if i == item_selected:
            if item == "PLAY":
                color = (24, 242, 93) # Play button select color
            elif item == "SETTINGS":
                color = (245, 202, 32) # Settings button select color
            elif item == "INFO":
                color = (32, 174, 245) # Info button select color
            elif item == "QUIT":
                color = (220, 70, 70) # Quit button select color
        else:
            color = text_color # Color while not selected

        text = EvilEmpire140.render(item, True, color)
        text_rect = text.get_rect(center=(screen_size[0] // 2, 420 + i * 105))
        screen.blit(text, text_rect)

    # Render version text
    version = EvilEmpire50.render(f"{game_verision}", True, version_color)
    version_rect = version.get_rect(center=(screen_size[0] // 2, screen_size[1] - 55))
    screen.blit(version, version_rect)

    # Render title image
    screen.blit(title_img, (0, 0))

