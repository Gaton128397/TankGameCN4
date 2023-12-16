import pygame,sys,params,random

class Map:
    def __init__(self,ID,img,gravity,terrainColor):
        self.ID = ID
        self.img = img
        self.gravity = gravity
        self.img = img #'pantalla/imagen'#pygame.transform.scale(self.img, (params.size*16, params.size*9))
        self.terrainColor = terrainColor

    def getMap(self):
        return (self.img,self.gravity,self.terrainColor)