import pygame, params, drawFunctions

class iconoTurno:
    def __init__(self, proporcion):
        # Inicialización de la clase iconoTurno
        self.WIDTH = params.size*16
        self.HEIGHT = params.size*9
        self.iconoTurnoSurface = pygame.Surface((int(self.WIDTH * proporcion), int(self.HEIGHT * proporcion)))
        self.alphaColor = (255,0,255)
        self.iconoTurnoSurface.set_alpha()
        self.iconoTurnoSurface.set_colorkey(self.alphaColor)
        self.iconoTurnoSurface.fill(self.alphaColor)
        self.actualizarIcono(False)

    def loadImagen(self, imagen, proporcionX, proporcionY, position):
        # Método para cargar y escalar una imagen en el iconoTurnoSurface
        loadImage = pygame.image.load(imagen)
        loadScale = pygame.transform.scale(loadImage, (self.iconoTurnoSurface.get_width()*proporcionX, self.iconoTurnoSurface.get_height()*proporcionY))
        self.iconoTurnoSurface.blit(loadScale, (int(self.iconoTurnoSurface.get_width() *position[0]),int(self.iconoTurnoSurface.get_height() *position[1])))

    def actualizarIcono(self, Turno):
        # Método para actualizar el icono del turno
        if Turno:
            self.loadImagen('items/flechaInvertida.png',1,1,(0,0))
        else:
            self.borrarIcono()

    def borrarIcono(self):
        # Método para borrar el icono del turno llenando el iconoTurnoSurface con el color alfa
        self.iconoTurnoSurface.fill(self.alphaColor)