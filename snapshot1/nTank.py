import pygame, sys, math, random
from functions import *

class Tank:
    def __init__(self,position, color,LoR,surface,terrainPoints):

        self.health = 100

        self.x = position
        self.y = 0
        while not ((self.x,self.y) in terrainPoints):
            #print("do")
            self.y += 1
            
        #valores de la hitbox. Cambiar esto por llamar a la funcion 
        self.y = self.y-20
        #self.x = self.x - 70
        #tambien cambiar n magicos por % de pantalla para el reescalado
        
        self.width = 50
        self.height = 20
        self.color = color
        self.terrainPoints = terrainPoints
        #eliminar: self.origin = (position[0] + 25, position[1] - 6.5)

        self.angulo = 0
        self.longitud = 25 #largo del cañon

        self.surface = surface
        self.LoR = LoR

        self.xCanon1 = 0
        self.yCanon1 = 0

        self.xCanon2 = 0
        self.yCanon2 = 0

        self.end = (0,0)
        a =1
        if self.LoR == 0:
            a = -1

        self.xCanon1 =(self.x + self.width/2)  #coordenadas del cañon
        self.yCanon1  = (self.y - self.height/3)

        self.xCanon2 = (self.xCanon1 + a*self.longitud * math.cos(math.radians(self.angulo)))
        self.yCanon2 = (self.yCanon1 - self.longitud * math.sin(math.radians(self.angulo)))
        
        self.ammo10mm = 3
        self.ammo8mm = 10
        self.ammo6mm = 3
        contador = 0 
        
        
    def draw_tank(self,staticCan):
        pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.width, self.height)) #rectangulo inicial
        pygame.draw.rect(self.surface, self.color, (self.x + self.width/4, self.y - self.height/5, self.width/2, self.height/2)) #circunferencia de la izquierda
        pygame.draw.circle(self.surface, self.color, ((self.x, self.y + self.height/2)), self.height/2) #circunferencia de la derecha
        pygame.draw.circle(self.surface, self.color, ((self.x + self.width, self.y + self.height/2)), self.height/2) #rectangulo donde estara el cañon
       
        if(staticCan):
            pygame.draw.line(self.surface, self.color, (self.xCanon1, self.yCanon1), (self.xCanon2, self.yCanon2), 4) #cañon
            
    def actualizar(self,a):
            
            if self.LoR == 0:
                a = -1

            self.xCanon2 = self.xCanon1 + a*self.longitud * math.cos(math.radians(self.angulo))
            self.yCanon2 = self.yCanon1 - self.longitud * math.sin(math.radians(self.angulo))
            self.end = (self.xCanon2,self.yCanon2)

    #funcion para mover el canon del tanque    
    def moveCannon(self,temp):
        self.actualizar(self.LoR)
        
        if 90 > self.angulo:
            keys1 = pygame.key.get_pressed()
            if keys1[pygame.K_UP]:

                self.angulo += 1
                self.surface.blit(temp[0],(0,0))
                pygame.draw.line(self.surface,self.color,(self.xCanon1, self.yCanon1), (self.xCanon2, self.yCanon2), 4)
                
        if 0 < self.angulo:
            keys1 = pygame.key.get_pressed()        
            if keys1[pygame.K_DOWN]:
                    #("algo abajo")
                    self.angulo -= 1
                    self.surface.blit(temp[0],(0,0))
                    pygame.draw.line(self.surface,self.color,(self.xCanon1, self.yCanon1), (self.xCanon2, self.yCanon2), 4)

    # funcion con hitbox del tanque              
    def hitBox(self):
        hitboxPoints = []
        hitboxInitialX=self.x-10
        hitboxInitialY=self.y-4
        hitboxWidth = 70
        hitboxHeight = 30

        for i in range(hitboxWidth):
            for j in range(hitboxHeight):
                hitboxPoints.append((hitboxInitialX + i, hitboxInitialY + j))

        ##(hitboxPoints[0])
        return hitboxPoints
    # def chooseAmmo(self):
    #     for event in pygame.event.get():
    #          if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_1:
    #                 #(1)
    #             if event.key == pygame.K_2:
    #                 #(2)
    #             if event.key == pygame.K_3:
    #                 #(3)
              
    def getAngle(self):
        
        return self.angulo
    
    #funcion para obtener la vida del tanque
    def getHeath(self):
        return self.health
    
    #funcion para restar vida al tanque
    def loseHealth(self, type):
        if type == 1:
            self.health -= 50
        elif type == 2:
            self.health -= 40
        elif type == 3:
            self.health -= 30
        return self.health
         