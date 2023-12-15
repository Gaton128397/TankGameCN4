import pygame, params, drawFunctions, random,scoreBoard

class infoBlock:
    def __init__(self, proporcion):
        self.WIDTH = params.size*16
        self.HEIGHT = params.size*9
        self.bloque = pygame.Surface((int(self.WIDTH * proporcion), int(self.HEIGHT * proporcion)))
        self.proporcion = proporcion
        self.alphaColor = (255,255,255)
        self.bloque.set_alpha()
        self.bloque.set_colorkey(self.alphaColor)
        
        self.bloque.fill(self.alphaColor)
        self.actualizarTitulo()
        self.cargar_imagen("items/angulo.png",0.15,0.2,(0.02,0.03))
        self.cargar_imagen("items/distancia.png",0.15,0.2,(0.02,0.27))
        self.cargar_imagen("items/bala.png",0.1,0.15,(0.05,0.5))
        self.cargar_imagen("items/balas.png",0.1,0.15,(0.05,0.7))
        
        self.turnoTanque = scoreBoard.imgTank((255,0,0),self.proporcion*0.2)
        self.bloque.blit(self.turnoTanque.surfaceTank,(int(self.bloque.get_width() *0.7), int(self.bloque.get_height() *0.7)))
        
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
        
        
    def actualizarEscudo(self, condicion):
        if condicion:
            self.borrarEscudo()
            self.cargar_imagen(params.shield,0.1,0.17,(0.7,0.2))
        else:
            self.borrarEscudo()
            
    def actualizarDmg(self, condicion):
        if condicion:
            self.borrarDmg()
            self.cargar_imagen(params.dmg,0.1,0.17,(0.8,0.2))
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
        if texto > 0:
            texto = str(texto)
            self.borrarCantidadBala(False)
            texto = "x"+texto
            fuente = pygame.font.Font(None, int(self.bloque.get_width() *0.09))
            superficie_texto = fuente.render(texto, True, (0, 0, 0))
            self.bloque.blit(superficie_texto, (int(self.bloque.get_width() *0.23), int(self.bloque.get_height() *0.72)))
        else:
            self.borrarCantidadBala(False)
            texto = "OUT OF AMMO"
            fuente = pygame.font.Font(None, int(self.bloque.get_width() *0.08))
            superficie_texto = fuente.render(texto, True, (0, 0, 0))
            self.bloque.blit(superficie_texto, (int(self.bloque.get_width() *0.18), int(self.bloque.get_height() *0.72)))
    def borrarDmg(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.8), int(self.bloque.get_height() *0.2), int(self.bloque.get_width() *0.1), int(self.bloque.get_height() *0.2)))
        
    def borrarEscudo(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.7), int(self.bloque.get_height() *0.2), int(self.bloque.get_width() *0.1), int(self.bloque.get_height() *0.2)))
        
    def borrarAngulo(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.21), int(self.bloque.get_width() *0.05), int(self.bloque.get_width() *0.15), int(self.bloque.get_width() *0.07)))
        
    def borrarDistancia(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.23), int(self.bloque.get_width() *0.17), int(self.bloque.get_width() *0.22), int(self.bloque.get_width() *0.07)))

    def borrarTipoBala(self):
        pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.23), int(self.bloque.get_height() *0.5), int(self.bloque.get_width() *0.22), int(self.bloque.get_height() *0.1)))

    def borrarCantidadBala(self,cond):
        if cond:
            pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.23), int(self.bloque.get_height() *0.72), int(self.bloque.get_width() *0.15), int(self.bloque.get_height() *0.1)))
        else:
            pygame.draw.rect(self.bloque, self.alphaColor, pygame.Rect(int(self.bloque.get_width() *0.18), int(self.bloque.get_height() *0.72), int(self.bloque.get_width() *0.4), int(self.bloque.get_height() *0.1)))
    
    def actualizarTanque (self, color):
        self.turnoTanque = scoreBoard.imgTank(color,self.proporcion*0.2)
        self.bloque.blit(self.turnoTanque.surfaceTank,(int(self.bloque.get_width() *0.7), int(self.bloque.get_height() *0.7)))
