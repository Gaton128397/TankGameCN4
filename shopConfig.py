import pygame, sys,button,items,params

pygame.init()

x = 100
width, height = 16*x, 9*x
screen = pygame.display.set_mode((width, height))

tiendaImg = pygame.image.load('imgs\shop.png')
tiendaImg = pygame.transform.scale(tiendaImg,(width,height))
screen.blit(tiendaImg,(0,0))
clock = pygame.time.Clock()

'''ITEMS'''
shield = items.item('shield',0,'+1 escudo',100,'imgs\shield.png')
dmg = items.item('dmg',1,'+10 dmg',100,'imgs\dmg.png')
health = items.item('health',2,'+10 vida',100,'imgs\health.png')
bigStone = items.item('big Stone',3,'piedra grande',100,'imgs\BigStone.png')
mediumStone = items.item('medium Stone',4,'piedra mediana',100,'imgs\mediumStone.png')
smallStone = items.item('small Stone',5,'piedra chica',100,'imgs\smallStone.png')

#items
settingButton = button.Button((x*0.1,x*0.1,x*1.2,x*0.9),(0,255,0),'home',False)
homeButton = button.Button((x*14.5,x*0.15,x*1.2,x*0.9),(255,0,0),'settings',False)
item1Button = button.Button((x*1.4,x*2,x*0.9,x*1),(255,0,0),shield,False)
item2Button = button.Button((x*3.7,x*2,x*1.15,x*1.1),(255,0,0),dmg,False)
item3Button = button.Button((x*6.1,x*2,x*1.15,x*1.1),(255,0,0),health,False)
item4Button = button.Button((x*8.8,x*2,x*1.15,x*1.1),(255,0,0),bigStone,False)
item5Button = button.Button((x*11,x*2,x*1.15,x*1.1),(255,0,0),mediumStone,False)
item6Button = button.Button((x*13.5,x*2,x*1.15,x*1.1),(255,0,0),smallStone,False)
buyButton = button.Button((x*5.3,x*7.05,x*1.15,x*0.8),(255,0,0),'buy',False)
sellButton = button.Button((x*9.5,x*7,x*1.15,x*0.8),(255,0,0),'sell',False)
finishButton = button.Button((x*12.5,x*7.5,x*3,x*1.1),(255,0,255),'finish',False)

botonesItems = [item1Button,item2Button,item3Button,item4Button,item5Button,item6Button]
botonesTienda = [settingButton,homeButton,buyButton,sellButton,finishButton]




botonesTienda = [settingButton,homeButton,buyButton,sellButton,finishButton]
botonesItems = [item1Button,item2Button,item3Button,item4Button,item5Button,item6Button]
#variables
itemActual = None
playerMoney = 1000
playerItemAvailable = 10
showItem = False


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
    showMoney = pygame.font.Font(None, 60)
    showMoney = showMoney.render("$"+str(playerMoney), True, (229,202,0))
    pygame.draw.rect(screen,'white',(width*0.1,height*0.03,width*0.08,height*0.05))
    screen.blit(showMoney,(width*0.1,height*0.03))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    for boton in botonesTienda:
        if boton.check_click(event):

            if boton.item == 'home': #anda al menu
                print('casita')

            elif boton.item == 'settings': #anda a settings
                print('engranaje')
                
            elif boton.item == 'buy':
                if itemActual !=None:
                    if itemActual != -1 and playerMoney >= itemActual.precio: #si tiene dinero, compra
                        playerItemAvailable -=1
                        playerMoney -= itemActual.precio
                        print(f'compra de {itemActual.nombre}')
            elif boton.item == 'sell':
                if itemActual !=None:
                    if itemActual != -1 and playerItemAvailable > 0: #si le quedan, vende
                        playerItemAvailable +=1
                        playerMoney += itemActual.precio
                        print(f'venta de {itemActual.nombre}')
            elif boton.item == 'finish': #termina la compra
                print('fin de compra')
                showItem = False
                itemActual = None

    for itemButton in botonesItems:
        if itemButton.check_click(event):
            itemActual = itemButton.item
            showItem = True
    if showItem:
        nombre = pygame.font.Font(None, 30)
        nombre = nombre.render(itemActual.nombre, True, (0, 0, 0))
        descripcion = pygame.font.Font(None, 30)
        descripcion = descripcion.render(itemActual.descripcion, True, (0, 0, 0))
        precio = pygame.font.Font(None, 30)
        precio = precio.render(str("precio: $"+str(itemActual.precio)), True, (0, 0, 0))
        cantidad = pygame.font.Font(None, 30)
        cantidad = cantidad.render(str("cantidad: "+str(playerItemAvailable)), True, (0, 0, 0))
        pygame.draw.rect(screen,((164, 164, 164)),(params.size*4.38,params.size*3.73,params.size*7.27,params.size*3.25))
        screen.blit(itemActual.Icon,(width*0.46,height*0.42))
        screen.blit(nombre,(width*0.46,height*0.53))
        screen.blit(descripcion,(width*0.46,height*0.58))
        screen.blit(precio,(width*0.46,height*0.62))
        screen.blit(cantidad,(width*0.46,height*0.66))
    if not showItem:
        pygame.draw.rect(screen,((164, 164, 164)),(params.size*4.38,params.size*3.73,params.size*7.27,params.size*3.25))
    pygame.display.flip()
    clock.tick(60)