import pygame, sys, params, button

class item:
    def __init__(self,nombre,id,descripcion,precio,icon):
        self.nombre = nombre
        self.ID = id
        self.descripcion = descripcion
        self.precio = precio
        self.Icon = icon
    def resize(self):
        self.Icon = pygame.transform.scale(self.Icon, (params.size,params.size))