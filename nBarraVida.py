import pygame, params, random, drawFunctions

class BarraVida:
    def __init__(self, proporcion):
        self.WIDTH = params.size*16
        self.HEIGHT = params.size*9
        self.lifeSurface = pygame.Surface((int(self.WIDTH * proporcion), int(self.HEIGHT * proporcion)))
        self.alphaColor = (255,0,255)
        self.lifeSurface.set_alpha()
        self.lifeSurface.set_colorkey(self.alphaColor)
        self.lifeSurface.fill((255,0,255))
        self.vida = 100  # Inicializamos la vida a 100
        self.corazones = ['health/full.png','health/half.png','health/none.png'] * 5  # Inicializamos los 5 corazones a llenos
        # self.game_over_image = pygame.image.load('game_over.png')  # Cargamos la imagen de game over
        self.actualizarVida(0)

    def loadImagen(self, imagen, proporcionX, proporcionY, position):
        loadImage = pygame.image.load(imagen)
        loadScale = pygame.transform.scale(loadImage, (self.lifeSurface.get_width()*proporcionX, self.lifeSurface.get_height()*proporcionY))
        self.lifeSurface.blit(loadScale, (int(self.lifeSurface.get_width() *position[0]),int(self.lifeSurface.get_height() *position[1])))

    def actualizarVida(self, dmg):
        vidaMaxima = 100
        dmg = int(dmg)
        self.vida -= dmg
        if self.vida >= 0:
            corazonLLeno = 0
            corazonMitad = 0
            corazonVacío = 0
            corazonLLeno = self.vida//20
            if self.vida%20 > 0:
                corazonMitad = 1
            corazonVacío = vidaMaxima//20 - corazonLLeno - corazonMitad
            self.actualizarCorazones(corazonLLeno,corazonMitad,corazonVacío)
        else:
            self.lifeSurface.fill((255,0,255))
        
    def actualizarCorazones(self,corazonLLeno,corazonMitad,corazonVacío):
        j = 0
        for i in range(corazonLLeno):
            self.loadImagen('health/full.png',0.1,0.1,(0.1*j,0))
            j += 1
        for i in range(corazonMitad):
            self.loadImagen('health/half.png',0.1,0.1,(0.1*j,0))
            j += 1
        for i in range(corazonVacío):
            self.loadImagen('health/none.png',0.1,0.1,(0.1*j,0))
            j += 1

    def restoreLife(self, life):
        if self.vida != 0:
            self.vida += life  # Restauramos la vida
            if self.vida > 100:  # Si la vida supera los 100, la limitamos a 100
                self.vida = 100
            if self.vida == 100:  # Si la vida es 100, todos los corazones deben estar llenos
                self.corazones = ['health/full.png'] * 5
            else:
                num_corazon = self.vida // 20  # Calculamos el número de corazón que debemos modificar
                if num_corazon < len(self.corazones):  # Verificamos que num_corazon no exceda el tamaño de la lista
                    if self.vida % 20 == 0:  # Si la vida es múltiplo de 20, el corazón estará lleno
                        self.corazones[num_corazon] = 'health/full.png'
                    elif self.vida % 20 <= 10:  # Si la vida es menor o igual a 10, el corazón estará a la mitad
                        self.corazones[num_corazon] = 'health/half.png'
                    else:  # Si no, el corazón estará lleno
                        self.corazones[num_corazon] = 'health/full.png'
            self.actualizarCorazones()  # Actualizamos los corazones en la barra de vida
        # else:
            #print("game over")
            
    def getVida(self):
        return self.vida
