import pygame
import sys
pygame.init()

#colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
YELLOW = (255, 255, 0)

#Screen
size = (800, 600)
screen=pygame.display.set_mode(size)

def draw_bird(window,x, y):
    pygame.draw.polygon(window, YELLOW, [(x+30, y-15), (x+50, y), (x+30, y+15)])  # Pico
    pygame.draw.circle(window, WHITE, (x+40, y-5), 5)  # Ojo