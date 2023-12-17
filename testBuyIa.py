from random import randint
import crearItems
params = ''
class Player:
    def __init__(self,ia):
        self.money = 10000
        self.health = 0
        self.dmg = 0
        self.shield = 0
        self.bigStone = 0
        self.smallStone = 0
        self.mediumStone = 0
        self.inventory=[self.shield,self.dmg,self.health,self.bigStone,self.mediumStone,self.smallStone]
        self.points = 0
        self.kills = 0
        self.deaths = 0
        self.tanque = None
        self.selfKill = False
        self.ia = ia
        
        self.kda = [0,0]#indice 0 kills, indice 1 deaths
        self.generalkda = [0,0]#indice 0 points, indice 1 kills, indice 2 deaths
        
    def asignTank(self,tank):
        self.tanque = tank
        
    def returnKDA(self):
        return self.kda
    
def createItems():
    '''CREARITEMS'''
    shield = crearItems.item(0,'shield','reduce daño (1 uso)',2500,'shield')
    dmg = crearItems.item(1,'damage','+10 daño',100,'shield')
    health = crearItems.item(2,'health','+10 vida',100,'shield')
    bigStone = crearItems.item(3,'Big Projectile','piedra grande',4000,'shield')
    mediumStone = crearItems.item(4,"Medium Projectile",'piedra chica',2500,'shield')
    smallStone = crearItems.item(5,'Small Projectile','piedra mediana',1000,'shield')
    return [shield,dmg,health,bigStone,mediumStone,smallStone]    

def buyItemIA(listaItems,player):
    gastado = 0
    while player.money > 0:
        item = listaItems[randint(0,5)]
        if player.money >= item.precio:
            if item.ID == 0: 
                #maximo de 1 escudo 
                if player.inventory[item.ID] < 1:
                    player.inventory[item.ID] +=1
                    player.money -= item.precio  
                    gastado +=item.precio
                    print('item comprado:',item.nombre)
                    print('dinero gastado:',gastado)
                else:
                    player.inventory[item.ID] = 1

            elif item.ID == 2:
                player.money = player.money
            elif item.ID == 1 and player.inventory[item.ID]  ==10 and player.money<1000:
                #en caso de que ya haya 10 de dano y el dinero sea menor que 1000, no se podra restar y entra en un ciclo infinito, con esto se evita
                print('dinero jugador:',player.money)
                break
            else:
                if player.inventory[item.ID] < 10: 
                    #maximo de 10 de cada item
                    player.inventory[item.ID] +=1
                    player.money -= item.precio
                    gastado +=item.precio
                    print('item comprado:',item.nombre)
                    print('dinero gastado:',gastado)
ia = Player(True)
buyItemIA(createItems(),ia)
print(ia.inventory)