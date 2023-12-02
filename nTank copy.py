import pygame, sys, math, random, params, drawFunctions, nTerrain, threading, nBarraVida
from functions import *

class Tank:
    def __init__(self,color,LoR, terrainPoints, window):
        self.xpos = 0
        self.ypos = 0
        self.hitBox = {}
        self.window = window

        #vida del tanque
        self.health = 100

        #valores de la hitbox. Cambiar esto por llamar a la funcion 
        #self.y = self.y-20
        #self.x = self.x - 70
        #tambien cambiar n magicos por % de pantalla para el reescalado
        
        
        self.color = color
        self.terrainPoints = terrainPoints
        #eliminar: self.origin = (position[0] + 25, position[1] - 6.5)

        self.angulo =0
        

        #self.surface = surface
        self.LoR = LoR

        self.xCanon1 = 0
        self.yCanon1 = 0

        self.xCanon2 = 0
        self.yCanon2 = 0

        self.end = (0,0)
        a =1
        if self.LoR == 0:
            a = -1
        
        #self.xCanon1 =(self.x + self.width/2)  #coordenadas del cañon
        #self.yCanon1  = (self.y - self.height/3)
        
       
        #self.xCanon2 = (self.xCanon1 + a*self.longitud * math.cos(math.radians(self.angulo)))
        self.tankProportion = 0.22
        self.surfaceTank = pygame.Surface((params.WIDTH*self.tankProportion, params.HEIGHT*self.tankProportion))
        self.x = int(self.surfaceTank.get_width()*0.4)
        self.y = int(self.surfaceTank.get_height()*0.7)
        self.width = int(self.surfaceTank.get_width()*0.22)
        self.height = int(self.surfaceTank.get_height()*0.14)

        
        self.surfaceTank.fill((255,0,255))
        #self.surfaceTank.set_alpha()
        #self.surfaceTank.set_colorkey((255,0,255))
        self.longitud = int(self.surfaceTank.get_width()*0.12) #largo del cañon
        self.xCanon1 =self.x #coordenadas del cañon
        self.yCanon1  = (self.y - self.height) - self.height/4
        self.xCanon2 = (self.xCanon1 + a*self.longitud * math.cos(math.radians(self.angulo)))
        self.yCanon2 = (self.yCanon1 - self.longitud * math.sin(math.radians(self.angulo)))
        self.draw_tank(True)
        self.getFallPoint()
        self.getHitBox()
        self.getLifeBar()
        
    def draw_tank(self,staticCan):
        pygame.draw.polygon(self.surfaceTank, self.color, ((self.x, self.y), (self.x - self.width/2, self.y), (self.x - self.width/2, self.y - self.height),(self.x + self.width/2, self.y - self.height),(self.x + self.width/2, self.y),(self.x, self.y))) #rectangulo inicial
        pygame.draw.polygon(self.surfaceTank, self.color, ((self.x, self.y - self.height), (self.x - self.width/3, self.y - self.height), (self.x - self.width/3, (self.y- self.height) - self.height/3),(self.x + self.width/3, (self.y- self.height) - self.height/3),(self.x + self.width/3, (self.y- self.height)))) #rectangulo donde estara el cañon
        pygame.draw.circle(self.surfaceTank, self.color, ((self.x - self.width/2, self.y+1 - self.height/2)), self.height/2 + 1) #circunferencia de la izquierda
        pygame.draw.circle(self.surfaceTank, self.color, ((self.x + self.width/2, self.y+1 - self.height/2)), self.height/2 + 1) #circunferencia de la derecha
        if(staticCan):
            pygame.draw.line(self.surfaceTank, self.color, (self.xCanon1, self.yCanon1), (self.xCanon2, self.yCanon2), int(self.surfaceTank.get_height()*0.04)) #cañon
            
    def getPos(self):
        return (self.xpos, self.ypos)
    
    def getFallPoint(self):
        #pygame.draw.circle(self.surfaceTank, (0,0,0), (self.getPos()[0]+int(self.surfaceTank.get_width()*0.4),self.getPos()[1]+int(self.surfaceTank.get_height()*0.7)), 1)
        return (int(self.getPos()[0]+int(self.surfaceTank.get_width()*0.4)),int(self.getPos()[1]+int(self.surfaceTank.get_height()*0.7)))

    def getHitBox(self):
        puntoOrigenHB = (self.getPos()[0]+int(self.surfaceTank.get_width()*0.25),self.getPos()[1]+int(self.surfaceTank.get_height()*0.54))
        HitLarge = int(self.width*1.36)
        HitHeight = int(self.height*1.24)
        print(puntoOrigenHB)
        for i in range(puntoOrigenHB[0], puntoOrigenHB[0]+HitLarge):
            for j in range(puntoOrigenHB[1], puntoOrigenHB[1]+HitHeight):
                self.hitBox[(i,j)] = True
        #pygame.draw.rect(self.surfaceTank, (0,0,0), (self.getPos()[0]+int(self.surfaceTank.get_width()*0.25),self.getPos()[1]+int(self.surfaceTank.get_height()*0.54),self.width*1.36,self.height*1.24), 1)

    def fallTank(self,listaJugadores,parach, terrainPoints, surface):
        clock = pygame.time.Clock()
        if not (self.getFallPoint() in terrainPoints):
            if not parach:
                falling = True
                while falling:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            falling = False
                            pygame.quit()
                    self.ypos += params.gravityConstant
                    self.window.blit(surface,(0,0))
                    for i in listaJugadores:
                        self.window.blit(i.surfaceTank,i.getPos())
                    self.window.blit(self.surfaceTank,self.getPos())
                    clock.tick(60)
                    pygame.display.flip()
                    if self.getFallPoint() in terrainPoints:
                        self.ypos = int(self.ypos)
                        falling = False
                        self.hitBox = {}
                        print(self.ypos)
                        self.getHitBox()
                    if self.ypos > params.HEIGHT:
                        print("se muricio")
                        falling = False
                        self.ypos = params.HEIGHT
                        self.hitBox = {}
                        self.getHitBox()
                        print(self.ypos)
            else:
                falling = True
                copy = self.surfaceTank.copy()
                drawFunctions.cargarImagen(self.surfaceTank,"props/parachute/parach1.png",0.2,0.5,(0.32,0.03))
                g = params.gravityConstant//3
                while falling:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            falling = False
                            pygame.quit()
                    self.ypos += g
                    self.window.blit(surface,(0,0))
                    for i in listaJugadores:
                        self.window.blit(i.surfaceTank,i.getPos())
                    self.window.blit(self.surfaceTank,self.getPos())
                    clock.tick(60)
                    pygame.display.flip()
                    if self.getFallPoint() in terrainPoints:
                        self.surfaceTank = copy
                        #self.surfaceTank.blit(self.surfaceTank,(0,0))
                        self.ypos = int(self.ypos)
                        falling = False
                        self.hitBox = {}
                        print(self.ypos)
                        self.getHitBox()
    
    def getLifeBar(self):
        lifeBarPos = (self.getPos()[0]+int(self.surfaceTank.get_width()*0.25), self.getPos()[1]+int(self.surfaceTank.get_height()*0.72))
        lifeHight = self.height*0.7
        lifeWidth = self.width*1.4
        LifeBar = nBarraVida.BarraVida(0.2)
        pygame.draw.rect(self.surfaceTank, (0,0,0), (self.getPos()[0]+int(self.surfaceTank.get_width()*0.25),self.getPos()[1]+int(self.surfaceTank.get_height()*0.72),self.width*1.4,self.height*0.7), 1)
                
                    
        
    def setPos(self,posicion):
        self.xpos = posicion[0]
        self.ypos = posicion[1]
    
    def printTankPost(self):
        print((self.x+self.xpos,self.y+self.ypos))
    
    def getLifeBar(self):
        lifeBarPos = (self.getPos()[0]+int(self.surfaceTank.get_width()*0.25), self.getPos()[1]+int(self.surfaceTank.get_height()*0.72))
        lifeHight = self.height*0.7
        lifeWidth = self.width*1.4
        pygame.draw.rect(self.surfaceTank, (0,0,0), (self.getPos()[0]+int(self.surfaceTank.get_width()*0.25),self.getPos()[1]+int(self.surfaceTank.get_height()*0.72),self.width*1.4,self.height*0.7), 1)
        
def player_fall(cond,listaJugadores,player,terrain,surface):
    player.fallTank(listaJugadores,cond,terrain.getDiccionary(), surface)
    #funcion para mover el canon del tanque    
    
def playerSpawn(listaJugadores,terrain,surface):
    threadList = []
    for i in range(len(listaJugadores)):
        threadList.append(threading.Thread(target=player_fall, args=(True,listaJugadores,listaJugadores[i],terrain,surface)))
        threadList[i].start()
    for i in range(len(listaJugadores)):
        threadList[i].join()
        
def playerFall(listaJugadores,terrain,surface):
    threadList = []
    for i in range(len(listaJugadores)):
        threadList.append(threading.Thread(target=player_fall, args=(False,listaJugadores,listaJugadores[i],terrain,surface)))
        threadList[i].start()
    for i in range(len(listaJugadores)):
        threadList[i].join()

def returnSurface(matriz):
    surface = pygame.Surface((params.WIDTH, params.HEIGHT))
    surface.blit(matriz[0],(0,0))
    surface.blit(matriz[1],(0,0))
    return surface


def testPlayer():
    pygame.init()
    terrain = nTerrain.TerrenoVariado(params.WIDTH, params.HEIGHT)
    window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    bg = pygame.Surface((params.WIDTH, params.HEIGHT))
    player = Tank("blue",1, terrain.getDiccionary, window)
    clock = pygame.time.Clock()
    #clock.tick(60)
    drawFunctions.backgroundDraw(bg)
    player.setPos((500,int(100)))

    player.getHitBox()
    surperficeJuego = [bg, terrain.surfTerrain]
    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False

            if pygame.mouse.get_pressed()[2]:
                print("click derecho")

            elif pygame.mouse.get_pressed()[0]:
                print("click izquierdo")

        #contador += 0.1
        window.blit(bg,(0,0))
        
        window.blit(terrain.surfTerrain,(0,0))
        window.blit(player.surfaceTank,player.getPos())
        clock.tick(60)
        pygame.display.flip()
testPlayer()