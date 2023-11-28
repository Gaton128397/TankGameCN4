import pygame, params, drawFunctions, random

class infoBlock:
    def __init__(self, proporcion):
        self.bloque = pygame.Surface((int(params.WIDTH * proporcion), int(params.HEIGHT * proporcion)))
        self.alphaColor = (255,255,255)
        #self.bloque.set_alpha()
        #self.bloque.set_colorkey(self.alphaColor)
        
        self.bloque.fill(self.alphaColor)
        self.cargar_imagen('imgs/angulo.png',0.15,0.2,(0.02,0.03))
        self.cargar_imagen('imgs/distancia.png',0.15,0.2,(0.02,0.27))
        fuente = pygame.font.Font(None, int(self.bloque.get_width() *0.09))
        superficie_texto = fuente.render("BUFFOS", True, (0, 0, 0))
        self.bloque.blit(superficie_texto, (int(self.bloque.get_width() *0.7), int(self.bloque.get_width() *0.05)))
        #self.cargar_imagen('imgs/distancia.png',0.2,0.2,(0,45))
        
    def cargar_imagen(self, imagen, proporcionX, proporcionY, posicion):
        
        imagen_cargada = pygame.image.load(imagen)
        imagen_escalada = pygame.transform.scale(imagen_cargada, (self.bloque.get_width()*proporcionX, self.bloque.get_height()*proporcionY))
        self.bloque.blit(imagen_escalada, (int(self.bloque.get_width() *posicion[0]),int(self.bloque.get_height() *posicion[1])))

    def actualizarAngulo(self, texto):
        self.borrarAngulo()
        texto = '°'+ texto
        fuente = pygame.font.Font(None, int(self.bloque.get_width() *0.09))
        superficie_texto = fuente.render(texto, True, (0, 0, 0))
        self.bloque.blit(superficie_texto, (int(self.bloque.get_width() *0.2), int(self.bloque.get_width() *0.05)))
        
    def actualizarDistancia(self, texto):
        self.borrarDistancia()
        texto = texto + " m"
        fuente = pygame.font.Font(None, int(self.bloque.get_width() *0.09))
        superficie_texto = fuente.render(texto, True, (0, 0, 0))
        self.bloque.blit(superficie_texto, (int(self.bloque.get_width() *0.23), int(self.bloque.get_width() *0.17)))
        
    def actualizarEscudo(self, condicion):
        if condicion:
            self.borrarEscudo()
            self.cargar_imagen('imgs/shield.png',0.1,0.17,(0.7,0.27))
        else:
            self.borrarEscudo()
            
    def borrarEscudo(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.7), int(self.bloque.get_height() *0.25), int(self.bloque.get_width() *0.1), int(self.bloque.get_height() *0.2)))
        
    def borrarAngulo(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.21), int(self.bloque.get_width() *0.05), int(self.bloque.get_width() *0.15), int(self.bloque.get_width() *0.07)))
        
    def borrarDistancia(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.23), int(self.bloque.get_width() *0.17), int(self.bloque.get_width() *0.22), int(self.bloque.get_width() *0.07)))

pygame.init()

window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
bg = pygame.Surface((params.WIDTH, params.HEIGHT))
drawFunctions.backgroundDraw(bg)
info = infoBlock(0.9)
info.actualizarAngulo('180')
info.actualizarDistancia("1920")
info.actualizarEscudo(True)
#info.actualizarAngulo('50')
contador = 0

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
    if contador < 1000:
        contador += 2
    info.actualizarEscudo(conds[random.randint(0,1)])
    info.actualizarAngulo(str(random.randint(0,180)))
    info.actualizarDistancia(str(random.randint(0,5000)))
    window.blit(bg,(0,0))
    window.blit(info.bloque, (0+contador, 0+contador))
    pygame.display.flip()

pygame.quit()