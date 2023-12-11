import pygame,sys,params,random

class Map:
    def __init__(self,ID,img,gravity,wind,terrainColor):
        self.ID = ID
        self.img = img
        self.gravity = gravity
        self.wind = wind
        self.img = pygame.transform.scale(self.img, (params.size*16, params.size*9))
        self.terrainColor = terrainColor

    def getMap(self):
        return (self.img,self.gravity,self.wind)
    
    # def draw(self,window):
    #     window.blit(self.img,(0,0))

    # def getGravity(self):
    #     return self.gravity
    
    # def getWind(self):
    #     return self.wind