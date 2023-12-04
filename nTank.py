<<<<<<< HEAD
import pygame, sys, math, random
# from functions import *

class Tank:
    def __init__(self,position, color,LoR,surface,terrainPoints):
        self.x = position
        self.y = 0
        while not ((self.x,self.y) in terrainPoints):
            #print("do")
            self.y += 1
=======
import pygame, sys, math, random, params, drawFunctions, nTerrain
from functions import *

class Tank:
    def __init__(self,color,LoR, terrainPoints, window):
        self.xpos = 0
        self.ypos = 0
        self.hitBox = {}
        self.window = window
        
        
>>>>>>> origin/Cherry
            
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
        self.surfaceTank.set_alpha()
        self.surfaceTank.set_colorkey((255,0,255))
        self.longitud = int(self.surfaceTank.get_width()*0.12) #largo del cañon
        self.xCanon1 =self.x #coordenadas del cañon
        self.yCanon1  = (self.y - self.height) - self.height/4
        self.xCanon2 = (self.xCanon1 + a*self.longitud * math.cos(math.radians(self.angulo)))
        self.yCanon2 = (self.yCanon1 - self.longitud * math.sin(math.radians(self.angulo)))
<<<<<<< HEAD
        
        self.ammo10mm = 3
        self.ammo8mm = 10
        self.ammo6mm = 3
        contador = 0 
        
    def showInventory(self): #va a ser una mini pantalla con los items y sus cantidades
        print(self.inventory)
        print(self.money)

=======
        self.draw_tank(True)
        self.getFallPoint()
        self.getHitBox()
        
>>>>>>> origin/Cherry
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

    def fallTank(self, terrainPoints, matriz):
        if not (self.getFallPoint() in terrainPoints):
            falling = True
            while falling:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        falling = False
                        pygame.quit()
                self.ypos += 0.5
                self.window.blit(matriz[0],(0,0))
                self.window.blit(matriz[1],(0,0))
                self.window.blit(self.surfaceTank,self.getPos())
                pygame.display.flip()
                if self.getFallPoint() in terrainPoints:
                    self.ypos = int(self.ypos)
                    falling = False
                    self.hitBox = {}
                    print(self.ypos)
                    self.getHitBox()
                if self.ypos > params.HEIGHT:
                    falling = False
                    self.ypos = params.HEIGHT
                    self.hitBox = {}
                    self.getHitBox()
                    print(self.ypos)
                    
        
    def setPos(self,posicion):
        self.xpos = posicion[0]
        self.ypos = posicion[1]
    
    def printTankPost(self):
        print((self.x+self.xpos,self.y+self.ypos))
    #funcion para mover el canon del tanque    

    # funcion con hitbox del tanque              

def testPlayer():
    pygame.init()
    terrain = nTerrain.TerrenoVariado(params.WIDTH, params.HEIGHT)
    window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    bg = pygame.Surface((params.WIDTH, params.HEIGHT))
    player = Tank("blue",1, terrain.getDiccionary, window)
    clock = pygame.time.Clock()
    #clock.tick(60)
    drawFunctions.backgroundDraw(bg)
    player.setPos((200,int(10)))
    player.getHitBox()
    matriz = [bg, terrain.surfTerrain]
    contador = 0
    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
            player.fallTank(terrain.getDiccionary(), matriz)
            if pygame.mouse.get_pressed()[2]:
                terrain.updateImpact(pygame.mouse.get_pos(),100)
                player.fallTank(terrain.getDiccionary(), matriz)
                if player.getFallPoint()[1] > params.HEIGHT:
                    print("se muricio")
                print("PUM!!!")
            elif pygame.mouse.get_pressed()[0]:
                if pygame.mouse.get_pos() in player.hitBox:
                    print("xd")
                else:
                    print("no xd")
        #contador += 0.1
        window.blit(bg,(0,0))
        
        window.blit(terrain.surfTerrain,(0,0))
        window.blit(player.surfaceTank,player.getPos())
        clock.tick(60)
        pygame.display.flip()
testPlayer()