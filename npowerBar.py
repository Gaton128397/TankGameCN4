import pygame, params, drawFunctions

# Define la clase para la barra de carga
class BarraDeCarga:
    def __init__(self, proporcion):
        self.WIDTH = params.size*16
        self.HEIGHT = params.size*9
        self.poweBarSurface = pygame.Surface((int(self.WIDTH * proporcion), int(self.HEIGHT * proporcion)))
        self.proporcion = proporcion
        self.alphaColor = (255,255,255)
        self.poweBarSurface.set_alpha()
        self.poweBarSurface.set_colorkey(self.alphaColor)
        self.poweBarSurface.fill((255,255,255))
        self.rect = pygame.Rect(0, 0, int(self.WIDTH * proporcion)*0.8, int(self.HEIGHT * proporcion)*0.2)
        self.color = (255, 0, 0)
        self.carga = 0  # Inicia la carga en 0
        self.fuente = pygame.font.SysFont(None, int(self.poweBarSurface.get_width() *0.09))  # Define la fuente para el texto
        self.fuente.set_bold(True)

    def dibujar(self, superficie):
        pygame.draw.rect(self.poweBarSurface, self.color, self.rect)
        barra_actual = pygame.Rect(self.rect.x, self.rect.y, self.carga*2, self.rect.height)  # Se multiplica por 2 para llenar la barra cuando la carga llega a la mitad
        pygame.draw.rect(self.poweBarSurface, (0, 255, 0), barra_actual)
        self.actualizarTexto(self.poweBarSurface)
        superficie.blit(self.poweBarSurface, (0,0))

    def actualizarTexto(self, superficie):
        self.borrarTexto()
        texto_porcentaje = f'{self.obtener_porcentaje():.2f}%'
        texto_completo = f'Poder Actual: {texto_porcentaje}'
        texto = self.fuente.render(texto_completo, True, (0, 0, 0))
        self.poweBarSurface.blit(texto, (self.rect.x, self.rect.y + self.rect.height + self.proporcion*5))
        superficie.blit(self.poweBarSurface, (0,0))

    def borrarTexto(self):
        pygame.draw.rect(self.poweBarSurface, self.alphaColor, (self.rect.x, self.rect.y + self.rect.height + self.proporcion*5, self.rect.width, self.rect.height))

    def cargar(self, incremento):
        if self.carga > self.rect.width / 2:  # Se divide por 2 para que la carga máxima sea la mitad del ancho de la barra
            self.carga = self.rect.width / 2
        elif self.carga < self.rect.width / 2:
            self.carga += incremento

    def resetear(self):
        self.carga = 0

    def obtener_porcentaje(self):
        return (self.carga / (self.rect.width / 2)) * 100  # Se divide por 2 para que el porcentaje se base en la mitad del ancho de la barra
