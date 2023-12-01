import pygame, sys,button,items,params,player
pygame.init()
#variables
jugadorTest = player.Player()
jugadorTest2 = player.Player()
jugadorTest3 = player.Player()
jugadorTest4 = player.Player()
listaJugadores = [jugadorTest,jugadorTest2,jugadorTest3,jugadorTest4]
class Shop:
    def __init__(self,window):

        '''SCREEN'''
        self.width, self.height = params.WIDTH, params.HEIGHT
        self.tiendaIni = pygame.image.load('imgs\shop/shopIni.png')
        self.tiendaMid = pygame.image.load('imgs\shop/shopMid.png')
        self.tiendaEnd = pygame.image.load('imgs\shop/shopFin.png')
        self.tiendaIni = pygame.transform.scale(self.tiendaIni,(self.width,self.height))
        self.tiendaMid = pygame.transform.scale(self.tiendaMid,(self.width,self.height))
        self.tiendaEnd = pygame.transform.scale(self.tiendaEnd,(self.width,self.height))
        self.window = window
        self.actualItem = None



        '''ITEMS'''
        self.shield = items.item('shield',0,'+1 escudo',100,params.shield)
        self.dmg = items.item('dmg',1,'+10 dmg',100,params.dmg)
        self.health = items.item('health',2,'+10 vida',100,params.health)
        self.bigStone = items.item('big Stone',3,'piedra grande',100,params.bigStone)
        self.mediumStone = items.item('small Stone',4,'piedra chica',100,params.smallStone)
        self.smallStone = items.item('medium Stone',5,'piedra mediana',100,params.mediumStone)
        
        '''SHOP BUTTONS'''
        self.settingButton = button.Button((params.size*0.1,params.size*0.1,params.size*1.2,params.size*0.9),(0,255,0),'home',False)
        self.homeButton = button.Button((params.size*14.5,params.size*0.15,params.size*1.2,params.size*0.9),(255,0,0),'settings',False)
        self.buyButton = button.Button((params.size*5.3,params.size*7.05,params.size*1.15,params.size*0.8),(255,0,0),'buy',False)
        self.sellButton = button.Button((params.size*9.5,params.size*7,params.size*1.15,params.size*0.8),(255,0,0),'sell',False)
        self.nextButton = button.Button((params.size*12.5,params.size*7.5,params.size*3,params.size*1),(255,0,0),'next',False)
        self.previousButton = button.Button((params.size*0.3,params.size*7.7,params.size*2.9,params.size*0.85),(255,0,0),'previous',False)
        self.finishButton = button.Button((params.size*12.5,params.size*7.5,params.size*3,params.size*1.1),(255,0,255),'finish',False)

        '''ITEMS BUTTONS'''
        self.shieldButton = button.Button((params.size*1.4,params.size*2,params.size*0.9,params.size*1),(255,0,0),self.shield,False)
        self.dmgButton = button.Button((params.size*3.7,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),self.dmg,False)
        self.healthButton = button.Button((params.size*6.1,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),self.health,False)
        self.bigStoneButton = button.Button((params.size*8.8,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),self.bigStone,False)
        self.mediumStoneButton = button.Button((params.size*11,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),self.mediumStone,False)
        self.smallStoneButton = button.Button((params.size*13.5,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),self.smallStone,False)


        self.botonesItems = [self.shieldButton,self.dmgButton,self.healthButton,self.bigStoneButton,self.mediumStoneButton,self.smallStoneButton]
        self.botonesTienda = [self.settingButton,self.homeButton,self.buyButton,self.sellButton,self.finishButton]
    '''METHODS'''


    def selectItem(self,item):
        self.actualItem = item
        # if showItem == 0: #oculta el item
        #     pygame.draw.rect(self.window,((164, 164, 164)),(params.size*4.38,params.size*3.73,params.size*7.27,params.size*3.25))

        # if showItem == 1:
        nombre = pygame.font.Font(None, 30)
        nombre = nombre.render(item.nombre, True, (0, 0, 0))

        descripcion = pygame.font.Font(None, 30)
        descripcion = descripcion.render(item.descripcion, True, (0, 0, 0))
        
        precio = pygame.font.Font(None, 30)
        precio = precio.render(str("precio: $"+str(item.precio)), True, (0, 0, 0))
        
        pygame.draw.rect(self.window,((164, 164, 164)),(params.size*4.38,params.size*3.73,params.size*7.27,params.size*3.25))
        
        self.window.blit(item.Icon,(self.width*0.46,self.height*0.42))
        self.window.blit(nombre,(self.width*0.46,self.height*0.53))
        self.window.blit(descripcion,(self.width*0.46,self.height*0.58))
        self.window.blit(precio,(self.width*0.46,self.height*0.62))

    def showInventory(self,player):

        #texto items
        item1text = pygame.font.Font(None, 30)
        item1text = item1text.render("x"+str(player.inventory[0]), True, (0, 0, 0))


        item2text = pygame.font.Font(None, 30)
        item2text = item2text.render("x"+str(player.inventory[1]), True, (0, 0, 0))
        
        item3text = pygame.font.Font(None, 30)
        item3text = item3text.render("x"+str(player.inventory[2]), True, (0, 0, 0))
        
        item4text = pygame.font.Font(None, 30)
        item4text = item4text.render("x"+str(player.inventory[3]), True, (0, 0, 0))
        
        item5text = pygame.font.Font(None, 30)
        item5text = item5text.render("x"+str(player.inventory[4]), True, (0, 0, 0))
        
        item6text = pygame.font.Font(None, 30)
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
        healthText = pygame.font.Font(None, 60)
        healthText = healthText.render(str(player.inventory[2]*10), True, (0, 0, 0))

        dmgText = pygame.font.Font(None, 60)
        dmgText = dmgText.render(str(player.inventory[1]*10), True, (0, 0, 0))

        shieldText = pygame.font.Font(None, 60)
        shieldText = shieldText.render(str(player.inventory[0]*10), True, (0, 0, 0))
        
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
                if item.ID == 0 and player.inventory[item.ID] < 1: #maximo de 1 escudo 
                    player.inventory[item.ID] +=1
                    player.money -= item.precio
                else:
                    if player.inventory[item.ID] < 10: #maximo de 10 de cada item
                        player.inventory[item.ID] +=1
                        player.money -= item.precio
            
    def showMoney(self,player):
        showMoney = pygame.font.Font(None, 60)
        showMoney = showMoney.render("$"+str(player.money), True, (229,202,0))
        pygame.draw.rect(self.window,'white',(self.width*0.1,self.height*0.03,self.width*0.1,self.height*0.05))
        self.window.blit(showMoney,(self.width*0.1,self.height*0.03))

    def openShop(self,players): #recibe una lista de jugadores
        
        player = 0 #jugador actual
        running =True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                if self.homeButton.check_click(event):
                    return 4
                if self.settingButton.check_click(event):
                    return 0

                if self.buyButton.check_click(event):
                    self.buyItem(self.actualItem,players[player])


                if self.sellButton.check_click(event):
                    self.sellItem(self.actualItem,players[player])

                for i in range(len(self.botonesItems)):
                    if self.botonesItems[i].check_click(event):
                        self.actualItem = self.botonesItems[i].item

                if player == 0:
                    self.window.blit(self.tiendaIni,(0,0))
                    if self.nextButton.check_click(event):
                        player +=1
                        self.actualItem = None
                elif player == len(players)-1:
                    self.window.blit(self.tiendaEnd,(0,0))
                    if self.previousButton.check_click(event):
                        player -=1
                        self.actualItem = None
                    elif self.finishButton.check_click(event):
                        return 10 #sale de la tienda
                else:
                    self.window.blit(self.tiendaMid,(0,0))
                    if self.nextButton.check_click(event):
                        player +=1
                        self.actualItem = None
                    elif self.previousButton.check_click(event):
                        player -=1
                        self.actualItem = None

            self.showInventory(players[player])
            self.showStats(players[player])
            self.showMoney(players[player])
            if self.actualItem != None:
                self.selectItem(self.actualItem)
            pygame.display.update()
        # return 2 #salir de la tienda

# tienda = Shop(pygame.display.set_mode((params.WIDTH, params.HEIGHT)))
# tiendita = tienda.openShop(listaJugadores)
# if tiendita == 0:
#     print("home")
# elif tiendita == 1:
#     print("settings")
# elif tiendita == 2:
#     print("finish")
# else:
#     print("error")
        
