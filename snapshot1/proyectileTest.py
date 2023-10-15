import math,pygame,time
from functions import *

g = 9.8
FPS = 60

class Projectile():
    def __init__(self, position,power, theta,radio,window):
        super(Projectile, self).__init__()

        self.origin = (position[0],position[1])

        self.power = power

        self.theta = toRadian(abs(theta))

        self.x, self.y = position[0], position[1]

        self.color = 'blue'

        self.ch = 0
        if (theta >90):
            self.dx = -0.4
        else:
            self.dx = 0.4


        self.f = self.getTrajectory()
        
        self.radio = radio
            
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
    
    def shoot(self):
        self.yNew = self.y-self.ch

        while (self.x +self.radio >0 and self.x <= 1300) and (self.yNew+self.radio > -2000 ):
            self.x += self.dx 
            self.ch = self.getProjectilePos(self.x - self.origin[0])
            self.path.append((self.x, self.y-self.ch))
            self.yNew = self.y-self.ch
            self.path = self.path[-50:]
            
            pygame.draw.circle(self.win, 'lightblue', self.path[0], self.radio+1)
            pygame.draw.circle(self.win, 'darkgrey', self.path[-1], self.radio+2)
            pygame.draw.circle(self.win, 'black', self.path[-1], self.radio)
            pygame.display.update()
    
        
    def delete(self,terrainPoints,selfhitboxPts,otherHitboxPoints):
        time.sleep(0.01)
        self.yNew = self.y-self.ch
        collided = False
        
        while (self.x+self.radio >0 and self.x + self.radio <= 1300) and (self.yNew + self.radio > -2000 and self.yNew + self.radio <terrainPoints[int(self.x)][1]-3) and not self.hit:
        
            if(self.x+self.radio >= otherHitboxPoints[0][0]  and self.x+self.radio <=otherHitboxPoints[len(otherHitboxPoints)-1][0]):
        
                if(self.yNew +self.radio>= otherHitboxPoints[0][1]  and self.yNew + self.radio <=otherHitboxPoints[len(otherHitboxPoints)-1][1]):
        
                    #print("hit!")
                    collide = True
        
            if(self.x +self.radio >= selfhitboxPts[0][0]  and self.x +self.radio <=selfhitboxPts[len(selfhitboxPts)-1][0]):
        
                if(self.yNew +self.radio>= selfhitboxPts[0][1]  and self.yNew +self.radio<=selfhitboxPts[len(selfhitboxPts)-1][1]):
        
                    #print("hit!")
                    collide = True

            self.x += self.dx 
            self.ch = self.getProjectilePos(self.x - self.origin[0])
            self.path.append((self.x, self.y-self.ch))
            self.yNew = self.y-self.ch
            self.path = self.path[-50:]
                
            pygame.draw.circle(self.win, 'lightblue', self.path[-1], self.radio+6)
            pygame.display.update()
        return True
    
    def getBulletPosition(self):
        return(self.x,self.yNew)
    
    def returnHit(self):
        if self.hitYourself == True:
            self.hit = False
            return 2
            
        elif self.hit == True:
            self.hitYourself = False
            return 1
        else:
            return 0
def game():
    run = True
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((1366,900))
    window.fill('lightblue')
    bullet = Projectile((100,500),100,45,5,window)
    bullet.shoot()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
        clock.tick(5)
        pygame.display.update()
game()

