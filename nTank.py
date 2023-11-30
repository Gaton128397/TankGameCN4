import pygame, sys, math, random, params, drawFunctions, nTerrain
from functions import *

class Tank:
    def __init__(self,color,LoR):
        self.xpos = 0
        self.ypos = 0
        
        
            
        #valores de la hitbox. Cambiar esto por llamar a la funcion 
        #self.y = self.y-20
        #self.x = self.x - 70
        #tambien cambiar n magicos por % de pantalla para el reescalado
        
        
        self.color = color
        #self.terrainPoints = terrainPoints
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
        self.tankProportion = 0.2
        self.surfaceTank = pygame.Surface((params.WIDTH*self.tankProportion, params.HEIGHT*self.tankProportion))
        self.x = int(self.surfaceTank.get_width()*0.3)
        self.y = int(self.surfaceTank.get_height()*0.57)
        self.width = int(self.surfaceTank.get_width()*0.24)
        self.height = int(self.surfaceTank.get_height()*0.15)
        self.surfaceTank.fill((255,0,255))
        self.surfaceTank.set_alpha()
        self.surfaceTank.set_colorkey((255,0,255))
        self.longitud = int(self.surfaceTank.get_width()*0.15) #largo del cañon
        self.xCanon1 =(self.x + self.width/2)  #coordenadas del cañon
        self.yCanon1  = (self.y - self.height/3)
        self.xCanon2 = (self.xCanon1 + a*self.longitud * math.cos(math.radians(self.angulo)))
        self.yCanon2 = (self.yCanon1 - self.longitud * math.sin(math.radians(self.angulo)))
        self.draw_tank(True)
        
        
    def draw_tank(self,staticCan):
        pygame.draw.rect(self.surfaceTank, self.color, (self.x, self.y, self.width, self.height)) #rectangulo inicial
        pygame.draw.rect(self.surfaceTank, self.color, (self.x + self.width/4, self.y - self.height/5, self.width/2, self.height/2)) #circunferencia de la izquierda
        pygame.draw.circle(self.surfaceTank, self.color, ((self.x, self.y + self.height/2)), self.height/2) #circunferencia de la derecha
        pygame.draw.circle(self.surfaceTank, self.color, ((self.x + self.width, self.y + self.height/2)), self.height/2) #rectangulo donde estara el cañon
        
        if(staticCan):
            pygame.draw.line(self.surfaceTank, self.color, (self.xCanon1, self.yCanon1), (self.xCanon2, self.yCanon2), int(self.surfaceTank.get_height()*0.05)) #cañon
            
    def getPos(self):
        return (self.xpos, self.ypos)
    
    def setPos(self,posicion):
        self.xpos = posicion[0]
        self.ypos = posicion[1]
    #funcion para mover el canon del tanque    

    # funcion con hitbox del tanque              

def testPlayer():
    pygame.init()
    terrain = nTerrain.TerrenoVariado(params.WIDTH, params.HEIGHT)
    window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    bg = pygame.Surface((params.WIDTH, params.HEIGHT))
    player = Tank("blue",1)
    clock = pygame.time.Clock()
    #clock.tick(60)
    drawFunctions.backgroundDraw(bg)
    player.setPos((300,-70))
    contador = 0
    ejecutando = True
    while ejecutando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ejecutando = False
            if pygame.mouse.get_pressed()[2]:
                print("xd")
            elif pygame.mouse.get_pressed()[0]:
                print("dx")
        contador += 0.1
        window.blit(bg,(0,0))
        player.setPos((300,int(player.getPos()[1]+contador)))
        window.blit(terrain.surfTerrain,(0,0))
        window.blit(player.surfaceTank,player.getPos())
        clock.tick(60)
        pygame.display.flip()
testPlayer()