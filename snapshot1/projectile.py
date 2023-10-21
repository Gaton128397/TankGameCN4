import math,pygame,time
from functions import *
g = 9.8
FPS = 60

class Projectile():
    def __init__(self, position, typeBullet,power, theta,window):
        super(Projectile, self).__init__()

        self.typeBullet = typeBullet
        self.quantity = 0
        self.dmg = 0
        self.power = power
        self.size = 0
        if self.typeBullet == 1: #105mm
            self.size = 10.5
            self.quantity = 3
            self.dmg = 50
        elif self.typeBullet == 2: #80mm
            self.size = 8
            self.quantity = 10
            self.dmg = 40
        elif self.typeBullet == 2: #60mm
            self.size = 6
            self.quantity = 3
            self.dmg = 30
        else: #standard 60mm
            self.size = 6
            self.quantity = 3
            self.dmg = 30
        



        self.origin = (position[0],position[1])


        self.theta = toRadian(abs(theta))

        self.x, self.y = position[0], position[1]

        self.color = 'blue'

        self.ch = 0
        if (theta >90):
            self.dx = -0.4
        else:
            self.dx = 0.4


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
    
    def shoot(self,terrainPoints,selfhitboxPts,otherHitboxPoints):
        self.yNew = self.y-self.ch

        while (self.x >0 and self.x <= 1300) and (self.yNew > -2000 and self.yNew <terrainPoints[int(self.x)][1]-3) and not self.hit:
            if(self.x >= otherHitboxPoints[0][0]  and self.x <=otherHitboxPoints[len(otherHitboxPoints)-1][0]):
                if(self.yNew >= otherHitboxPoints[0][1]  and self.yNew <=otherHitboxPoints[len(otherHitboxPoints)-1][1]):
                    #print("hit!")
                    self.hit = True
            if(self.x >= selfhitboxPts[0][0]  and self.x <=selfhitboxPts[len(selfhitboxPts)-1][0]):
                if(self.yNew >= selfhitboxPts[0][1]  and self.yNew <=selfhitboxPts[len(selfhitboxPts)-1][1]):
                    #print("hit!")
                    self.hitYourself = True
            self.x += self.dx 
            self.ch = self.getProjectilePos(self.x - self.origin[0])
            self.path.append((self.x, self.y-self.ch))
            self.yNew = self.y-self.ch
            self.path = self.path[-50:]
            pygame.draw.circle(self.win, 'lightblue', self.path[0], self.size-1)
            pygame.draw.circle(self.win, 'darkgrey', self.path[-1], self.size)
            pygame.draw.circle(self.win, 'black', self.path[-1], self.size-2)
            pygame.display.update()
    
        
    def delete(self,terrainPoints,selfhitboxPts,otherHitboxPoints):
        time.sleep(0.01)
        self.yNew = self.y-self.ch
        collided = False
        while (self.x >0 and self.x <= 1300) and (self.yNew > -2000 and self.yNew <terrainPoints[int(self.x)][1]-3) and not self.hit:
            if(self.x >= otherHitboxPoints[0][0]  and self.x <=otherHitboxPoints[len(otherHitboxPoints)-1][0]):
                if(self.yNew >= otherHitboxPoints[0][1]  and self.yNew <=otherHitboxPoints[len(otherHitboxPoints)-1][1]):
                    #print("hit!")
                    collide = True
            if(self.x >= selfhitboxPts[0][0]  and self.x <=selfhitboxPts[len(selfhitboxPts)-1][0]):
                if(self.yNew >= selfhitboxPts[0][1]  and self.yNew <=selfhitboxPts[len(selfhitboxPts)-1][1]):
                    #print("hit!")
                    collide = True
            
            
            
            self.x += self.dx
            self.ch = self.getProjectilePos(self.x - self.origin[0])
            self.path.append((self.x, self.y-self.ch))
            self.yNew = self.y-self.ch
            self.path = self.path[-50:]
                
            pygame.draw.circle(self.win, 'lightblue', self.path[-1], self.size)
            pygame.display.update()
        return True
    
    def getBulletPosition(self):
        return(self.x,self.yNew)
    
    def returnHit(self):
        if self.hitYourself == True:
            return 2
        elif self.hit == True:
            return 1
        else:
            return 0
def game():
    run = True
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((800,600))
    window.fill('lightblue')

    bullet = Projectile((100,100),50,45,window)
    bullet.shoot()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
        clock.tick(60)
        pygame.display.update()
# game()

