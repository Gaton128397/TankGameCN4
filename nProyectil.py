import math,pygame,params, drawFunctions, nTerrain, nTank, random
from functions import *
g = 100
FPS = 60
def cargarProyectil(surf, imagen, proporcionX, proporcionY, posicion):
    imagen_cargada = pygame.image.load(imagen)
    imagen_escalada = pygame.transform.scale(imagen_cargada, (surf.get_width()*proporcionX, surf.get_height()*proporcionY))
    surf.blit(imagen_escalada, (posicion))
class Projectile():
    def __init__(self, position, typeBullet,power, theta,window):
        super(Projectile, self).__init__()
        #('se crea')
        self.typeBullet = typeBullet
        self.quantity = 0
        self.dmg = 0
        self.surf = pygame.Surface((params.WIDTH*0.05,params.HEIGHT*0.07))
        self.alphaColor = (255,0,255)
        self.surf.fill(self.alphaColor)
        self.surf.set_alpha()
        self.surf.set_colorkey(self.alphaColor)
        cargarProyectil(self.surf,"imgs/projectile1.png",1,1,(0,0))
        pygame.draw.circle(self.surf, (0,0,0), (int(self.surf.get_width()/2),int(self.surf.get_height()/2)), 2)
        self.power = power
        self.size = 0
        self.explosionArea = 0
        if self.typeBullet == 1: #105mm
            self.color = 'green'
            self.size = 15
            self.quantity = 3
            self.dmg = 50
        elif self.typeBullet == 2: #80mm
            self.color = 'blue'
            self.size = 8
            self.quantity = 10
            self.dmg = 40
        elif self.typeBullet == 3: #60mm
            self.color = 'red'
            self.size = 6
            self.quantity = 3
            self.dmg = 30
        elif self.typeBullet == 5: #no quedan
            self.size = 0
            #('endgame')
            #('no hay mas')
        else: #standard 60mm
            self.size = 6
            self.quantity = 3
            self.dmg = 30
            self.explosionArea = self.size*2 - self.size/2
        self.origin = (position[0],position[1])

        self.theta = toRadian(abs(theta))

        self.x, self.y = position[0], position[1]

        # self.color = 'blue'

        self.ch = 0
        if (theta >90):
            self.dx = -1
        else:
            self.dx = 1

        self.f = self.getTrajectory()

        self.range = self.x + abs(self.getRange())
        self.win = window
        self.path = []
        self.oldPath = []
        self.hit = False
        self.hitYourself = False

    def timeOfFlight(self):
        return round((2 * self.power * math.sin(self.theta)) / g, 2)

    def getRange(self):

        range_ = ((self.power ** 2) * 2 * math.sin(self.theta) * math.cos(self.theta)) / g
        return round(range_, 2)

    def getMaxHeight(self):

        h = ((self.power ** 2) * (math.sin(self.theta)) ** 2) / (2 * g)
        return round(h, 2)

    def getTrajectory(self):
        
        return round(g /  (2 * (self.power ** 2) * (math.cos(self.theta) ** 2)), 4) 

    def getProjectilePos(self, x):

        return x * math.tan(self.theta) - self.f * x ** 2
    
    def shoot(self,matriz,puntosTerreno):
        clock = pygame.time.Clock()
        self.yNew = self.y-self.ch
        puntox = int(self.surf.get_width()/2)
        puntoy = int(self.surf.get_height()/2)
        self.x += 10
        while (self.x >0 and self.x < params.WIDTH):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
            self.x += self.dx 
            self.ch = self.getProjectilePos(self.x - self.origin[0])
            self.yNew = self.y-self.ch
            print(int(self.x),int(self.yNew))
            self.win.blit(matriz[0],(0,0))
            self.win.blit(matriz[1],(0,0))
            self.win.blit(self.surf,(int(self.x),int(self.yNew)))
            if (int(self.x+puntox),int(self.yNew+puntoy)) in puntosTerreno:
                return (int(self.x+puntox),int(self.yNew+puntoy))
            clock.tick(200)
            pygame.display.update()
        pygame.display.update()
        print("hola")
        
def game():
    run = True
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    terrain = nTerrain.TerrenoVariado()
    bg = pygame.Surface((params.WIDTH, params.HEIGHT))
    drawFunctions.backgroundDraw(bg)
    listajugador = []
    for i in range(1):
        listajugador.append(nTank.Tank(300,(255,0,0),window))
    matriz = []
    matriz.append(bg)
    matriz.append(terrain.surfTerrain)
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            elif pygame.mouse.get_pressed()[0]:
                print(pygame.mouse.get_pos())
        bullet = Projectile((100,10),1,random.randint(1,100),60,window)
        terrain.updateImpact(bullet.shoot(matriz,terrain.getDiccionary()),100,listajugador)
        window.blit(matriz[0],(0,0))
        window.blit(matriz[1],(0,0))
        pygame.display.update()
game()