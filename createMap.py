import pygame,sys,params,random

class Map:
    def __init__(self,ID,img,gravity,terrainColor):
        self.ID = ID
        self.img = img
        self.gravity = gravity
        self.img = img 
        self.terrainColor = terrainColor

    def getMap(self):
        return (self.img,self.gravity,self.terrainColor)