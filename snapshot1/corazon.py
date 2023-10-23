import pygame
import sys

# Inicializar pygame
pygame.init()

# Definir dimensiones de la ventana
ANCHO, ALTO = 1300, 700
VENTANA = pygame.display.set_mode((ANCHO, ALTO))

class Corazon:
    def __init__(self, x, y, rotar=False):
        self.x = x
        self.y = y
        self.rotar = rotar

        
        self.medio_corazon = pygame.image.load('snapshot1/MedioCorazon.png').convert_alpha()

        # Redimensionar el corazón al 80% del tamaño original
        nuevo_ancho = int(self.medio_corazon.get_width() * 0.8)
        nuevo_alto = int(self.medio_corazon.get_height() * 0.8)
        self.medio_corazon = pygame.transform.scale(self.medio_corazon, (nuevo_ancho, nuevo_alto))

        if self.rotar:
            self.medio_corazon = pygame.transform.flip(self.medio_corazon, True, False)
    
    def draw_corazon(self, superficie):
        superficie.blit(self.medio_corazon, (self.x, self.y))



