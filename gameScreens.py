import drawFunctions, pygame, params, scoreBoard, functions, proporciones, params,scoreBoard,math, sys
from button import Button

def pantallaEmpiezaJuego(screen, variableReseteo):
    drawFunctions.backgroundDraw(screen,'Pantallas/juegoPrev.png')
    WIDTH = params.size*16
    HEIGHT = params.size*9
    miniTankSurface = pygame.Surface((int(WIDTH * 0.7), int(HEIGHT * 0.15)))
    alphaColor = (255,0,255)
    miniTankSurface.set_alpha()
    miniTankSurface.set_colorkey(alphaColor)
    miniTankSurface.fill((255,0,255))
    for i in range(params.playersNumber):
        tanque = scoreBoard.imgTank(variableReseteo[i][0],0.1)
        miniTankSurface.blit(tanque.surfaceTank,(int(miniTankSurface.get_width()*0.05*i*3.4), int(miniTankSurface.get_height() *0.2)))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
        screen.blit(miniTankSurface,(int(WIDTH * 0.153), int(HEIGHT * 0.43)))
        pygame.display.update()
        
def controlesPausa(screen):
    run = True
    background = pygame.Surface((screen.get_width(),screen.get_height()))
    drawFunctions.backgroundDraw(background,"Pantallas/ControlesPausa.png")
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
        screen.blit(background,(0,0))
        pygame.display.update()
        
def pauseScreen(screen):
    run = True
    pantalla = 5
    background = pygame.Surface((screen.get_width(),screen.get_height()))
    drawFunctions.backgroundDraw(background,"Pantallas/Pausa.png")
    bttns = crearBotonPausa(proporciones.listaProporciones)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for btns in bttns:
                for btn in btns:
                    if btn.check_click(event):
                        #controles menu
                        if pantalla == 5:
                            if btn.item == 15:
                                #('Vuelve al juego')
                                return None
                            elif btn.item == 16:
                                #('Vuelve al menu')
                                return 4
                            elif btn.item == 17:
                                controlesPausa(screen)
                                #('Controles pausa')
                                pass
                            elif btn.item == 18:
                                #('salir')
                                return -1
        screen.blit(background,(0,0))
        pygame.display.update()
    
def ganadorScreen(screen, colorGanador):
    run = True
    tanqueGanador = imgTankWinner(colorGanador,0.07)
    background = pygame.Surface((screen.get_width(),screen.get_height()))
    drawFunctions.backgroundDraw(background,"Pantallas/Ganador.png")
    bttns = crearBotonPausa(proporciones.listaProporciones)
    pantalla = 2
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            for btns in bttns:
                for btn in btns:
                    if btn.check_click(event):
                        #controles menu
                       if pantalla == 2:
                            if btn.item == 2:
                                #('Volver al menu')
                                return 4
                                
                            elif btn.item == 3:
                                #('Cierra el juego')
                                return -1
                            
        screen.blit(background,(0,0))
        screen.blit(tanqueGanador.surfaceTank,(screen.get_width()*0.46,screen.get_height()*0.65))
        pygame.display.update()
            
def crearBotonPausa(listaProporciones):
    listaBotonesPantallas = []
    pantalla = []
    ID = 0
    x = 0
    for screen in listaProporciones:
        for prop in screen:
            boton = Button(prop[x],prop[x+1],prop[x+2],prop[x+3],ID)
            pantalla.append(boton)
            ID+=1
        listaBotonesPantallas.append(pantalla)
        pantalla=[]
    return listaBotonesPantallas

class imgTankWinner:
    def __init__(self,color,tankProportion):
        self.WIDTH = params.size*16
        self.HEIGHT = params.size*9
        self.xpos = 0
        self.ypos = 0
        self.angulo = 0
        self.color = color
        self.xCanon1 = 0
        self.yCanon1 = 0
        self.xCanon2 = 0
        self.yCanon2 = 0

        self.tankProportion = tankProportion
        self.surfaceTank = pygame.Surface((self.WIDTH*self.tankProportion, self.HEIGHT*self.tankProportion))
        self.x = int(self.surfaceTank.get_width()*0.5)
        self.y = int(self.surfaceTank.get_height()*0.8)
        self.width = int(self.surfaceTank.get_width()*0.55)
        self.height = int(self.surfaceTank.get_height()*0.55)
        self.alphaColor = (255,0,255)
        self.surfaceTank.fill(self.alphaColor)
        self.surfaceTank.set_alpha()
        self.surfaceTank.set_colorkey(self.alphaColor)
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