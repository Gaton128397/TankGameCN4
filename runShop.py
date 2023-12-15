import pygame, sys,crearItems,params,player,time,functions
from button import Button

pygame.init()

#variables

jugadorTest = player.Player()
jugadorTest2 = player.Player()
jugadorTest3 = player.Player()
jugadorTest4 = player.Player()
listaJugadores = [jugadorTest,jugadorTest2,jugadorTest3,jugadorTest4]

tiendaIni = pygame.image.load('Pantallas/shopIni.png')
tiendaMid = pygame.image.load('Pantallas/shopMid.png')
tiendaEnd = pygame.image.load('Pantallas/shopFin.png')

actualItem = None

'''METHODS'''
def createItems():
    '''CREARITEMS'''
    shield = crearItems.item(0,'shield','reduce daño (1 uso)',100,params.shield)
    dmg = crearItems.item(1,'damage','+10 daño',100,params.dmg)
    health = crearItems.item(2,'health','+10 vida',100,params.health)
    bigStone = crearItems.item(3,'Big Projectile','piedra grande',100,params.bigStone)
    mediumStone = crearItems.item(4,"Medium Projectile",'piedra chica',100,params.smallStone)
    smallStone = crearItems.item(5,'Small Projectile','piedra mediana',100,params.mediumStone)
    return [shield,dmg,health,bigStone,mediumStone,smallStone]

def buttons():
    buttons = [ 
        Button(0.78, 0.85, 0.2, 0.1,'Next'), #siguiente
        Button(0.015, 0.85, 0.2, 0.1,'Back'), #volver


        Button(0.330, 0.78, 0.09, 0.1,'Buy'), #comprar
        Button(0.585, 0.78, 0.09, 0.1,'Sell'), #vender

        Button(0.14, 0.22, 0.11, 0.15,createItems()[0]), #escudo
        Button(0.3, 0.22, 0.11, 0.15,createItems()[1]), #espada
        Button(0.45, 0.22, 0.11, 0.15,createItems()[3]), #piedra grande
        Button(0.60, 0.22, 0.11, 0.15,createItems()[4]), #piedra pequena
        Button(0.75, 0.22, 0.11, 0.15,createItems()[5]) #piedra mediana
        ]
    
    return buttons

def selectItem(item):
    actualItem = item
    ignore = [None,'Buy','Sell','Next','Back']
    if actualItem not in ignore:
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
    else:
        pygame.draw.rect(params.screen,(('#D6C6BC')),(params.size*4.38,params.size*3.73,params.size*7.27,params.size*3.25))
def showInventory(player):

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
    pygame.draw.rect(params.screen,'white',(params.size*1,params.size*6.8,params.size*0.45,params.size*0.4))
    pygame.draw.rect(params.screen,'white',(params.size*2.75,params.size*5,params.size*0.45,params.size*0.4))
    pygame.draw.rect(params.screen,'white',(params.size*2.75,params.size*5.8,params.size*0.45,params.size*0.4))
    pygame.draw.rect(params.screen,'white',(params.size*2.75,params.size*6.8,params.size*0.45,params.size*0.4))
    
    #escribir nuevo
    params.screen.blit(item1text,(params.size*1,params.size*5))
    params.screen.blit(item2text,(params.size*1,params.size*6.8))
    params.screen.blit(item6text,(params.size*2.75,params.size*5))
    params.screen.blit(item4text,(params.size*2.75,params.size*5.8))
    params.screen.blit(item5text,(params.size*2.75,params.size*6.8))

def showStats(player):
    
    #texto stats

    dmgText = pygame.font.Font(None, int(params.size*0.6))
    dmgText = dmgText.render(str(player.inventory[1]*10), True, (0, 0, 0))

    shieldText = pygame.font.Font(None, int(params.size*0.6))
    shieldText = shieldText.render(str(player.inventory[0]), True, (0, 0, 0))
    
    #borrar anterior
    pygame.draw.rect(params.screen,'white',(params.size*13.5,params.size*4.5,params.size*1.5,params.size*0.4))
    pygame.draw.rect(params.screen,'white',(params.size*13.5,params.size*6.5,params.size*1.5,params.size*0.4))
    
    #escribir nuevo
    params.screen.blit(dmgText,(params.size*13.5,params.size*6.5))
    params.screen.blit(shieldText,(params.size*13.5,params.size*4.5))

def sellItem(item,player):
    if player.inventory[item.ID] > 0:
        player.inventory[item.ID] -=1
        print(item.nombre)
        print("id",item.ID)
        print(player.inventory[item.ID])
        player.money += item.precio

def buyItem(item,player):
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

def showMoney(player):
    showMoney = pygame.font.Font(None, int(params.size*0.6))
    showMoney = showMoney.render("$"+str(player.money), True, (229,202,0))
    pygame.draw.rect(params.screen,'white',(params.size*16*0.1,params.size*9*0.03,params.size*16*0.1,params.size*9*0.05))
    params.screen.blit(showMoney,(params.size*16*0.1,params.size*9*0.03))
    
def openShop(playerList): #recibe una lista de jugadores
    actualImg = tiendaIni
    player = 0 #jugador actual
    running =True
    actualItem = None
    ignore = [None,'Buy','Sell','Next','Back']
    while running:
        params.screen.blit(pygame.transform.scale(actualImg, (params.size*16,params.size*9)), (0, 0))
        
        #DESCOMENTAR PARA VER HITBOX BOTONES TIENDA

        #for boton in buttons():
            #pygame.draw.rect(params.screen, (255, 0, 0), boton.rect, 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                
            for boton in buttons():
                time.sleep(0.005)
                if boton.check_click(event):
                    if boton.item == 'Buy' and actualItem not in ignore:
                        buyItem(actualItem,playerList[player])
                    elif boton.item == 'Sell' and actualItem not in ignore:
                        sellItem(actualItem,playerList[player])
                    elif boton.item == 'Back':
                        if player > 0:
                            player -= 1
                            actualItem = None
                        else:
                            player = len(playerList)-1
                            actualItem = None
                    elif boton.item == 'Next':
                        if player == len(playerList)-1:
                            running = False
                            actualItem = None
                        if player < len(playerList)-1:
                            player += 1
                            actualItem = None

                    else:
                        actualItem = boton.item
                        selectItem(boton.item)

        #dibujar tienda
        if player == 0:
            
            actualImg = tiendaIni
        elif player == len(playerList)-1:
            
            actualImg = tiendaEnd
        else:
            
            actualImg = tiendaMid

        if actualItem != None:
            selectItem(actualItem)
        showInventory(playerList[player])
        showStats(playerList[player])
        showMoney(playerList[player])
        pygame.display.update()
    return 12

#DESCOMENTAR PARA EJECUTAR TIENDA DE MANERA INDEPENDIENTE

#if __name__ == "__main__":
#   openShop(listaJugadores)