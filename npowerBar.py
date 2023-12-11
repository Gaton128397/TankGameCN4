import pygame, params, drawFunctions

# Define la clase para la barra de carga
class BarraDeCarga:
    def __init__(self, proporcion):
        self.poweBarSurface = pygame.Surface((int(params.size*16 * proporcion), int(params.size*9 * proporcion)))
        self.proporcion = proporcion
        self.alphaColor = (255,255,255)
        self.poweBarSurface.set_alpha()
        self.poweBarSurface.set_colorkey(self.alphaColor)
        self.poweBarSurface.fill((255,255,255))
        self.rect = pygame.Rect(0, 0, int(params.size*16 * proporcion)*0.8, int(params.size*9 * proporcion)*0.2)
        self.color = (255, 0, 0)
        self.carga = 10  # Inicia la carga en 0
        self.fuente = pygame.font.SysFont('Arial', 20)  # Define la fuente para el texto
        #self.fuente.set_bold(True)

    def dibujar(self, superficie):
        # Dibuja el fondo de la barra
        pygame.draw.rect(self.poweBarSurface, self.color, self.rect)
        # Dibuja la barra de carga
        barra_actual = pygame.Rect(self.rect.x, self.rect.y, self.carga, self.rect.height)
        pygame.draw.rect(self.poweBarSurface, (0, 255, 0), barra_actual)
        superficie.blit(self.poweBarSurface, (0,0))
    
    def actualizarTexto(self, superficie):

        self.borrarTexto()
        # Renderiza el porcentaje y lo muestra debajo de la barra de carga
        texto_porcentaje = f'{self.obtener_porcentaje():.2f}%'
        texto_completo = f'Poder Actual: {texto_porcentaje}'
        texto = self.fuente.render(texto_completo, True, (0, 0, 0))
        self.poweBarSurface.blit(texto, (self.rect.x, self.rect.y + self.rect.height + self.proporcion*5))
        superficie.blit(self.poweBarSurface, (0,0))

    def borrarTexto(self):
        pygame.draw.rect(self.poweBarSurface, self.alphaColor, (self.rect.x, self.rect.y + self.rect.height + self.proporcion*5, self.rect.width, self.rect.height))

    def cargar(self, incremento):
        # Incrementa la carga de la barra
        if self.carga > self.rect.width:
            self.carga = self.rect.width
        elif self.carga < self.rect.width:
            self.carga += incremento
        #la carga se guarda pero una vez se deja de presionar se resetea
    

    def resetear(self):
        # Resetea la carga de la barra
        self.carga = 0
        
    def obtener_porcentaje(self):
        # Devuelve la proporción de la carga como un porcentaje
        return (self.carga / self.rect.width) * 100
# Crea una instancia de la barra de carga


# Bucle principal del juego
