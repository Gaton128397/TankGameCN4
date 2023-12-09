class Player:
    def init(self):
        self.money = 10000
        self.dmg = True
        self.shield = True
        self.bigStone = 3
        self.smallStone = 3
        self.mediumStone = 10
        self.inventory=[self.shield,self.dmg,self.health,self.bigStone,self.mediumStone,self.smallStone]

        self.points = 0
        self.kills = 0
        self.deaths = 0
        
        self.tanque = None
        
    def asignTank(self,tank):
        self.tanque = tank