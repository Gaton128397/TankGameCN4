import pygame, sys, math, random
from functions import *

class Tank:
    def __init__(self,position, color,LoR,surface):

        self.health = 100


        self.x = position[0] - 15
        self.y = position[1] - 25
        self.width = 50
        self.height = 20
        self.color = color

        self.origin = (position[0] + 25, position[1] - 6.5)

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
    def draw_tank(self,color):

        pygame.draw.rect(self.surface, color, (self.x, self.y, self.width, self.height)) #rectangulo inicial
        pygame.draw.line(self.surface, color, (self.xCanon1, self.yCanon1), (self.xCanon2, self.yCanon2), 4) #cañon

        pygame.draw.rect(self.surface, color, (self.x + self.width/4, self.y - self.height/5, self.width/2, self.height/2)) #circunferencia de la izquierda
        
        pygame.draw.circle(self.surface, color, ((self.x, self.y + self.height/2)), self.height/2) #circunferencia de la derecha
        
        pygame.draw.circle(self.surface, color, ((self.x + self.width, self.y + self.height/2)), self.height/2) #rectangulo donde estara el cañon
        

    def actualizar(self,a):
            
            if self.LoR == 0:
                a = -1

            self.xCanon2 = self.xCanon1 + a*self.longitud * math.cos(math.radians(self.angulo))
            self.yCanon2 = self.yCanon1 - self.longitud * math.sin(math.radians(self.angulo))
            self.end = (self.xCanon2,self.yCanon2)
    def moveCannon(self):
        self.actualizar(self.LoR)
        
        keys = pygame.key.get_pressed()
        if 90 > self.angulo:
            if keys[pygame.K_UP]:
                
                self.angulo += 1

                pygame.draw.line(self.surface, 'lightblue', (self.xCanon1, self.yCanon1), (self.xCanon2, self.yCanon2), 6)
                pygame.draw.line(self.surface,self.color,(self.xCanon1, self.yCanon1), (self.xCanon2, self.yCanon2), 4)
                pygame.display.update()

        if 0 < self.angulo:        
            if keys[pygame.K_DOWN]:
                    self.angulo -= 1
                    pygame.draw.line(self.surface, 'lightblue', (self.xCanon1, self.yCanon1), (self.xCanon2, self.yCanon2), 6)
                    pygame.draw.line(self.surface,self.color,(self.xCanon1, self.yCanon1), (self.xCanon2, self.yCanon2), 4)
                    pygame.display.update()

        return (self.end)
    def hitBox(self):
        hitboxPoints = []
        hitboxInitialX=self.x-10
        hitboxInitialY=self.y-4
        hitboxWidth = 70
        hitboxHeight = 30

        for i in range(hitboxWidth):
            for j in range(hitboxHeight):
                hitboxPoints.append((hitboxInitialX + i, hitboxInitialY + j))

        #print(hitboxPoints[0])
        return hitboxPoints
    
    def getAngle(self):
        
        return self.angulo

