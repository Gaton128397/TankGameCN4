import pygame,math,random,drawFunctions
import numpy as np

class TerrenoVariado:
    def __init__(self, window, width, height):
        self.window = window
        self.width = width
        self.height = height
        self.num_points = 15
        self.points = []
        self.yPoints = []

        pygame.init()
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Terreno Variado")

    #funcion para interpolar los puntos
    def interpolate(self, x1, y1, x2, y2, x):
        return y1 + ((y2 - y1) / (x2 - x1)) * (x - x1)

    def getTerrain(self):
        for i in range(self.num_points):
            x = int(i * (self.width / (self.num_points - 1)))
            y = random.randint(self.height // 5, self.height - 200)
            if 0 <= x <= 1300:
                self.points.append((x, y))
                self.yPoints.append(y)


        for x in range(0, 1301):
            if not any(point[0] == x for point in self.points):
                # encontrar los puntos mas cercanos
                for i in range(len(self.points) - 1):
                    if self.points[i][0] < x < self.points[i+1][0]:
                        x1, y1 = self.points[i]
                        x2, y2 = self.points[i+1]
                        break

                # interpolar valor de y en los puntos faltantes
                y = self.interpolate(x1, y1, x2, y2, x)
                self.points.append((x, int(y)))
                self.yPoints.append(int(y))
            #print(self.points[x])

    def drawTerrain(self):
        surf = self.window.copy()
        drawFunctions.backgroundDraw(surf)
        
        x_interp = np.linspace(0, self.width, 100)
        y_interp = np.interp(x_interp, [point[0] for point in self.points], [point[1] for point in self.points])
        points_interp = [(int(x), int(y)) for x, y in zip(x_interp, y_interp)]
        #self.points = points_interp

        pygame.draw.polygon(surf, (255, 213, 158), [(0, self.height)] + points_interp + [(self.width, self.height)])
        pygame.draw.lines(surf, (139, 69, 19), False, points_interp, 5)
        return surf
        #pygame.display.update()

    def getPoints(self):
        return self.points

    def yPoint(self):
        return self.yPoints

    def restart(self):
        self.points = []  # Limpia la lista de puntos del terreno
        self.yPoints = []  # Limpia la lista de valores de y
        self.getTerrain()  # Genera un nuevo terreno