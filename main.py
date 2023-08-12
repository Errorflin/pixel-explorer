import pygame

from utils.shared import *
import utils.menus as menus

pygame.init()

def main():
    clock = pygame.time.Clock()

    switcher = True
    while switcher:
        screen.fill(background_color)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                exit()

        if main_menu:
            menus.main_menu()

        pygame.display.flip()
        clock.tick(fps_limit)

if __name__ == "__main__":
    main()