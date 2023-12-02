import pygame, params, random, drawFunctions

class BarraVida:
    def __init__(self, proporcion):
        self.lifeSurface = pygame.Surface((int(params.WIDTH * proporcion), int(params.HEIGHT * proporcion)))
        self.alphaColor = (255,0,255)
        self.lifeSurface.set_alpha()
        self.lifeSurface.set_colorkey(self.alphaColor)
        self.lifeSurface.fill((255,0,255))
        self.vida = 100  # Inicializamos la vida a 100
        self.corazones = ['imgs/health/full.png'] * 5  # Inicializamos los 5 corazones a llenos
        self.game_over_image = pygame.image.load('imgs/game_over.png')  # Cargamos la imagen de game over

    def loadImagen(self, imagen, proporcionX, proporcionY, position):
        loadImage = pygame.image.load(imagen)
        loadScale = pygame.transform.scale(loadImage, (self.lifeSurface.get_width()*proporcionX, self.lifeSurface.get_height()*proporcionY))
        self.lifeSurface.blit(loadScale, (int(self.lifeSurface.get_width() *position[0]),int(self.lifeSurface.get_height() *position[1])))

    def takeDMG(self, dmg):
        if self.vida > 0:  # Verificamos si aún queda vida
            self.vida -= dmg  # Restamos la vida
            num_corazon = self.vida // 20  # Calculamos el número de corazón que debemos modificar
            if self.vida % 20 == 0:  # Si la vida es múltiplo de 20, el corazón estará vacío
                self.corazones[num_corazon] = 'imgs/health/none.png'
            elif self.vida % 20 <= 10:  # Si la vida es menor o igual a 10, el corazón estará a la mitad
                self.corazones[num_corazon] = 'imgs/health/half.png'
            else:  # Si no, el corazón estará lleno
                self.corazones[num_corazon] = 'imgs/health/full.png'
            self.actualizarCorazones()  # Actualizamos los corazones en la barra de vida
        else:  # Si no queda vida
            self.lifeSurface.fill((255,0,255))
            self.loadImagen('imgs/game_over.png', 0.5, 0.5, (0.05, 0.05))
    
    def actualizarCorazones(self):
        for i, img in enumerate(self.corazones):
            self.loadImagen(img, 0.1, 0.1, (0.1 * (i + 1), 0.1))
    
    def restoreLife(self, life):
        if self.vida != 0:
            self.vida += life  # Restauramos la vida
            if self.vida > 100:  # Si la vida supera los 100, la limitamos a 100
                self.vida = 100
            if self.vida == 100:  # Si la vida es 100, todos los corazones deben estar llenos
                self.corazones = ['imgs/health/full.png'] * 5
            else:
                num_corazon = self.vida // 20  # Calculamos el número de corazón que debemos modificar
                if num_corazon < len(self.corazones):  # Verificamos que num_corazon no exceda el tamaño de la lista
                    if self.vida % 20 == 0:  # Si la vida es múltiplo de 20, el corazón estará lleno
                        self.corazones[num_corazon] = 'imgs/health/full.png'
                    elif self.vida % 20 <= 10:  # Si la vida es menor o igual a 10, el corazón estará a la mitad
                        self.corazones[num_corazon] = 'imgs/health/half.png'
                    else:  # Si no, el corazón estará lleno
                        self.corazones[num_corazon] = 'imgs/health/full.png'
            self.actualizarCorazones()  # Actualizamos los corazones en la barra de vida
        else:
            print("game over")

def testLifeBar():
    pygame.init()
    window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    bg = pygame.Surface((params.WIDTH, params.HEIGHT))
    drawFunctions.backgroundDraw(bg)
    barra = BarraVida(0.2)
    barra.actualizarCorazones()
    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
            if pygame.mouse.get_pressed()[2]:
                barra.takeDMG(10)  # Si se pulsa el botón derecho del ratón, restamos 10 de vida
            elif pygame.mouse.get_pressed()[0]:
                barra.restoreLife(10)
            window.blit(bg,(0,0))
            window.blit(barra.lifeSurface, (0, 0))
        pygame.display.flip()
    pygame.quit()
testLifeBar()
