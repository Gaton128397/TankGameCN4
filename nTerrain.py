import pygame,math,random,drawFunctions, params, playerPhysics, functions
import numpy as np

class TerrenoVariado:
    def __init__(self,color):
        self.WIDTH = params.size*16
        self.HEIGHT = params.size*9
        self.surfTerrain = pygame.Surface((self.WIDTH,self.HEIGHT))
        self.num_points = 15
        self.points = []
        self.yPoints = []
        self.hitPoints = {}
        self.color = color
        
        for i in range(self.num_points):
            x = int(i * (self.WIDTH / (self.num_points - 1)))
            y = random.randint(self.HEIGHT // 5, self.HEIGHT - 200)
            if 0 <= x <= self.WIDTH:
                self.points.append([x, y])
                self.yPoints.append([y])

        # interpolar los puntos faltantes
        for x in range(0, self.WIDTH+1):
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
                self.yPoints.append([int(y)])
        
        self.points.sort()
        
        for i in range(self.WIDTH):
            for j in range(self.points[i][1],self.WIDTH+1):
                self.hitPoints[(i,j)]=True
        
        self.drawTerrain()

    def updateImpact(self,position,proyectil,lista,listaPlayers,jugadoresDerrotados,turno):
        pos = []
        if position[0] < 0:
            pos.append(0)
        elif position[0] > self.WIDTH:
            pos.append(self.WIDTH)
        else:
            pos.append(position[0])
        if position[1] < 0:
            pos.append(0)
        elif position[1] > self.HEIGHT:
            pos.append(self.HEIGHT)
        else:
            pos.append(position[1])
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
        
        # Imprime los puntos de impacto
        
        for z, punto in puntosImpactoIzquierda.items():
            distancia = functions.calcular_distancia(pos, punto)
            dmg = int(functions.calcularDMG(distancia, proyectil.DMG, proyectil.blastRadius,proyectil.typeBullet))
            if listaPlayers[lista[z].playerID].inventory[0] == 1:
                listaPlayers[lista[z].playerID].inventory[0] = 0
                dmg = dmg*0.60
            lista[z].actualizarVida(dmg)
            if lista[z].getVida() <= 0:
                jugadoresDerrotados.append(lista[z])
                if lista[z].playerID == lista[turno].playerID:
                    listaPlayers[lista[turno].playerID].selfKill = True
                    listaPlayers[lista[turno].playerID].kda[1] += 1
                else:
                    listaPlayers[lista[turno].playerID].kda[0] += 1
                    listaPlayers[lista[z].playerID].kda[1] += 1
                    
        for z, punto in puntosImpactoDerecha.items():
            distancia = functions.calcular_distancia(pos, punto)
            dmg = int(functions.calcularDMG(distancia, proyectil.DMG, proyectil.blastRadius,proyectil.typeBullet))
            if listaPlayers[lista[z].playerID].inventory[0] == 1:
                listaPlayers[lista[z].playerID].inventory[0] = 0
                dmg = dmg*0.60
            lista[z].actualizarVida(dmg)
            if lista[z].getVida() <= 0:
                jugadoresDerrotados.append(lista[z])
                if lista[z].playerID == lista[turno].playerID:
                    listaPlayers[lista[turno].playerID].selfKill = True
                    listaPlayers[lista[turno].playerID].kda[1] += 1
                else:
                    listaPlayers[lista[turno].playerID].kda[0] += 1
                    listaPlayers[lista[z].playerID].kda[1] += 1
                    
    
    def interpolate(self, x1, y1, x2, y2, x):
        return y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)
    
    # Genera el terreno
    def drawTerrain(self):
        self.surfTerrain = pygame.Surface((self.WIDTH,self.HEIGHT))
        self.surfTerrain.fill((255,0,255))
        
        x_interp = np.linspace(0, self.WIDTH, 100)
        y_interp = np.interp(x_interp, [point[0] for point in self.points], [point[1] for point in self.points])
        points_interp = [(int(x), int(y)) for x, y in zip(x_interp, y_interp)]

        pygame.draw.polygon(self.surfTerrain, (self.color), [(0, self.HEIGHT)] + points_interp + [(self.WIDTH, self.HEIGHT)])
        pygame.draw.lines(self.surfTerrain, (self.color), False, points_interp, 5)
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
