import pygame

class BarraVida:
    def __init__(self, pantalla, color,posicion, longitud, ancho,player):
        self.pantalla = pantalla
        self.posicion = posicion
        self.longitud = longitud
        self.ancho = ancho
        self.color = color
        self.vida = 100  
        self.player = player

    def actualizar_vida(self, nueva_vida):
        self.vida = max(0, min(100, nueva_vida))

    def drawDibujarVida(self,vidaSurface):
        if self.player == 1:
            rectangulo = pygame.Surface((300,0))
            rectangulo.fill((255, 213, 158))
            vidaSurface.blit(rectangulo,(self.longitud,self.ancho))
    
            longitud_vida = (self.vida / 100) * self.longitud
            pygame.draw.rect(vidaSurface,'black', (*self.posicion, self.longitud, self.ancho))
            pygame.draw.rect(vidaSurface,self.color, (*self.posicion, longitud_vida, self.ancho))
