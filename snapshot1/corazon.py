import pygame

class Corazon:
    def __init__(self, x, y, rotar=False):
        self.x = x
        self.y = y
        self.rotar = rotar

        # Cargar imágenes de medio corazón
        self.medio_corazon = pygame.image.load('snapshot1/MedioCorazon.png').convert_alpha()

        if self.rotar:
            # Rotar medio corazón en 90 grados horizontales
            self.medio_corazon = pygame.transform.flip(self.medio_corazon, True, False)

    def dibujar(self, superficie):
        superficie.blit(self.medio_corazon, (self.x, self.y))

# Ejemplo de uso
corazon1 = Corazon(100, 100)
corazon2 = Corazon(200, 100, rotar=True)

