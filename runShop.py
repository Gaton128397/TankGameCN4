import pygame, sys,button,items,params
pygame.init()
#variables
itemActual = -1
playerMoney = 1000
playerItemAvailable = 1
showItem = False

class Shop:
    def __init__(self):

        '''SCREEN'''
        self.width, self.height = 16*params.size, 9*params.size
        self.tiendaImg = pygame.image.load('imgs\shop.png')
        self.tiendaImg = pygame.transform.scale(self.tiendaImg,(self.width,self.height))

        '''ITEMS'''
        self.shield = items.item('shield',0,'+1 escudo',100,'imgs\shield.png')
        self.dmg = items.item('dmg',1,'+10 dmg',100,'imgs\dmg.png')
        self.health = items.item('health',2,'+10 vida',100,'imgs\health.png')
        self.bigStone = items.item('big Stone',3,'piedra grande',100,'imgs\BigStone.png')
        self.mediumStone = items.item('medium Stone',4,'piedra mediana',100,'imgs\mediumStone.png')
        self.smallStone = items.item('small Stone',5,'piedra chica',100,'imgs\smallStone.png')

        '''BOTONES'''
        self.settingButton = button.Button((params.size*0.1,params.size*0.1,params.size*1.2,params.size*0.9),(0,255,0),'home',False)
        self.homeButton = button.Button((params.size*14.5,params.size*0.15,params.size*1.2,params.size*0.9),(255,0,0),'settings',False)
        self.item1Button = button.Button((params.size*1.4,params.size*2,params.size*0.9,params.size*1),(255,0,0),self.shield,False)
        self.item2Button = button.Button((params.size*3.7,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),self.dmg,False)
        self.item3Button = button.Button((params.size*6.1,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),self.health,False)
        self.item4Button = button.Button((params.size*8.8,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),self.bigStone,False)
        self.item5Button = button.Button((params.size*11,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),self.mediumStone,False)
        self.item6Button = button.Button((params.size*13.5,params.size*2,params.size*1.15,params.size*1.1),(255,0,0),self.smallStone,False)
        self.buyButton = button.Button((params.size*5.3,params.size*7.05,params.size*1.15,params.size*0.8),(255,0,0),'buy',False)
        self.sellButton = button.Button((params.size*9.5,params.size*7,params.size*1.15,params.size*0.8),(255,0,0),'sell',False)
        self.finishButton = button.Button((params.size*12.5,params.size*7.5,params.size*3,params.size*1.1),(255,0,255),'finish',False)

        self.botonesItems = [self.item1Button,self.item2Button,self.item3Button,self.item4Button,self.item5Button,self.item6Button]
        self.botonesTienda = [self.settingButton,self.homeButton,self.buyButton,self.sellButton,self.finishButton]

        
        
        '''VARIABLES AND PLAYERS'''
        self.players = []
        self.player = 0
        self.item = 0
        self.showItem = False

    '''METHODS'''

    '''
    def getPlayers(self,players):
        self.players = players #guarda los jugadores para recorrerlos al mostrar la tienda

        #ESTO SOLO ES LA LOGICA DE COMO SE MUESTRA LA TIENDA, NO SE SI VA A IR EN ESTE METODO O EN OTRO
        while self.player < len(players): #por cada jugador en la lista de jugadores
            if self.player.type==1: #0 es humano, 1 es bot. En caso de ser bot, no se muestra la tienda ya que los items se eligen al azar (de manera proporcionada)
                print('es bot')
                print('comprando items. . .') #el bot compra items solo
                
            else:
                print('es humano')
                print('mostrando tienda. . .') #cuando se presione volver, se guarda lo que compro el jugador y su saldo y se disminuye el indice, en caso de continuar lo mismo pero se aumenta el indice
                
        pass
    '''

    def showItem(self,item,screen,player):
        if showItem == 0: #oculta el item
            pygame.draw.rect(screen,((164, 164, 164)),(params.size*4.38,params.size*3.73,params.size*7.27,params.size*3.25))

        if showItem == 1:
            nombre = pygame.font.Font(None, 30)
            nombre = nombre.render(item.nombre, True, (0, 0, 0))
            descripcion = pygame.font.Font(None, 30)
            descripcion = descripcion.render(item.descripcion, True, (0, 0, 0))
            precio = pygame.font.Font(None, 30)
            precio = precio.render(str("precio: $"+str(item.precio)), True, (0, 0, 0))
            pygame.draw.rect(screen,((164, 164, 164)),(params.size*4.38,params.size*3.73,params.size*7.27,params.size*3.25))
            screen.blit(item.Icon,(self.width*0.46,self.height*0.42))
            screen.blit(nombre,(self.width*0.46,self.height*0.53))
            screen.blit(descripcion,(self.width*0.46,self.height*0.58))
            screen.blit(precio,(self.width*0.46,self.height*0.62))

            '''
            cantidad = pygame.font.Font(None, 30)
            cantidad = cantidad.render(str("cantidad: "+str(self.player.inventory[])), True, (0, 0, 0))
            screen.blit(cantidad,(self.width*0.46,self.height*0.66))
            '''
            
        pass
    
    def sellItem(self,item,player):
        if player.inventory[item.ID] > 0:
            player.inventory[item.ID] -=1
            player.money += item.precio

    def buyItem(self,item,player):
        if player.money >= item.precio:
            player.inventory[item.ID] +=1
            player.money -= item.precio
            
    def showMoney(self,screen,player):
        showMoney = pygame.font.Font(None, 60)
        showMoney = showMoney.render("$"+str(player.money), True, (229,202,0))
        pygame.draw.rect(screen,'white',(self.width*0.1,self.height*0.03,self.width*0.08,self.height*0.05))
        screen.blit(showMoney,(self.width*0.1,self.height*0.03))
    def endShop(self):
        pass


def buy(player,item):
    if player.inventory[0] == 0:
        player.inventory[0] +=1 #compra piedra grande
        player.Money -= item.precio
    elif player.inventory[1] == 0:
        player.inventory[1] +=1
        player.Money -= item.precio
    elif player.inventory[2] == 0:
        player.inventory[2] +=1
        player.Money -= item.precio

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.eparams.sizeit()
    for boton in botonesTienda:
        if boton.check_click(event):

            if boton.item == 'home': #anda al menu
                print('casita')

            elif boton.item == 'settings': #anda a settings
                print('engranaje')
                
            elif boton.item == 'buy':
                if itemActual != -1 and playerMoney >= itemActual.precio: #si tiene dinero, compra
                    print(f'compra de {itemActual.nombre}')

            elif boton.item == 'sell':
                if itemActual != -1 and playerItemAvailable > 0: #si le quedan, vende
                    print(f'venta de {itemActual.nombre}')
                    
            elif boton.item == 'finish': #termina la compra
                print('fin de compra')
                itemActual = 1

    for itemButton in botonesItems:
        if itemButton.check_click(event):
            itemActual = itemButton.item

    if itemActual != 0 and itemActual != -1: #muestra el item
        
        texto = pygame.font.Font(None, 30)
        texto = texto.render('hola', True, (0, 0, 0))
        screen.blit(texto,(params.size*5.5,params.size*4))
        
        
    if itemActual == 1:
        # se borra al dar continuar
    pygame.display.flip()
    clock.tick(60)


