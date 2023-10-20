import pygame,math,sys
from random import randint
class terrenoCoseno:
    def __init__(self,screen,width,height):
        self.window = screen
        self.width = width
        self.height = height
        self.cos_points = []
        self.yCosPoints = []
    def getTerrain(self):

        amplitude = 60#randint(80,90)
        frequency = 0.02#randint(1,2)/100
        phase_shift = 0

        for x in range(self.width):
            y = amplitude * math.cos(frequency * x + phase_shift) + self.height/2 + 150
            self.cos_points.append((x, int(y)))
            self.yCosPoints.append(int(y))
            #print(self.cos_points[x])
    def drawTerrain(self):
        self.window.fill('lightblue')
        pygame.draw.polygon(self.window, (255, 213, 158), [(0, self.height)] + self.cos_points + [(self.width, self.height)])
        pygame.draw.lines(self.window, (139, 69, 19), False, self.cos_points, 5)
        # pygame.display.update()
    def getCosPoints(self):
        return(self.cos_points)
    def yCosPoint(self):
        return self.yCosPoints