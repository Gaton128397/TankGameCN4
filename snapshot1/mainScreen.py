from menu import Menu
from winScreen import Winner
from instrucciones import Instrucciones
from random import randint
import pygame,projectile,tank,terreno,time,sys,chooseMenu,infoBlock
WIDTH,HEIGHT = 1300,700
hills = []
canyons = []
potencia = 0
tiempo_presionado = 0
tiempo_anterior = 0
presionado = False


def game():
    pygame.init()
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    window.fill('lightblue')
    pygame.display.set_caption("Tank v Tank")
    winScreen = Winner(window,WIDTH,HEIGHT)
    instrucciones = Instrucciones(window,WIDTH,HEIGHT)
    menu1 = Menu(window,WIDTH,HEIGHT)
    start = 0
    if start ==0:
        menu1.draw_menu()
        pygame.display.update()

    fuente = pygame.font.Font(None, 30)
    fuente2 = pygame.font.Font(None, 60)
    

    initialHeight = HEIGHT-HEIGHT/6

    clock = pygame.time.Clock()
    
    terrain = terreno.terrenoCoseno(window,WIDTH,HEIGHT)
    
    terrain.getTerrain()

    terrainPoints = terrain.getCosPoints()

    player1 = tank.Tank(terrainPoints[randint(0,WIDTH-700)],'blue',1,window) #1 apunta a la derecha
    player2 = tank.Tank(terrainPoints[randint(WIDTH-300,WIDTH-300)],'red',0,window) #0 apunta a la izq

    player1Hitbox = player1.hitBox()
    player2Hitbox = player2.hitBox()

    somebodyWon = False

    shoot = True
    turno = 1

    global potencia, tiempo_presionado, tiempo_anterior, presionado
    lastPower1 = 0
    lastPower2 = 0
    angleBullet1 = 0
    angleBullet2 = 0
    lastAngulo1 = 0
    lastAngulo2 = 0
    alturamaxima1 = 0
    alturamaxima2 = 0
    range1 = 0
    range2 = 0
    end = False

    terrain.drawTerrain()
    player1.draw_tank('blue')
    player2.draw_tank('red')
    run = True

    ammoPlayer1 = [1,10,3]
    ammoPlayer2 = [1,10,3]
    typeBullet = 1
    bulletTypePlayer1 = typeBullet
    bulletTypePlayer2 = typeBullet

    chooseMenu1 = chooseMenu.ChooseMenu(window,WIDTH,HEIGHT)
    chooseMenu1.choosing(1)
    pygame.draw.rect(window, 'white', (0,HEIGHT*0.7,WIDTH,HEIGHT*0.3))
    infoPlayer1 = infoBlock.InfoBlock(window,1,WIDTH,HEIGHT,lastAngulo1,potencia,lastPower1,range1,alturamaxima1)

    infoPlayer2 = infoBlock.InfoBlock(window,2,WIDTH,HEIGHT,lastAngulo2,potencia,lastPower2,range2,alturamaxima2)
    infoPlayer2.drawInfoBlock(potencia,angleBullet2+180, lastPower2, lastAngulo2, range2, alturamaxima2)
    
    while run:
        try:
            if start ==1:
                chooseMenu1.drawChooseMenu(window)
                tiempo_actual = pygame.time.get_ticks() / 1000.0
                if turno == 1:
                    positionBullet1 = player1.moveCannon()
                    angleBullet1 = player1.getAngle()
                    infoPlayer1.deleteLast()
                    
                    
                    infoPlayer1.drawInfoBlock(potencia,angleBullet1, lastPower1, lastAngulo1, range1, alturamaxima1)
                elif turno ==2:
                    positionBullet2 = player2.moveCannon()
                    angleBullet2 = 180-player2.getAngle()
                    infoPlayer2.deleteLast()

                    
                    infoPlayer2.drawInfoBlock(potencia,angleBullet2, lastPower2, lastAngulo2, range2, alturamaxima2)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu1.buttonPlay.collidepoint(event.pos):
                        start = 1
                    if menu1.buttonControls.collidepoint(event.pos):
                        print("a")

                    elif menu1.buttonExit.collidepoint(event.pos):
                        run = False
                        pygame.quit()
                        sys.exit()

                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_1:
                        chooseMenu1.choosing(1)
                        typeBullet = 1
                        if turno ==1:
                            if ammoPlayer1[0] >0:
                                bulletTypePlayer1 =typeBullet
                            else:
                                print('no more 10mm ammo')
                                if ammoPlayer1[1] >0:
                                    bulletTypePlayer1 =2
                                else:
                                    if ammoPlayer1[2] >0:
                                        bulletTypePlayer1 =3
                                    else:
                                        print('player {turno} run out of ammo')
                        
                        elif turno ==2:
                            if ammoPlayer2[0] >0:
                                bulletTypePlayer2 =typeBullet
                            else:
                                print('no more 10mm ammo')
                                if ammoPlayer2[1] >0:
                                    bulletTypePlayer2 =2
                                else:
                                    if ammoPlayer2[2] >0:
                                        bulletTypePlayer2 =3
                                    else:
                                        print('player {turno} run out of ammo')


                    if event.key == pygame.K_2:
                        chooseMenu1.choosing(2)
                        typeBullet = 2
                        if turno ==1:
                            if ammoPlayer1[1] >0:
                                bulletTypePlayer1 =typeBullet
                            else:
                                print('no more 8mm ammo')
                                if ammoPlayer1[2] >0:
                                    bulletTypePlayer1 =3
                                else:
                                    if ammoPlayer1[0] >0:
                                        bulletTypePlayer1 =1
                                    else:
                                        print('player {turno} run out of ammo')
                        
                        elif turno ==2:
                            if ammoPlayer2[1] >0:
                                bulletTypePlayer2 =typeBullet
                            else:
                                print('no more 8mm ammo')
                                if ammoPlayer2[2] >0:
                                    bulletTypePlayer2 =3
                                else:
                                    if ammoPlayer2[0] >0:
                                        bulletTypePlayer2 =1
                                    else:
                                        print('player {turno} run out of ammo')


                    if event.key == pygame.K_3:
                        chooseMenu1.choosing(3)
                        typeBullet = 3
                        if turno ==1:
                            if ammoPlayer1[2] >0:
                                bulletTypePlayer1 =typeBullet
                            else:
                                print('no more 6mm ammo')
                                if ammoPlayer1[1] >0:
                                    bulletTypePlayer1 =2
                                else:
                                    if ammoPlayer1[0] >0:
                                        bulletTypePlayer1 =1
                                    else:
                                        print('player {turno} run out of ammo')
                        elif turno ==2:
                            if ammoPlayer2[2] >0:
                                bulletTypePlayer2 =typeBullet
                            else:
                                print('no more 6mm ammo')
                                


                    if event.key == pygame.K_SPACE:
                        tiempo_presionado = tiempo_actual
                        presionado = True
                    if event.key == pygame.K_RETURN:
                        if turno ==1:
                            bulletTypePlayer1 = typeBullet
                            bullet1 = projectile.Projectile(positionBullet1,bulletTypePlayer1,potencia,angleBullet1,window)
                            deleteBullet = projectile.Projectile(positionBullet1,bulletTypePlayer1,potencia,angleBullet1,window)
                            bullet1.shoot(terrainPoints,player1Hitbox,player2Hitbox)
                            ammoPlayer1[bulletTypePlayer1-1] -=1
                            lastPower1 = potencia
                            potencia = 0
                            range1 = bullet1.getRange()
                            alturamaxima1 = bullet1.getMaxHeight()
                            if bullet1.returnHit() ==1:
                                winScreen.drawWinner(turno)
                                end = True
                            elif bullet1.returnHit() ==2:
                                winScreen.drawWinner(turno)
                                end = True
                            else:
                                deleteBullet.delete(terrainPoints,player1Hitbox,player2Hitbox)
                                turno = 2
                        elif turno ==2:
                            bulletTypePlayer2 = typeBullet
                            bullet2 = projectile.Projectile(positionBullet2,bulletTypePlayer2,potencia,angleBullet2,window) 
                            deleteBullet2 = projectile.Projectile(positionBullet2,bulletTypePlayer2,potencia,angleBullet2,window) 
                            bullet2.shoot(terrainPoints,player2Hitbox,player1Hitbox)
                            ammoPlayer2[bulletTypePlayer2-1] -=1 
                            lastPower2 = potencia
                            potencia = 0
                            range2 = bullet2.getRange() *-1
                            alturamaxima2 = bullet2.getMaxHeight()
                            if bullet2.returnHit() ==1:
                                winScreen.drawWinner(turno)
                                end = True

                            elif bullet2.returnHit() ==2:
                                winScreen.drawWinner(turno)
                                end = True
                            else:
                                deleteBullet2.delete(terrainPoints,player2Hitbox,player1Hitbox)
                                turno = 1
                            
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:

                        if tiempo_actual - tiempo_presionado >= 10.0:  # MÁXIMO 5 SEGUNDOS PARA LLEGAR A 100
                            potencia = 200
                            
                        else:
                            potencia = min((tiempo_actual - tiempo_presionado) * 20, 200)
                        tiempo_anterior = tiempo_actual 
                        presionado = False

                            
            if start == 1:
                pygame.draw.rect(window, 'lightblue', (40,20,350, 70))            
                pygame.draw.rect(window, 'grey', (50, 50, 200, 20))  
            
                if presionado:
                    tiempo_presion = tiempo_actual - tiempo_presionado
                    llenado = min(tiempo_presion * 20, 200)  # Ajustamos el llenado
                    pygame.draw.rect(window, 'red', (50, 50, llenado, 20))
                elif end:
                    winScreen.drawWinner(1)

                    
                elif end:
                    
                    winScreen.drawWinner(1)

                if presionado:
                    potencia_actual = min(tiempo_presion * 20, 200)
                    texto_potencia_actual = fuente.render(f'POWER NOW: {potencia_actual:.1f}', True, 'black')
                    window.blit(texto_potencia_actual, (50, 70))
                elif end:
                    winScreen.drawWinner(1)
                
                
                clock.tick(60)
                pygame.display.update()
        except (ZeroDivisionError,UnboundLocalError):
            textoError = fuente.render("Espera tu turno", True, 'black')
game()