import pygame,sys,params,random

class Map:
    def __init__(self,img,gravity,wind,terrainColor):
        self.img = img
        self.gravity = gravity
        self.wind = wind
        self.img = pygame.transform.scale(self.img, (params.WIDTH, params.HEIGHT))
        self.terrainColor = terrainColor

    def getMap(self):
        return (self.img,self.gravity,self.wind)
    
    def draw(self,window):
        window.blit(self.img,(0,0))

    def getGravity(self):
        return self.gravity
    
    def getWind(self):
        return self.wind