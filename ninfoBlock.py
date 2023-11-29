import pygame, params, drawFunctions, random

class infoBlock:
    def __init__(self, proporcion):
        self.bloque = pygame.Surface((int(params.WIDTH * proporcion), int(params.HEIGHT * proporcion)))
        self.alphaColor = (255,255,255)
        self.bloque.set_alpha()
        self.bloque.set_colorkey(self.alphaColor)
        
        self.bloque.fill(self.alphaColor)
        self.actualizarTitulo()
        self.cargar_imagen('imgs/angulo.png',0.15,0.2,(0.02,0.03))
        self.cargar_imagen('imgs/distancia.png',0.15,0.2,(0.02,0.27))
        self.cargar_imagen('imgs/elixir.png',0.1,0.17,(0.7,0.4))
        self.cargar_imagen('imgs/bala.png',0.1,0.15,(0.05,0.5))
        self.cargar_imagen('imgs/balas.png',0.1,0.15,(0.05,0.7))
        
        
    def cargar_imagen(self, imagen, proporcionX, proporcionY, posicion):
        imagen_cargada = pygame.image.load(imagen)
        imagen_escalada = pygame.transform.scale(imagen_cargada, (self.bloque.get_width()*proporcionX, self.bloque.get_height()*proporcionY))
        self.bloque.blit(imagen_escalada, (int(self.bloque.get_width() *posicion[0]),int(self.bloque.get_height() *posicion[1])))

    def actualizarAngulo(self, texto):
        texto = str(texto)
        self.borrarAngulo()
        texto = '°'+ texto
        fuente = pygame.font.Font(None, int(self.bloque.get_width() *0.09))
        superficie_texto = fuente.render(texto, True, (0, 0, 0))
        self.bloque.blit(superficie_texto, (int(self.bloque.get_width() *0.2), int(self.bloque.get_width() *0.05)))
        
    def actualizarDistancia(self, texto):
        texto = str(texto)
        self.borrarDistancia()
        texto = texto + " m"
        fuente = pygame.font.Font(None, int(self.bloque.get_width() *0.09))
        superficie_texto = fuente.render(texto, True, (0, 0, 0))
        self.bloque.blit(superficie_texto, (int(self.bloque.get_width() *0.23), int(self.bloque.get_width() *0.17)))
        
    def actualizarBotellas(self, texto):
        texto = str(texto)
        self.borrarBotellas()
        texto = "x"+texto
        fuente = pygame.font.Font(None, int(self.bloque.get_width() *0.09))
        superficie_texto = fuente.render(texto, True, (0, 0, 0))
        self.bloque.blit(superficie_texto, (int(self.bloque.get_width() *0.81), int(self.bloque.get_height() *0.45)))
        
    def actualizarEscudo(self, condicion):
        if condicion:
            self.borrarEscudo()
            self.cargar_imagen('imgs/shield.png',0.1,0.17,(0.7,0.2))
        else:
            self.borrarEscudo()
            
    def actualizarDmg(self, condicion):
        if condicion:
            self.borrarDmg()
            self.cargar_imagen('imgs/sword.png',0.1,0.17,(0.8,0.2))
        else:
            self.borrarDmg()
            
    def actualizarTitulo(self):
        fuente = pygame.font.Font(None, int(self.bloque.get_width() *0.09))
        superficie_texto = fuente.render("PODERES", True, (0, 0, 0))
        self.bloque.blit(superficie_texto, (int(self.bloque.get_width() *0.7), int(self.bloque.get_width() *0.05)))
        
    def actualizarTipoBala(self,texto):
        texto = str(texto)
        self.borrarTipoBala()
        texto = texto + "mm"
        fuente = pygame.font.Font(None, int(self.bloque.get_width() *0.09))
        superficie_texto = fuente.render(texto, True, (0, 0, 0))
        self.bloque.blit(superficie_texto, (int(self.bloque.get_width() *0.23), int(self.bloque.get_height() *0.5)))
    
    def actualizarCantidadBalas(self,texto):
        texto = str(texto)
        self.borrarCantidadBala()
        texto = "x"+texto
        fuente = pygame.font.Font(None, int(self.bloque.get_width() *0.09))
        superficie_texto = fuente.render(texto, True, (0, 0, 0))
        self.bloque.blit(superficie_texto, (int(self.bloque.get_width() *0.23), int(self.bloque.get_height() *0.72)))
        
    def borrarDmg(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.8), int(self.bloque.get_height() *0.2), int(self.bloque.get_width() *0.1), int(self.bloque.get_height() *0.2)))
        
    def borrarEscudo(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.7), int(self.bloque.get_height() *0.2), int(self.bloque.get_width() *0.1), int(self.bloque.get_height() *0.2)))
        
    def borrarAngulo(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.21), int(self.bloque.get_width() *0.05), int(self.bloque.get_width() *0.15), int(self.bloque.get_width() *0.07)))
        
    def borrarDistancia(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.23), int(self.bloque.get_width() *0.17), int(self.bloque.get_width() *0.22), int(self.bloque.get_width() *0.07)))

    def borrarBotellas(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.81), int(self.bloque.get_height() *0.45), int(self.bloque.get_width() *0.15), int(self.bloque.get_height() *0.1)))
    
    def borrarTipoBala(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.23), int(self.bloque.get_height() *0.5), int(self.bloque.get_width() *0.22), int(self.bloque.get_height() *0.1)))

    def borrarCantidadBala(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.23), int(self.bloque.get_height() *0.72), int(self.bloque.get_width() *0.15), int(self.bloque.get_height() *0.1)))

pygame.init()
window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
bg = pygame.Surface((params.WIDTH, params.HEIGHT))
drawFunctions.backgroundDraw(bg)
info = infoBlock(0.5)
info.actualizarAngulo('180')
info.actualizarDistancia("1920")
info.actualizarEscudo(True)
info.actualizarDmg(True)
info.actualizarBotellas("100")
info.actualizarTipoBala("105")
info.actualizarCantidadBalas("10")
#info.actualizarAngulo('50')
contador = 0
contador_x = 0
contador_y = 0
velocidad = 5
direccion_x = 1
direccion_y = 1
conds = [True,False]
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        if pygame.mouse.get_pressed()[2]:
            print("xd")
        elif pygame.mouse.get_pressed()[0]:
            print("dx")
    contador_x += velocidad * direccion_x
    contador_y += velocidad * direccion_y
    if contador_x <= 0 or contador_x >= params.WIDTH - int(info.bloque.get_width()*0.9):
        direccion_x *= -1
    if contador_y <= 0 or contador_y >= params.HEIGHT - int(info.bloque.get_height()*0.9):
        direccion_y *= -1
    #info.actualizarDmg(conds[random.randint(0,1)])
    #info.actualizarEscudo(conds[random.randint(0,1)])
    info.actualizarAngulo(random.randint(0,180))
    info.actualizarDistancia(random.randint(0,5000))
    info.actualizarBotellas(random.randint(0,100))
    info.actualizarTipoBala(random.randint(0,200))
    info.actualizarCantidadBalas(random.randint(0,50))
    window.blit(bg,(0,0))
    window.blit(info.bloque, (0+contador_x, 0+contador_y))
    pygame.display.flip()

pygame.quit()