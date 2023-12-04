import pygame,math,random, params
import numpy as np

class TerrenoVariado:
    def __init__(self,  width, height):
        self.surfTerrain = pygame.Surface((params.WIDTH,params.HEIGHT))
        self.width = width
        self.height = height
        self.num_points = 15
        self.points = []
        self.yPoints = []
        self.hitPoints = {}
        
        
        for i in range(self.num_points):
            x = int(i * (self.width / (self.num_points - 1)))
            y = random.randint(self.height // 5, self.height - 200)
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
        
    def updateImpact(self,pos,radius):
        # Dibuja el círculo en la superficie
        pygame.draw.circle(self.surfTerrain, (255, 0, 255), pos, radius)
        # Actualiza la hitbox
        for i in range(pos[0] - radius, pos[0] + radius):
            for j in range(pos[1] - radius, pos[1] + radius):
                if (i - pos[0]) ** 2 + (j - pos[1]) ** 2 <= radius ** 2:
                    if(((i, j)) in self.hitPoints):
                        del self.hitPoints[(i, j)]
        
    #funcion para interpolar los puntos
    def interpolate(self, x1, y1, x2, y2, x):
        return y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)
    
    # Genera el terreno
    def drawTerrain(self):
        self.surfTerrain = pygame.Surface((self.width,self.height))
        self.surfTerrain.fill((255,0,255))
        
        x_interp = np.linspace(0, self.width, 100)
        y_interp = np.interp(x_interp, [point[0] for point in self.points], [point[1] for point in self.points])
        points_interp = [(int(x), int(y)) for x, y in zip(x_interp, y_interp)]
        #self.points = points_interp

        pygame.draw.polygon(self.surfTerrain, (255, 213, 158), [(0, self.height)] + points_interp + [(self.width, self.height)])
        pygame.draw.lines(self.surfTerrain, (139, 69, 19), False, points_interp, 5)
        self.surfTerrain.set_alpha()
        self.surfTerrain.set_colorkey((255,0,255))
        
        #pygame.display.update()
    # Devuelve los puntos del terreno
    
    def getDiccionary(self):
        return self.hitPoints
    
    def getPoints(self):
        return self.points
    
    # Devuelve los valores de y
    def yPoint(self):

        return self.yPoints
    # Reinicia el terreno
    def restart(self):
        self.points = []  # Limpia la lista de puntos del terreno
        self.yPoints = []  # Limpia la lista de valores de y
        self.getTerrain()  # Genera un nuevo terreno