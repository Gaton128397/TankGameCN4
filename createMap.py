import pygame,sys,params,random

class Map:
    def __init__(self,img,gravity,wind,terrainColor):
        self.img = img
        self.gravity = gravity
        self.wind = wind
        self.width, self.height = params.size*16, params.size*9
        self.img = pygame.transform.scale(self.img, (self.width, self.height))
        self.terrainColor = terrainColor

    def returnMap(self):
        return Map(self.img,self.gravity,self.wind)
    
    def draw(self,window):
        window.blit(self.img,(0,0))

    def getGravity(self):
        return self.gravity
    
    def getWind(self):
        return self.wind