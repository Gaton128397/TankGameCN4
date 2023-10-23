import pygame

class Corazon:
    def __init__(self, x, y, rotar=False):
        self.x = x
        self.y = y
        self.rotar = rotar
     
        self.medio_corazon = pygame.image.load('snapshot1/MedioCorazon.png').convert_alpha()

        if self.rotar:
            # Rotar en 90 grados horizontales
            self.medio_corazon = pygame.transform.flip(self.medio_corazon, True, False)

    def draw_corazon(self, superficie):
        superficie.blit(self.medio_corazon, (self.x, self.y))