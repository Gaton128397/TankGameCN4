import pygame, sys, params, button

class item:
    def __init__(self,nombre,descripcion,precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
    def showItem(self,screen):
        pass