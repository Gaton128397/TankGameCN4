import pygame, sys,button,crearItems,params,player,time
pygame.init()
#variables
jugadorTest = player.Player()
jugadorTest2 = player.Player()
jugadorTest3 = player.Player()
jugadorTest4 = player.Player()
listaJugadores = [jugadorTest,jugadorTest2,jugadorTest3,jugadorTest4]
class Shop:
    def __init__(self):

        '''SCREEN'''
        self.width, self.height = params.size*16,params.size*9
        self.tiendaIni = params.shopIniImg
        self.tiendaMid = params.shopMidImg
        self.tiendaEnd = params.shopFinImg
        self.window = params.screen#pygame.display.set_mode((self.width, self.height))

        self.actualItem = None
        self.buttons = self.buttons()
    '''METHODS'''
    def createItems(self):
        '''CREARITEMS'''
        shield = crearItems.item('shield',0,'+1 escudo',100,params.shield)
        dmg = crearItems.item('dmg',1,'+10 dmg',100,params.dmg)
        health = crearItems.item('health',2,'+10 vida',100,params.health)
        bigStone = crearItems.item('big Stone',3,'piedra grande',4000,params.bigStone)
        mediumStone = crearItems.item('small Stone',4,'piedra chica',1000,params.smallStone)
        smallStone = crearItems.item('medium Stone',5,'piedra mediana',2500,params.mediumStone)
        return [shield,dmg,health,bigStone,mediumStone,smallStone]
    
    def buttons(self):
        x,width,height = params.size,params.size*16,params.size*9 
        crearitems = self.createItems()
        '''SHOP BUTTONS'''
        settingButton = button.Button((params.size*0.1,params.size*0.1,params.size*1.2,params.size*0.9),(0,255,0),'home',False)
        homeButton = button.Button((params.size*14.5,params.size*0.15,params.size*1.2,params.size*0.9),(255,0,0),'settings',False)
        buyButton = button.Button((params.size*5.3,params.size*7.05,params.size*1.15,params.size*0.8),(255,0,0),'buy',False)
        sellButton = button.Button((params.size*9.5,params.size*7,params.size*1.15,params.size*0.8),(255,0,0),'sell',False)
        nextButton = button.Button((params.size*12.5,params.size*7.5,params.size*3,params.size*1),(255,0,0),'next',False)
        previousButton = button.Button((params.size*0.3,params.size*7.7,params.size*2.9,params.size*0.85),(255,0,0),'previous',False)
        finishButton = button.Button((params.size*12.5,params.size*7.5,params.size*3,params.size*1.1),(255,0,255),'finish',False)

        '''CREARITEMS BUTTONS'''
        shieldButton = button.Button((params.size*1.4,params.size*2,params.size*0.9,params.size*1),(255,0,0),crearitems[0],False)
        dmgButton = button.Button((params.size*3.7,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),crearitems[1],False)
        healthButton = button.Button((params.size*6.1,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),crearitems[2],False)
        bigStoneButton = button.Button((params.size*8.8,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),crearitems[3],False)
        mediumStoneButton = button.Button((params.size*11,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),crearitems[4],False)
        smallStoneButton = button.Button((params.size*13.5,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),crearitems[5],False)


        buttons = [shieldButton,dmgButton,healthButton,bigStoneButton,mediumStoneButton,smallStoneButton,settingButton,homeButton,buyButton,sellButton,finishButton,previousButton]
        return buttons

    def selectItem(self,item):
        self.actualItem = item

        nombre = pygame.font.Font(None, int(params.size*0.4))
        nombre = nombre.render(item.nombre, True, (0, 0, 0))

        descripcion = pygame.font.Font(None, int(params.size*0.4))
        descripcion = descripcion.render(item.descripcion, True, (0, 0, 0))
        
        precio = pygame.font.Font(None, int(params.size*0.4))
        precio = precio.render(str("precio: $"+str(item.precio)), True, (0, 0, 0))
        
        pygame.draw.rect(self.window,((164, 164, 164)),(params.size*4.38,params.size*3.73,params.size*7.27,params.size*3.25))
        item.resize()
        self.window.blit(item.Icon,(params.size*16*0.46,params.size*9*0.42))
        self.window.blit(nombre,(params.size*16*0.46,params.size*9*0.53))
        self.window.blit(descripcion,(params.size*16*0.46,params.size*9*0.58))
        self.window.blit(precio,(params.size*16*0.46,params.size*9*0.62))

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
        pygame.draw.rect(self.window,'white',(params.size*1,params.size*5,params.size*0.45,params.size*0.4))
        pygame.draw.rect(self.window,'white',(params.size*1,params.size*5.8,params.size*0.45,params.size*0.4))
        pygame.draw.rect(self.window,'white',(params.size*1,params.size*6.8,params.size*0.45,params.size*0.4))
        pygame.draw.rect(self.window,'white',(params.size*2.75,params.size*5,params.size*0.45,params.size*0.4))
        pygame.draw.rect(self.window,'white',(params.size*2.75,params.size*5.8,params.size*0.45,params.size*0.4))
        pygame.draw.rect(self.window,'white',(params.size*2.75,params.size*6.8,params.size*0.45,params.size*0.4))
        
        #escribir nuevo
        self.window.blit(item1text,(params.size*1,params.size*5))
        self.window.blit(item2text,(params.size*1,params.size*6.8))
        self.window.blit(item3text,(params.size*1,params.size*5.8))
        self.window.blit(item6text,(params.size*2.75,params.size*5))
        self.window.blit(item4text,(params.size*2.75,params.size*5.8))
        self.window.blit(item5text,(params.size*2.75,params.size*6.8))

    def showStats(self,player):
        
        #texto stats
        healthText = pygame.font.Font(None, int(params.size*0.6))
        healthText = healthText.render(str(player.inventory[2]*10), True, (0, 0, 0))

        dmgText = pygame.font.Font(None, int(params.size*0.6))
        dmgText = dmgText.render(str(player.inventory[1]*10), True, (0, 0, 0))

        shieldText = pygame.font.Font(None, int(params.size*0.6))
        shieldText = shieldText.render(str(player.inventory[0]), True, (0, 0, 0))
        
        #borrar anterior
        pygame.draw.rect(self.window,'white',(params.size*13.5,params.size*4.5,params.size*1.5,params.size*0.4))
        pygame.draw.rect(self.window,'white',(params.size*13.5,params.size*5.5,params.size*1.5,params.size*0.4))
        pygame.draw.rect(self.window,'white',(params.size*13.5,params.size*6.5,params.size*1.5,params.size*0.4))
        
        #escribir nuevo
        self.window.blit(dmgText,(params.size*13.5,params.size*6.5))
        self.window.blit(healthText,(params.size*13.5,params.size*5.5))
        self.window.blit(shieldText,(params.size*13.5,params.size*4.5))

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
        pygame.draw.rect(self.window,'white',(params.size*16*0.1,params.size*9*0.03,params.size*16*0.1,params.size*9*0.05))
        self.window.blit(showMoney,(params.size*16*0.1,params.size*9*0.03))

    def openShop(self,playerList): #recibe una lista de jugadores
        actualImg = self.tiendaIni
        player = 0 #jugador actual
        running =True
        while running:
            
            params.screen.blit(pygame.transform.scale(actualImg, (params.size*16,params.size*9)), (0, 0))
            #events = pygame.event.get()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                #botones tienda
                for btn in self.buttons:
                    time.sleep(0.005)
                    if btn.check_click(event):
                        if btn.item == 'home':
                            running = False
                        elif btn.item == 'settings':
                            print('settings')
                        elif btn.item == 'buy':
                            self.buyItem(self.actualItem,playerList[player])
                        elif btn.item == 'sell':
                            self.sellItem(self.actualItem,playerList[player])

                        elif btn.item == 'previous':
                            if player > 0:
                                player -= 1
                                self.actualItem = None
                            else:
                                player = len(playerList)-1
                        elif btn.item == 'finish':
                            if player == len(playerList)-1:
                                running = False
                            if player < len(playerList)-1:
                                player += 1
                                self.actualItem = None

                        else:
                            self.selectItem(btn.item)
                            self.actualItem = btn.item
            #dibujar tienda
            if player == 0:
                
                actualImg = self.tiendaIni
            elif player == len(playerList)-1:
                
                actualImg = self.tiendaEnd
            else:
                
                actualImg = self.tiendaMid


            self.showInventory(playerList[player])
            self.showStats(playerList[player])
            self.showMoney(playerList[player])
            if self.actualItem != None:
                self.selectItem(self.actualItem)
            pygame.display.update()

#if __name__ == "__main__":
#     shop = Shop()
#     shop.openShop(listaJugadores)
