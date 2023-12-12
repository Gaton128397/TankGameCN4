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
        self.surf = pygame.Surface((params.size*16*0.05,params.size*9*0.07))
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
            self.blastRadius = int(params.size*16*0.07)
            self.DMG = 50
            
        elif self.typeBullet == 4: #80mm
            cargarProyectil(self.surf,"imgs/icons/80mmStone.png",1,1,(0,0))
            pygame.draw.circle(self.surf, (0,0,0), (int(self.surf.get_width()/2),int(self.surf.get_height()/2)), 2)
            self.blastRadius = int(params.size*16*0.05)
            self.DMG = 40
            
        elif self.typeBullet == 5: #60mm
            cargarProyectil(self.surf,"imgs/icons/60mmStone.png",0.6,0.6,(0,0))
            pygame.draw.circle(self.surf, (0,0,0), (int(self.surf.get_width()/2),int(self.surf.get_height()/2)), 2)
            self.blastRadius = int(params.size*16*0.03)
            self.DMG = 30
        self.origin = (position[0],position[1])
        if theta < 100 and theta > 85:
            variable = random.randint(0,1)
            if variable == 0:
                self.theta = 85 - random.randint(0,5)
            else:
                self.theta = 100 + random.randint(0,5)
            
        self.theta = toRadian(abs(theta))

        self.x, self.y = position[0], position[1]

        # self.color = 'blue'

        self.ch = 0
        if (theta >90):
            self.dx = -params.size*16*0.002
        else:
            self.dx = params.size*16*0.002
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
        while (self.x >0 and self.x < params.size*16) and (self.yNew < params.size*9):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.x += self.dx + self.wind/100
            self.ch = self.getProjectilePos(self.x - self.origin[0])
            self.yNew = self.y-self.ch
            self.win.blit(matriz[0],(0,0))
            self.win.blit(matriz[1],(0,0))
            self.win.blit(matriz[2],(params.size*16*0.7,0))
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
            clock.tick(self.reloj)
            pygame.display.update()
        pygame.display.update()
        return (int(self.x+puntox),int(self.yNew+puntoy))
        
