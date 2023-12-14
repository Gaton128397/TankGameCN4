import pygame, sys, params, button

class item:
    def __init__(self,id,nombre,descripcion,precio,icon):
        self.ID = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.Icon = icon
    def resize(self):
        self.Icon = pygame.transform.scale(self.Icon, (params.size,params.size))