class Player:
    def __init__(self):
        self.money = 10000
        self.health = 0
        self.dmg = 0
        self.shield = 0
        self.bigStone = 3
        self.smallStone = 3
        self.mediumStone = 3
        self.inventory=[self.shield,self.dmg,self.health,self.bigStone,self.mediumStone,self.smallStone]
        self.points = 0
        self.kills = 0
        self.deaths = 0
        self.tanque = None
        self.selfKill = False
        self.ia = False
        
        self.kda = [0,0]#indice 0 kills, indice 1 deaths
        self.generalkda = [0,0]#indice 0 points, indice 1 kills, indice 2 deaths
        
    def asignTank(self,tank):
        self.tanque = tank
        
    def returnKDA(self):
        return self.kda