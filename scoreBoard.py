import pygame, params, drawFunctions, nTank, math

class imgTank:
    def __init__(self,color):
        self.xpos = 0
        self.ypos = 0
        self.angulo = 0
        self.color = color
        self.xCanon1 = 0
        self.yCanon1 = 0
        self.xCanon2 = 0
        self.yCanon2 = 0

        self.tankProportion = 0.05
        self.surfaceTank = pygame.Surface((params.WIDTH*self.tankProportion, params.HEIGHT*self.tankProportion))
        self.x = int(self.surfaceTank.get_width()*0.5)
        self.y = int(self.surfaceTank.get_height()*0.8)
        self.width = int(self.surfaceTank.get_width()*0.55)
        self.height = int(self.surfaceTank.get_height()*0.55)
        self.alphaColor = (255,0,255)
        self.surfaceTank.fill(self.alphaColor)
        #self.surfaceTank.set_alpha()
        #self.surfaceTank.set_colorkey(self.alphaColor)
        self.longitud = int(self.surfaceTank.get_width()*0.12) #largo del cañon
        self.xCanon1 =self.x #coordenadas del cañon
        self.yCanon1  = (self.y - self.height) - self.height/4
        self.xCanon2 = (self.xCanon1 + self.longitud * math.cos(math.radians(self.angulo)))
        self.yCanon2 = (self.yCanon1 - self.longitud * math.sin(math.radians(self.angulo)))
        self.draw_tank()
        

        
    def draw_tank(self):
        pygame.draw.polygon(self.surfaceTank, self.color, ((self.x, self.y), (self.x - self.width/2, self.y), (self.x - self.width/2, self.y - self.height),(self.x + self.width/2, self.y - self.height),(self.x + self.width/2, self.y),(self.x, self.y))) #rectangulo inicial
        pygame.draw.polygon(self.surfaceTank, self.color, ((self.x, self.y - self.height), (self.x - self.width/3, self.y - self.height), (self.x - self.width/3, (self.y- self.height) - self.height/3),(self.x + self.width/3, (self.y- self.height) - self.height/3),(self.x + self.width/3, (self.y- self.height)))) #rectangulo donde estara el cañon
        pygame.draw.circle(self.surfaceTank, self.color, ((self.x - self.width/2, self.y+1 - self.height/2)), self.height/2 + 1) #circunferencia de la izquierda
        pygame.draw.circle(self.surfaceTank, self.color, ((self.x + self.width/2, self.y+1 - self.height/2)), self.height/2 + 1) #circunferencia de la derecha
        pygame.draw.line(self.surfaceTank, self.color, (self.xCanon1, self.yCanon1), (self.xCanon2, self.yCanon2), int(self.surfaceTank.get_height()*0.04)) #cañon
        
    
class scoreBoard():
    def __init__(self,listaJugadores, window,colors,ruta,general):
        self.colors = colors
        self.surface = pygame.Surface((params.WIDTH,params.HEIGHT))
        drawFunctions.backgroundDraw(self.surface,ruta)
        self.window = window
        self.general = general
        self.listaJugadores = listaJugadores
        self.infoMostrar = None
        self.mostrarJugadores()
    def mostrarJugadores(self):
        contador = 0
        for i in range(len(self.listaJugadores)):
            jugador = pygame.Surface((params.WIDTH*0.842,params.HEIGHT*0.07))
            jugador.fill((255,0,255))
            jugador.set_alpha()
            jugador.set_colorkey((255,0,255))
            self.mostrarJugador(jugador,i)
            self.surface.blit(jugador,(params.WIDTH*0.077,params.HEIGHT*0.275+contador))
            contador += params.HEIGHT*0.07
    def mostrarJugador(self,superficie,jugador):
        tank = imgTank(self.colors[jugador])
        superficie.blit(tank.surfaceTank,(0,0))
        if not self.general:
            self.mostrarTexto(superficie,str(self.listaJugadores[jugador].kda[0]),int(superficie.get_width() *0.37))
            self.mostrarTexto(superficie,str(self.listaJugadores[jugador].kda[1]),int(superficie.get_width() *0.65))
            self.mostrarTexto(superficie,str(self.listaJugadores[jugador].money),int(superficie.get_width() *0.85))
        else:
            self.mostrarTexto(superficie,str(self.listaJugadores[jugador].generalkda[0]),int(superficie.get_width() *0.37))
            self.mostrarTexto(superficie,str(self.listaJugadores[jugador].generalkda[1]),int(superficie.get_width() *0.65))
            self.mostrarTexto(superficie,str(self.listaJugadores[jugador].money),int(superficie.get_width() *0.85))
    def mostrarTexto(self,superficie,texto, pos):
        fuente = pygame.font.Font(None, int(params.HEIGHT*0.05))
        superficie_texto = fuente.render(texto, True, (0, 0, 0))
        superficie.blit(superficie_texto, (pos, int(superficie.get_height() *0.05)))
        
    def sb_run(self):
        clock = pygame.time.Clock()
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        run = False
            clock.tick(60)
            self.window.blit(self.surface,(0,0))
            
            pygame.display.flip()
