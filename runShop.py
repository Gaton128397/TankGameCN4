import pygame, sys,crearItems,params,player,time,functions
from button import Button
# from functions import checkResize
pygame.init()
#variables
# jugadorTest = player.Player()
# jugadorTest2 = player.Player()
# jugadorTest3 = player.Player()
# jugadorTest4 = player.Player()
# listaJugadores = [jugadorTest,jugadorTest2,jugadorTest3,jugadorTest4]
class Shop:
    def __init__(self):

        self.tiendaIni = pygame.image.load('Pantallas/shopIni.png')
        self.tiendaMid = pygame.image.load('Pantallas/shopMid.png')
        self.tiendaEnd = pygame.image.load('Pantallas/shopFin.png')

        self.actualItem = None

    '''METHODS'''
    def createItems(self):
        '''CREARITEMS'''
        shield = crearItems.item(0,'shield','+1 escudo, reduce dmg a la mitad pero se rompe',100,params.shield)
        dmg = crearItems.item(1,'damage','+10 dmg',100,params.dmg)
        health = crearItems.item(2,'health','+10 vida',100,params.health)
        bigStone = crearItems.item(3,'Big Projectile','piedra grande',100,params.bigStone)
        mediumStone = crearItems.item(4,"Medium Projectile",'piedra chica',100,params.smallStone)
        smallStone = crearItems.item(5,'Small Projectile','piedra mediana',100,params.mediumStone)
        # print(shield.nombre)
        return [shield,dmg,health,bigStone,mediumStone,smallStone]
    
    def buttons(self):
        buttons = [ 
            Button(0.78, 0.85, 0.2, 0.1,'Next'), #siguiente
            Button(0.015, 0.85, 0.2, 0.1,'Back'), #volver


            Button(0.330, 0.78, 0.09, 0.1,'Buy'), #comprar
            Button(0.585, 0.78, 0.09, 0.1,'Sell'), #vender

            Button(0.06, 0.22, 0.11, 0.15,self.createItems()[0]), #escudo
            Button(0.22, 0.22, 0.11, 0.15,self.createItems()[1]), #espada
            Button(0.36, 0.22, 0.11, 0.15,self.createItems()[2]), #corazon
            Button(0.50, 0.22, 0.11, 0.15,self.createItems()[3]), #piedra grande
            Button(0.66, 0.22, 0.11, 0.15,self.createItems()[4]), #piedra pequena
            Button(0.80, 0.22, 0.11, 0.15,self.createItems()[5]) #piedra mediana
            ]
        
        return buttons

    def selectItem(self,item):
        self.actualItem = item

        nombre = pygame.font.Font(None, int(params.size*0.4))
        nombre = nombre.render(item.nombre, True, (0, 0, 0))

        descripcion = pygame.font.Font(None, int(params.size*0.4))
        descripcion = descripcion.render(item.descripcion, True, (0, 0, 0))
        
        precio = pygame.font.Font(None, int(params.size*0.4))
        precio = precio.render(str("precio: $"+str(item.precio)), True, (0, 0, 0))
        
        pygame.draw.rect(params.screen,(('#D6C6BC')),(params.size*4.38,params.size*3.73,params.size*7.27,params.size*3.25))
        item.resize()
        params.screen.blit(item.Icon,(params.size*16*0.46,params.size*9*0.42))
        params.screen.blit(nombre,(params.size*16*0.46,params.size*9*0.53))
        if item.nombre == 'shield':
            params.screen.blit(descripcion,(params.size*16*0.3,params.size*9*0.58))
        else:
            params.screen.blit(descripcion,(params.size*16*0.46,params.size*9*0.58))
        params.screen.blit(precio,(params.size*16*0.46,params.size*9*0.62))

    def showInventory(self,player):

        item1text = pygame.font.Font(None, int(params.size*0.4))
        item1text = item1text.render("x"+str(player.inventory[0]), True, (0, 0, 0))


        item2text = pygame.font.Font(None, int(params.size*0.4))
        item2text = item2text.render("x"+str(player.inventory[1]), True, (0, 0, 0))
        
        item3text = pygame.font.Font(None, int(params.size*0.4))
        item3text = item3text.render("x"+str(player.inventory[2]), True, (0, 0, 0))
        
        item4text = pygame.font.Font(None, int(params.size*0.4))
        item4text = item4text.render("x"+str(player.inventory[3]), True, (0, 0, 0))
        
        item5text = pygame.font.Font(None, int(params.size*0.4))
        item5text = item5text.render("x"+str(player.inventory[4]), True, (0, 0, 0))
        
        item6text = pygame.font.Font(None, int(params.size*0.4))
        item6text = item6text.render("x"+str(player.inventory[5]), True, (0, 0, 0))
        
        #borrar anterior
        pygame.draw.rect(params.screen,'white',(params.size*1,params.size*5,params.size*0.45,params.size*0.4))
        pygame.draw.rect(params.screen,'white',(params.size*1,params.size*5.8,params.size*0.45,params.size*0.4))
        pygame.draw.rect(params.screen,'white',(params.size*1,params.size*6.8,params.size*0.45,params.size*0.4))
        pygame.draw.rect(params.screen,'white',(params.size*2.75,params.size*5,params.size*0.45,params.size*0.4))
        pygame.draw.rect(params.screen,'white',(params.size*2.75,params.size*5.8,params.size*0.45,params.size*0.4))
        pygame.draw.rect(params.screen,'white',(params.size*2.75,params.size*6.8,params.size*0.45,params.size*0.4))
        
        #escribir nuevo
        params.screen.blit(item1text,(params.size*1,params.size*5))
        params.screen.blit(item2text,(params.size*1,params.size*6.8))
        params.screen.blit(item3text,(params.size*1,params.size*5.8))
        params.screen.blit(item6text,(params.size*2.75,params.size*5))
        params.screen.blit(item4text,(params.size*2.75,params.size*5.8))
        params.screen.blit(item5text,(params.size*2.75,params.size*6.8))

    def showStats(self,player):
        
        #texto stats
        healthText = pygame.font.Font(None, int(params.size*0.6))
        healthText = healthText.render(str(player.inventory[2]*10), True, (0, 0, 0))

        dmgText = pygame.font.Font(None, int(params.size*0.6))
        dmgText = dmgText.render(str(player.inventory[1]*10), True, (0, 0, 0))

        shieldText = pygame.font.Font(None, int(params.size*0.6))
        shieldText = shieldText.render(str(player.inventory[0]), True, (0, 0, 0))
        
        #borrar anterior
        pygame.draw.rect(params.screen,'white',(params.size*13.5,params.size*4.5,params.size*1.5,params.size*0.4))
        pygame.draw.rect(params.screen,'white',(params.size*13.5,params.size*5.5,params.size*1.5,params.size*0.4))
        pygame.draw.rect(params.screen,'white',(params.size*13.5,params.size*6.5,params.size*1.5,params.size*0.4))
        
        #escribir nuevo
        params.screen.blit(dmgText,(params.size*13.5,params.size*6.5))
        params.screen.blit(healthText,(params.size*13.5,params.size*5.5))
        params.screen.blit(shieldText,(params.size*13.5,params.size*4.5))

    def sellItem(self,item,player):
        if self.actualItem !=None:
            if player.inventory[item.ID] > 0:
                player.inventory[item.ID] -=1
                print(item.nombre)
                print("id",item.ID)
                print(player.inventory[item.ID])
                player.money += item.precio

    def buyItem(self,item,player):
        
        if self.actualItem !=None:
            if player.money >= item.precio:
                if item.ID == 0: #maximo de 1 escudo 
                    if player.inventory[item.ID] < 1:
                        player.inventory[item.ID] +=1
                        player.money -= item.precio
                    else:
                        player.inventory[item.ID] = 1
                else:
                    if player.inventory[item.ID] < 10: #maximo de 10 de cada item
                        player.inventory[item.ID] +=1
                        player.money -= item.precio

    def showMoney(self,player):
        showMoney = pygame.font.Font(None, int(params.size*0.6))
        showMoney = showMoney.render("$"+str(player.money), True, (229,202,0))
        pygame.draw.rect(params.screen,'white',(params.size*16*0.1,params.size*9*0.03,params.size*16*0.1,params.size*9*0.05))
        params.screen.blit(showMoney,(params.size*16*0.1,params.size*9*0.03))
        
    def openShop(self,playerList): #recibe una lista de jugadores
        actualImg = self.tiendaIni
        player = 0 #jugador actual
        running =True
        while running:
            
            if params.size == 120:
                screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            else:
                screen = pygame.display.set_mode((params.size*16, params.size*9))
            screen.blit(pygame.transform.scale(actualImg, (params.size*16,params.size*9)), (0, 0))
            # pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                #botones tienda
            # checkResize(event)
            for boton in self.buttons():
                time.sleep(0.005)
                if boton.check_click(event):
                    if boton.item == 'Buy':
                        self.buyItem(self.actualItem,playerList[player])
                    elif boton.item == 'Sell':
                        self.sellItem(self.actualItem,playerList[player])
                    elif boton.item == 'Back':
                        if player > 0:
                            player -= 1
                            self.actualItem = None
                        else:
                            player = len(playerList)-1
                    elif boton.item == 'Next':
                        if player == len(playerList)-1:
                            running = False
                        if player < len(playerList)-1:
                            player += 1
                            self.actualItem = None

                    else:
                        self.selectItem(boton.item)
                        self.actualItem = boton.item
            #dibujar tienda
            if player == 0:
                
                actualImg = self.tiendaIni
            elif player == len(playerList)-1:
                
                actualImg = self.tiendaEnd
            else:
                
                actualImg = self.tiendaMid


            
            if self.actualItem != None:
                self.selectItem(self.actualItem)
            self.showInventory(playerList[player])
            self.showStats(playerList[player])
            self.showMoney(playerList[player])
            pygame.display.update()
        return 12
# if __name__ == "__main__":
    # shop = Shop()
    # shop.openShop(listaJugadores)
