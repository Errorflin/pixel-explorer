import pygame

pygame.init()

# Load the font files once
EvilEmpireFile = "data/fonts/EvilEmpire.ttf"
EvilEmpire = {}

# Define the font sizes
font_sizes = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 140, 160, 180]

# Load the fonts and store them in the dictionary
for size in font_sizes:
    EvilEmpire[size] = pygame.font.Font(EvilEmpireFile, size)

# Access fonts in different sizes:
EvilEmpire10 = EvilEmpire[10]
EvilEmpire20 = EvilEmpire[20]
EvilEmpire30 = EvilEmpire[30]
EvilEmpire40 = EvilEmpire[40]
EvilEmpire50 = EvilEmpire[50]
EvilEmpire60 = EvilEmpire[60]
EvilEmpire70 = EvilEmpire[70]
EvilEmpire80 = EvilEmpire[80]
EvilEmpire90 = EvilEmpire[90]
EvilEmpire100 = EvilEmpire[100]
EvilEmpire110 = EvilEmpire[110]
EvilEmpire120 = EvilEmpire[120]
EvilEmpire140 = EvilEmpire[140]
EvilEmpire160 = EvilEmpire[160]
EvilEmpire180 = EvilEmpire[180]