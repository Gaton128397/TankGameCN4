import pygame,math,random,drawFunctions, params, playerPhysics, functions
import numpy as np

class TerrenoVariado:
    def __init__(self):
        self.surfTerrain = pygame.Surface((params.WIDTH,params.HEIGHT))
        self.num_points = 15
        self.points = []
        self.yPoints = []
        self.hitPoints = {}
        
        
        for i in range(self.num_points):
            x = int(i * (params.WIDTH / (self.num_points - 1)))
            y = random.randint(params.HEIGHT // 5, params.HEIGHT - 200)
            if 0 <= x <= params.WIDTH:
                self.points.append([x, y])
                self.yPoints.append([y])

        # interpolar los puntos faltantes
        for x in range(0, params.WIDTH+1):
            if not any(point[0] == x for point in self.points):
                # encontrar los puntos mas cercanos
                for i in range(len(self.points) - 1):
                    if self.points[i][0] < x < self.points[i+1][0]:
                        x1, y1 = self.points[i]
                        x2, y2 = self.points[i+1]
                        break

                # interpolar valor de y en los puntos faltantes
                y = self.interpolate(x1, y1, x2, y2, x)
                self.points.append([x, int(y)])
                self.yPoints.append([int(y)])#????????????????????????
        
        self.points.sort()
        print(self.points[0][1])
        
        for i in range(params.WIDTH):
            #print("hola")
            for j in range(self.points[i][1],params.WIDTH+1):
                self.hitPoints[(i,j)]=True
        self.drawTerrain()
        
    def updateImpact(self,pos,proyectil,lista):
        pygame.draw.circle(self.surfTerrain, (255, 0, 255), pos, proyectil.blastRadius)
        tanquesDañadosIzquierda = {}
        tanquesDañadosDerecha= {}
        puntosImpactoIzquierda = {}
        puntosImpactoDerecha = {}
        for i in range(pos[0] - proyectil.blastRadius, pos[0] + proyectil.blastRadius):
            for j in range(pos[1] - proyectil.blastRadius, pos[1] + proyectil.blastRadius):
                if (i - pos[0]) ** 2 + (j - pos[1]) ** 2 <= proyectil.blastRadius ** 2:
                    if(((i, j)) in self.hitPoints):
                        del self.hitPoints[(i, j)]
                    for z in range(len(lista)):
                        if i < pos[0]:
                            if (i,j) in lista[z].hitBox:
                                tanquesDañadosIzquierda[z] = True
                                puntosImpactoIzquierda[z] = (i, j)
                        if i > pos[0]:
                            if (i,j) in lista[z].hitBox:
                                if z not in tanquesDañadosIzquierda:
                                    tanquesDañadosDerecha[z] = True
                                    if z not in puntosImpactoDerecha:
                                        puntosImpactoDerecha[z] = (i, j) 
                    #if(((i, j)) in self.hitPoints):
                    #    del self.hitPoints[(i, j)]
       
        # Imprime los puntos de impacto
        
        print("Puntos de impacto en la izquierda:")
        for z, punto in puntosImpactoIzquierda.items():
            print(f"Tanque {z}: {punto}")
            distancia = functions.calcular_distancia(pos, punto)
            dmg = int(functions.calcularDMG(distancia, proyectil.DMG, proyectil.blastRadius,proyectil.typeBullet))
            #dano = self.calcularDMG(distancia, 50)
            lista[z].actualizarVida(dmg)
            print(f"El tanque {z} recibe un daño de {dmg}")
        print("Puntos de impacto en la derecha:")
        for z, punto in puntosImpactoDerecha.items():
            distancia = functions.calcular_distancia(pos, punto)
            dmg = int(functions.calcularDMG(distancia, proyectil.DMG, proyectil.blastRadius,proyectil.typeBullet))
            lista[z].actualizarVida(dmg)
            print(distancia)
            print(f"El tanque {z} recibe un daño de {dmg}")
    
    def testupdateImpact(self,pos,radius,lista):
        print(radius)
        pygame.draw.circle(self.surfTerrain, (255, 0, 255), pos, radius)
        tanquesDañadosIzquierda = {}
        tanquesDañadosDerecha= {}
        puntosImpactoIzquierda = {}
        puntosImpactoDerecha = {}
        for i in range(pos[0] - radius, pos[0] + radius):
            for j in range(pos[1] - radius, pos[1] + radius):
                if (i - pos[0]) ** 2 + (j - pos[1]) ** 2 <= radius ** 2:
                    if(((i, j)) in self.hitPoints):
                        del self.hitPoints[(i, j)]
                    for z in range(len(lista)):
                        if i < pos[0]:
                            if (i,j) in lista[z].hitBox:
                                tanquesDañadosIzquierda[z] = True
                                puntosImpactoIzquierda[z] = (i, j)
                        if i > pos[0]:
                            if (i,j) in lista[z].hitBox:
                                if z not in tanquesDañadosIzquierda:
                                    tanquesDañadosDerecha[z] = True
                                    if z not in puntosImpactoDerecha:
                                        puntosImpactoDerecha[z] = (i, j) 
                    #if(((i, j)) in self.hitPoints):
                    #    del self.hitPoints[(i, j)]
       
        # Imprime los puntos de impacto
        
        print("Puntos de impacto en la izquierda:")
        for z, punto in puntosImpactoIzquierda.items():
            print(f"Tanque {z}: {punto}")
            distancia = functions.calcular_distancia(pos, punto)
            dmg = int(functions.calcularDMG(distancia, 50, radius,1))
            #dano = self.calcularDMG(distancia, 50)
            lista[z].actualizarVida(dmg)
            print(f"El tanque {z} recibe un daño de {dmg}")
        print("Puntos de impacto en la derecha:")
        for z, punto in puntosImpactoDerecha.items():
            distancia = functions.calcular_distancia(pos, punto)
            dmg = int(functions.calcularDMG(distancia, 50, radius,1))
            lista[z].actualizarVida(dmg)
            print(distancia)
            print(f"El tanque {z} recibe un daño de {dmg}")
    
    def interpolate(self, x1, y1, x2, y2, x):
        return y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)
    def interpolate(self, x1, y1, x2, y2, x):
        return y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)
    
    # Genera el terreno
    def drawTerrain(self):
        self.surfTerrain = pygame.Surface((params.WIDTH,params.HEIGHT))
        self.surfTerrain.fill((255,0,255))
        
        x_interp = np.linspace(0, params.WIDTH, 100)
        y_interp = np.interp(x_interp, [point[0] for point in self.points], [point[1] for point in self.points])
        points_interp = [(int(x), int(y)) for x, y in zip(x_interp, y_interp)]
        #self.points = points_interp

        pygame.draw.polygon(self.surfTerrain, (255, 213, 158), [(0, params.HEIGHT)] + points_interp + [(params.WIDTH, params.HEIGHT)])
        pygame.draw.lines(self.surfTerrain, (139, 69, 19), False, points_interp, 5)
        self.surfTerrain.set_alpha()
        self.surfTerrain.set_colorkey((255,0,255))
        

    def getDiccionary(self):
        return self.hitPoints
    
    def getPoints(self):
        return self.points
    
    # Devuelve los valores de y
    def yPoint(self):

        return self.yPoints
    # Reinicia el terreno
