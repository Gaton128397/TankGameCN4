import pygame
import sys

class Cloud:
    def __init__(self,window, x, y, tangible):
        self.screen = window
        self.x = x
        self.y = y
        self.tangible = tangible

    def draw(self):
        pygame.draw.circle(self.screen, 'white', (self.x, self.y), 30)
        pygame.draw.circle(self.screen, 'white', (self.x+15, self.y-10), 30)
        pygame.draw.circle(self.screen, 'white', (self.x+45, self.y-10), 30)
        pygame.draw.circle(self.screen, 'white', (self.x+60, self.y), 30)
        pygame.draw.circle(self.screen, 'white', (self.x+30, self.y), 30)
