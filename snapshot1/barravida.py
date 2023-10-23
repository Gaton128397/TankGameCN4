import pygame

class BarraVida:
    def __init__(self, pantalla, posicion, longitud, ancho):
        self.pantalla = pantalla
        self.posicion = posicion
        self.longitud = longitud
        self.ancho = ancho
        self.vida = 100  

    def actualizar_vida(self, nueva_vida):
        self.vida = max(0, min(100, nueva_vida))

    def dibujar(self):
        longitud_vida = (self.vida / 100) * self.longitud

        pygame.draw.rect(self.pantalla,'black', (*self.posicion, self.longitud, self.ancho))

        pygame.draw.rect(self.pantalla,'red', (*self.posicion, longitud_vida, self.ancho))
