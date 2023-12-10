import pygame, sys, math, random, params, drawFunctions, nTerrain, threading, playerPhysics, nBarraVida
from functions import *

class Tank:
    def __init__(self,color, window, playerID):
        self.playerID = playerID
        self.xpos = 0
        self.ypos = 0
        self.hitBox = {}
        self.window = window
        self.listaEventos = [] #indice 0 mover cañon, indice 1 poderes
        self.cargarEventos()
        self.lifeBar = nBarraVida.BarraVida(0.1)
        self.health = True
        self.color = color

        self.angulo = 60

        self.xCanon1 = 0
        self.yCanon1 = 0

        self.xCanon2 = 0
        self.yCanon2 = 0

        self.end = (0,0)

        self.tankProportion = 0.22
        self.surfaceTank = pygame.Surface((params.WIDTH*self.tankProportion, params.HEIGHT*self.tankProportion))
        self.x = int(self.surfaceTank.get_width()*0.4)
        self.y = int(self.surfaceTank.get_height()*0.7)
        self.width = int(self.surfaceTank.get_width()*0.22)
        self.height = int(self.surfaceTank.get_height()*0.14)
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
        self.getFallPoint()
        self.getHitBox()
        self.surfaceTank.blit(self.lifeBar.lifeSurface,(int(self.surfaceTank.get_width()*0.28),int(self.surfaceTank.get_height()*0.74)))
        
    def cargarEventos(self):
        diccionarioEventosCañon = {}
        diccionarioEventosCañon[pygame.K_LEFT] = 1
        diccionarioEventosCañon[pygame.K_RIGHT] = -1
        self.listaEventos.append(diccionarioEventosCañon)
        

        
    def draw_tank(self):
        pygame.draw.polygon(self.surfaceTank, self.color, ((self.x, self.y), (self.x - self.width/2, self.y), (self.x - self.width/2, self.y - self.height),(self.x + self.width/2, self.y - self.height),(self.x + self.width/2, self.y),(self.x, self.y))) #rectangulo inicial
        pygame.draw.polygon(self.surfaceTank, self.color, ((self.x, self.y - self.height), (self.x - self.width/3, self.y - self.height), (self.x - self.width/3, (self.y- self.height) - self.height/3),(self.x + self.width/3, (self.y- self.height) - self.height/3),(self.x + self.width/3, (self.y- self.height)))) #rectangulo donde estara el cañon
        pygame.draw.circle(self.surfaceTank, self.color, ((self.x - self.width/2, self.y+1 - self.height/2)), self.height/2 + 1) #circunferencia de la izquierda
        pygame.draw.circle(self.surfaceTank, self.color, ((self.x + self.width/2, self.y+1 - self.height/2)), self.height/2 + 1) #circunferencia de la derecha
        pygame.draw.line(self.surfaceTank, self.color, (self.xCanon1, self.yCanon1), (self.xCanon2, self.yCanon2), int(self.surfaceTank.get_height()*0.04)) #cañon
        
    def actualizarTanque(self):
        pygame.draw.rect(self.surfaceTank, self.alphaColor, (0,0,self.surfaceTank.get_width(),self.surfaceTank.get_height()))
        self.draw_tank()
        self.surfaceTank.blit(self.lifeBar.lifeSurface,(int(self.surfaceTank.get_width()*0.28),int(self.surfaceTank.get_height()*0.74)))
        
    def actualizarVida(self,vida):
        self.lifeBar.actualizarVida(vida)
        self.actualizarTanque()

    def actualizarAngulo(self, event):
        if self.listaEventos[0][event] == 1:
            if self.angulo < 180:
                self.angulo += 1
        if self.listaEventos[0][event] == -1:
            if self.angulo > 0:
                self.angulo += -1
        self.xCanon2 = (self.xCanon1 + self.longitud * math.cos(math.radians(self.angulo)))
        self.yCanon2 = (self.yCanon1 - self.longitud * math.sin(math.radians(self.angulo)))
        self.actualizarTanque()
        
    def getPos(self):
        return (self.xpos, self.ypos)
    
    def getFallPoint(self):
        
        return (int(self.getPos()[0]+int(self.surfaceTank.get_width()*0.4)),int(self.getPos()[1]+int(self.surfaceTank.get_height()*0.7)))

    def getHitBox(self):
        puntoOrigenHB = (self.getPos()[0]+int(self.surfaceTank.get_width()*0.25),self.getPos()[1]+int(self.surfaceTank.get_height()*0.54))
        HitLarge = int(self.width*1.36)
        HitHeight = int(self.height*1.24)
        for i in range(puntoOrigenHB[0], puntoOrigenHB[0]+HitLarge):
            for j in range(puntoOrigenHB[1], puntoOrigenHB[1]+HitHeight):
                self.hitBox[(i,j)] = True
    
    def setPos(self,posicion):
        self.xpos = posicion[0]
        self.ypos = posicion[1]
    
    def printTankPost(self):
        print((self.x+self.xpos,self.y+self.ypos))
        
    def getVida(self):
        return self.lifeBar.vida
    
    def recalcularCordCanon(self):
        self.xCanon1 =self.x
        self.yCanon1  = (self.y - self.height) - self.height/4
        self.xCanon2 = (self.xCanon1 + self.longitud * math.cos(math.radians(self.angulo)))
        self.yCanon2 = (self.yCanon1 - self.longitud * math.sin(math.radians(self.angulo)))
        
def actualizar(window,i):
    window.blit(i.surfaceTank,i.getPos())
            


#def testPlayer():
    
