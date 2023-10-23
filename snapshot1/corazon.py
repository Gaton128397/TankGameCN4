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

# Crear una lista de instancias de Corazon
corazones = []

for i in range(10):
    x = i * 80  # Ajusta la posición x según tus necesidades
    y = 100  # Ajusta la posición y según tus necesidades
    corazon = Corazon(x, y)
    corazones.append(corazon)

# Bucle principal del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    VENTANA.fill((255, 255, 255))  # Rellenar la ventana con color blanco

    # Dibujar los corazones en la ventana
    for corazon in corazones:
        corazon.draw_corazon(VENTANA)

    pygame.display.update()
