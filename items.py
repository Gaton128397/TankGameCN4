import pygame, sys, params, button

class item:
    def __init__(self,id,nombre,descripcion,precio,icon):
        self.nombre = nombre
        self.ID = id
        self.descripcion = descripcion
        self.precio = precio
        self.Icon = icon
    def showItem(self,screen):
        pass
