import pygame,sys,random
class Bot:
    def __init__(self, name):
        self.name = name
        self.health = 0
        self.damage = 0
        self.armor = 0
        self.bigStone = 0
        self.mediumStone = 0
        self.smallStone = 0
        
        self.stats = [self.health, self.damage, self.armor]
        self.inventory = [self.bigStone, self.mediumStone, self.smallStone]

    def buy(self):
        pass
    def chooseEnemy(self, enemies):
        enemy = random.randint(0, len(enemies)-1) #elige un enemigo al azar
        enemyPosition = enemy.Pos() #recibe el punto medio del enemigo, tambien podria crearse usando matrices
    
    def chooseProjectile(self):
        projectile = random.randint(0,len(self.inventory)-1) #elige un proyectil al azar
        return projectile
    
    def calculateTrajectory(self):
        power = random.randint(0,100)
        angle = random.randint(0,90)


    def shootingAlgorithm(self):
        positionPlayers = [1,2,3,4,5,6,7,"..."] #guarda la posicion del punto medio de los jugadores
