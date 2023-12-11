import math,pygame,params, drawFunctions, nTerrain, nTank, random, playerPhysics, ninfoBlock
from functions import *
FPS = 60
def cargarProyectil(surf, imagen, proporcionX, proporcionY, posicion):
    imagen_cargada = pygame.image.load(imagen)
    imagen_escalada = pygame.transform.scale(imagen_cargada, (surf.get_width()*proporcionX, surf.get_height()*proporcionY))
    surf.blit(imagen_escalada, (posicion))
class Projectile():
    def __init__(self, position, typeBullet,power, theta,window,listaJugador,gravity,wind):
        self.reloj = 400
        super(Projectile, self).__init__()
        #('se crea')
        self.listaJugador = listaJugador
        self.typeBullet = typeBullet
        self.quantity = 0
        self.dmg = 0
        self.surf = pygame.Surface((params.WIDTH*0.05,params.HEIGHT*0.07))
        self.alphaColor = (255,0,255)
        self.surf.fill(self.alphaColor)
        self.surf.set_alpha()
        self.surf.set_colorkey(self.alphaColor)
        self.power = power
        self.explosionArea = 0
        self.blastRadius = 0
        self.DMG = 0
        self.g = gravity
        self.wind = wind
        if self.typeBullet == 3: #105mm
            cargarProyectil(self.surf,"imgs/icons/105mmStone.png",1,1,(0,0))
            pygame.draw.circle(self.surf, (0,0,0), (int(self.surf.get_width()/2),int(self.surf.get_height()/2)), 2)
            self.blastRadius = int(params.WIDTH*0.07)
            self.DMG = 50
            
        elif self.typeBullet == 4: #80mm
            cargarProyectil(self.surf,"imgs/icons/80mmStone.png",1,1,(0,0))
            pygame.draw.circle(self.surf, (0,0,0), (int(self.surf.get_width()/2),int(self.surf.get_height()/2)), 2)
            self.blastRadius = int(params.WIDTH*0.05)
            self.DMG = 40
            
        elif self.typeBullet == 5: #60mm
            cargarProyectil(self.surf,"imgs/icons/60mmStone.png",0.6,0.6,(0,0))
            pygame.draw.circle(self.surf, (0,0,0), (int(self.surf.get_width()/2),int(self.surf.get_height()/2)), 2)
            self.blastRadius = int(params.WIDTH*0.03)
            self.DMG = 30
        self.origin = (position[0],position[1])

        self.theta = toRadian(abs(theta))

        self.x, self.y = position[0], position[1]

        # self.color = 'blue'

        self.ch = 0
        if (theta >90):
            self.dx = -params.WIDTH*0.001
        else:
            self.dx = params.WIDTH*0.001
        print("este es self dx"+str(self.dx))
        self.f = self.getTrajectory()

        self.range = self.x + abs(self.getRange())
        self.win = window
        self.path = []
        self.oldPath = []
        self.hit = False
        self.hitYourself = False

    def timeOfFlight(self):
        return round((2 * self.power * math.sin(self.theta)) / self.g, 2)

    def getRange(self):

        range_ = ((self.power ** 2) * 2 * math.sin(self.theta) * math.cos(self.theta)) / self.g
        return round(range_, 2)

    def getMaxHeight(self):

        h = ((self.power ** 2) * (math.sin(self.theta)) ** 2) / (2 * self.g)
        return round(h, 2)

    def getTrajectory(self):
        
        return round(self.g /  (2 * (self.power ** 2) * (math.cos(self.theta) ** 2)), 4) 

    def getProjectilePos(self, x):

        return x * math.tan(self.theta) - self.f * x ** 2
    
    def shoot(self,matriz,puntosTerreno):
        clock = pygame.time.Clock()
        self.yNew = self.y-self.ch
        puntox = int(self.surf.get_width()/2)
        puntoy = int(self.surf.get_height()/2)
        self.x += 10
        while (self.x >0 and self.x < params.WIDTH) and (self.yNew < params.HEIGHT):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.x += self.dx + self.wind/100
            self.ch = self.getProjectilePos(self.x - self.origin[0])
            self.yNew = self.y-self.ch
            self.win.blit(matriz[0],(0,0))
            self.win.blit(matriz[1],(0,0))
            self.win.blit(matriz[2],(params.WIDTH*0.7,0))
            self.win.blit(self.surf,(int(self.x),int(self.yNew)))
            for i in range(len(self.listaJugador)):
                self.win.blit(self.listaJugador[i].surfaceTank,self.listaJugador[i].getPos())
            if (int(self.x+puntox),int(self.yNew+puntoy)) in puntosTerreno:
                return (int(self.x+puntox),int(self.yNew+puntoy))
            else:
                for i in range(len(self.listaJugador)):
                    if (int(self.x+puntox),int(self.yNew+puntoy)) in self.listaJugador[i].hitBox:
                        print("ouch")
                        return (int(self.x+puntox),int(self.yNew+puntoy))
            clock.tick(self.reloj)
            pygame.display.update()
        pygame.display.update()
        return (int(self.x+puntox),int(self.yNew+puntoy))
        
def game():
    pygame.init()
    run = True
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    terrain = nTerrain.TerrenoVariado()
    bg = pygame.Surface((params.WIDTH, params.HEIGHT))
    drawFunctions.backgroundDraw(bg)
    info = ninfoBlock.infoBlock(0.3)
    info.actualizarAngulo('10')
    info.actualizarDistancia("2000")
    info.actualizarEscudo(False)
    info.actualizarDmg(False)
    info.actualizarBotellas("0")
    info.actualizarTipoBala("105")
    info.actualizarCantidadBalas(0)
    listajugador = []
    for i in range(1):
        listajugador.append(nTank.Tank(700,(255,0,0),window))
    matriz = []
    matriz.append(bg)
    matriz.append(terrain.surfTerrain)
    matriz.append(info.bloque)
    playerPhysics.playerSpawn(window,listajugador,terrain,drawFunctions.returnSurface(matriz))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            elif pygame.mouse.get_pressed()[0]:
                print(pygame.mouse.get_pos())
        bullet = Projectile((100,10),1,random.randint(1,100),60,window,listajugador)
        terrain.updateImpact(bullet.shoot(matriz,terrain.getDiccionary()),bullet,listajugador)
        playerPhysics.fallTanks(window,listajugador,terrain.getDiccionary(),drawFunctions.returnSurface(matriz))
        window.blit(matriz[0],(0,0))
        window.blit(matriz[1],(0,0))
        window.blit(listajugador[0].surfaceTank,listajugador[0].getPos())
        window.blit(matriz[2],(870,0))
        pygame.display.update()
#game()