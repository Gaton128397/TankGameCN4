import pygame, params, drawFunctions

# Define la clase para la barra de carga
class BarraDeCarga:
    def __init__(self, proporcion):
        self.poweBarSurface = pygame.Surface((int(params.WIDTH * proporcion), int(params.HEIGHT * proporcion)))
        self.proporcion = proporcion
        self.alphaColor = (255,255,255)
        self.poweBarSurface.set_alpha()
        self.poweBarSurface.set_colorkey(self.alphaColor)
        self.poweBarSurface.fill((255,255,255))
        self.rect = pygame.Rect(0, 0, int(params.WIDTH * proporcion)*0.8, int(params.HEIGHT * proporcion)*0.2)
        self.color = (255, 0, 0)
        self.carga = 0  # Inicia la carga en 0
<<<<<<< HEAD
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
=======
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
>>>>>>> 805a6ec9bc642aaca7451425bb355dd7b20380e9
        texto_porcentaje = f'{self.obtener_porcentaje():.2f}%'
        texto_completo = f'Poder Actual: {texto_porcentaje}'
        texto = self.fuente.render(texto_completo, True, (0, 0, 0))
        self.poweBarSurface.blit(texto, (self.rect.x, self.rect.y + self.rect.height + self.proporcion*5))
        superficie.blit(self.poweBarSurface, (0,0))

    def borrarTexto(self):
        pygame.draw.rect(self.poweBarSurface, self.alphaColor, (self.rect.x, self.rect.y + self.rect.height + self.proporcion*5, self.rect.width, self.rect.height))

    def cargar(self, incremento):
<<<<<<< HEAD
        if self.carga > self.rect.width / 2:  # Se divide por 2 para que la carga máxima sea la mitad del ancho de la barra
            self.carga = self.rect.width / 2
        elif self.carga < self.rect.width / 2:
            self.carga += incremento

    def resetear(self):
        self.carga = 0

    def obtener_porcentaje(self):
        return (self.carga / (self.rect.width / 2)) * 100  # Se divide por 2 para que el porcentaje se base en la mitad del ancho de la barra
=======
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
pygame.init()
barra = BarraDeCarga(0.2)
window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
bg = pygame.Surface((params.WIDTH, params.HEIGHT))
drawFunctions.backgroundDraw(bg)
ejecutando = True
while ejecutando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Verifica si la tecla espacio está presionada
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_SPACE]:
        barra.cargar(0.05)  # Incrementa la carga mientras se presiona espacio
        print(barra.carga)
    else:
        barra.resetear()  # Resetea la carga si no se presiona espacio

    # Actualiza la pantalla
    window.blit(bg,(0,0))  # Limpia la pantalla
    barra.dibujar(window)  # Dibuja la barra de carga
    barra.actualizarTexto(window)  # Actualiza el texto de la barra de carga
    pygame.display.flip()

pygame.quit()
>>>>>>> 805a6ec9bc642aaca7451425bb355dd7b20380e9
