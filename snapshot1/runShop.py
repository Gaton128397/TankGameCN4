<<<<<<< HEAD
import pygame, sys, button ,items

=======
import pygame, sys,button,items
>>>>>>> origin/Maru

pygame.init()

x = 100
width, height = 16*x, 9*x
screen = pygame.display.set_mode((width, height))

<<<<<<< HEAD
tiendaImg = pygame.image.load('snapshot1\shop.png')
=======
tiendaImg = pygame.image.load('snapshot1\imgs\shop.png')
>>>>>>> origin/Maru
tiendaImg = pygame.transform.scale(tiendaImg,(width,height))
screen.blit(tiendaImg,(0,0))
clock = pygame.time.Clock()

#items
shield = items.item('shield','+1 escudo',100)
dmg = items.item('dmg','+10 dmg',100)
health = items.item('health','+10 vida',100)
bigStone = items.item('big Stone','piedra grande',100)
mediumStone = items.item('medium Stone','piedra mediana',100)
smallStone = items.item('small Stone','piedra chica',100)


#botones
<<<<<<< HEAD
settingButton = button.Button((x*0.1,x*0.1,x*1.2,x*0.9),(0,255,0),'settings',False)
homeButton = button.Button((x*14.5,x*0.15,x*1.2,x*0.9),(255,0,0),'home',False)
=======
settingButton = button.Button((x*0.1,x*0.1,x*1.2,x*0.9),(0,255,0),'home',False)
homeButton = button.Button((x*14.5,x*0.15,x*1.2,x*0.9),(255,0,0),'settings',False)
>>>>>>> origin/Maru
item1Button = button.Button((x*1.4,x*2,x*0.9,x*1),(255,0,0),shield,False)
item2Button = button.Button((x*3.7,x*2,x*1.15,x*1.1),(255,0,0),dmg,False)
item3Button = button.Button((x*6.1,x*2,x*1.15,x*1.1),(255,0,0),health,False)
item4Button = button.Button((x*8.8,x*2,x*1.15,x*1.1),(255,0,0),bigStone,False)
item5Button = button.Button((x*11,x*2,x*1.15,x*1.1),(255,0,0),mediumStone,False)
item6Button = button.Button((x*13.5,x*2,x*1.15,x*1.1),(255,0,0),smallStone,False)
buyButton = button.Button((x*5.3,x*7.05,x*1.15,x*0.8),(255,0,0),'buy',False)
sellButton = button.Button((x*9.5,x*7,x*1.15,x*0.8),(255,0,0),'sell',False)
finishButton = button.Button((x*12.5,x*7.5,x*3,x*1.1),(255,0,255),'finish',False)


botonesTienda = [settingButton,homeButton,buyButton,sellButton,finishButton]
botonesItems = [item1Button,item2Button,item3Button,item4Button,item5Button,item6Button]
#variables
itemActual = -1
playerMoney = 1000
playerItemAvailable = 1
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
            sys.exit()
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
    if itemActual != 0 and itemActual != -1:
<<<<<<< HEAD
        pygame.draw.rect(screen,(255,255,255),(0,0,100,100)) #debera ser un cuadrado con texto, info e imagen del Item o Stat
    if itemActual == 1:
        pygame.draw.rect(screen,(0,0,0),(0,0,100,100))# se borra al dar continuar
=======
        
        texto = pygame.font.Font(None, 30)
        texto = texto.render('hola', True, (0, 0, 0))
        screen.blit(texto,(x*5.5,x*4))
        print('.')
        
    if itemActual == 1:
        pygame.draw.rect(screen,((164, 164, 164)),(x*4.38,x*3.73,x*7.27,x*3.25))# se borra al dar continuar
>>>>>>> origin/Maru
    pygame.display.flip()
    clock.tick(60)


