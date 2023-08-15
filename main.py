import pygame

from utils.shared import *    # Shared variables
from utils.fonts import *     # Fonts
from utils.images import *    # Images
import utils.menus as menus   # Menu rendering
from utils.saveload import *  # Save & load data

pygame.init()

def main():
    clock = pygame.time.Clock()
    switcher = True
    while switcher:
        screen.fill(background_color)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()
            if e.type == pygame.KEYDOWN:
                # Handle menu selection changes
                if e.key == pygame.K_UP:
                    if main_menu: menus.item_selected = (menus.item_selected - 1) % len(menus.main_menu_items)
                elif e.key == pygame.K_DOWN:
                    if main_menu: menus.item_selected = (menus.item_selected + 1) % len(menus.main_menu_items)
                elif e.key == pygame.K_RETURN:
                    if menus.item_selected == 0 and main_menu:    # PLAY
                        print("PLAY")
                    elif menus.item_selected == 1 and main_menu:  # SETTINGS
                        print("SETTINGS")
                    elif menus.item_selected == 2 and main_menu:  # INFO
                        print("INFO")
                    elif menus.item_selected == 3 and main_menu:  # QUIT
                        exit()

        if main_menu:
            menus.main_menu()

        pygame.display.flip()
        clock.tick(fps_limit)

if __name__ == "__main__":
    print(settings_data["keys"])
    main()