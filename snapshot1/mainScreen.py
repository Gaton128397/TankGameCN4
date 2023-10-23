from winnerdisplay import drawWinner
from newMenu import draw_menu
from instrucciones import draw_instrucciones
from random import randint
from barravida import BarraVida
import pygame,projectile,tank,terreno,time,sys,chooseMenu, params, drawFunctions,  infoBlock

WIDTH,HEIGHT = params.WIDTH,params.HEIGHT
hills = []
canyons = []
potencia = 0
tiempo_presionado = 0
tiempo_anterior = 0
presionado = False



def game():

    #informacion pygame
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((WIDTH, HEIGHT))



    pygame.display.set_caption("Tank v Tank")
    fuente = pygame.font.Font(None, 30)
    fuente2 = pygame.font.Font(None, 60)
    
    ganador = 0

    superficies = []
    actualScreen = 0

    surfaceMenu = pygame.Surface((WIDTH,HEIGHT))
    surfaceJuego = pygame.Surface((WIDTH,HEIGHT))
    surfaceControles = pygame.Surface((WIDTH,HEIGHT))
    surfaceWinner =pygame.Surface((WIDTH,HEIGHT))

    listaBotones = draw_menu(surfaceMenu, WIDTH, HEIGHT)
    listaBotones.append(draw_instrucciones(surfaceControles, WIDTH, HEIGHT))
    listaBotones.append(drawWinner(surfaceWinner, WIDTH, HEIGHT, ganador))

    superficies.append(surfaceMenu)
    superficies.append(surfaceControles)
    superficies.append(surfaceJuego)
    superficies.append(surfaceWinner)

    #variables globales para la potencia
    global potencia, tiempo_presionado, tiempo_anterior, presionado,falling


    #variables de informacion impresa
    lastPower1 = 0;lastPower2 = 0;angleBullet1 = 0;angleBullet2 = 0;lastAngulo1 = 0;lastAngulo2 = 0;alturamaxima1 = 0;alturamaxima2 = 0;range1 = 0;range2 = 0;end = False
    
    chooseMenu1 = chooseMenu.ChooseMenu(surfaceJuego, WIDTH, HEIGHT)
    chooseMenu2 = chooseMenu.ChooseMenu(surfaceJuego, WIDTH, HEIGHT)

    #terreno
    terrain = terreno.TerrenoVariado(surfaceJuego, WIDTH, HEIGHT)
    terrain.getTerrain()
    terrainYpoints = terrain.yPoint()
    terrainPoints = terrain.getPoints()
    
    #crear Jugadores


    player1 = tank.Tank((randint(20,WIDTH*0.5),10), "blue", 1, surfaceJuego,terrainPoints)
    player2 = tank.Tank((randint(WIDTH*0.5,WIDTH),10), "red", 0, surfaceJuego,terrainPoints)

    #crear hitbox jugadores
    player1Hitbox = player1.hitBox()
    player2Hitbox = player2.hitBox()
    
    #variables municion jugadores
    ammoPlayer1 = [3, 10, 3]
    ammoPlayer2 = [3, 10, 3]
    typeBullet = 1
    bulletTypePlayer1 = typeBullet
    bulletTypePlayer2 = typeBullet

    #info jugadores
    infoPlayer1 = infoBlock.InfoBlock(surfaceJuego,1,WIDTH,HEIGHT,lastAngulo1,potencia,lastPower1,range1,alturamaxima1,)
    infoPlayer2 = infoBlock.InfoBlock(surfaceJuego,2,WIDTH,HEIGHT,lastAngulo2,potencia,lastPower2,range2,alturamaxima2,)

    #variables flujo de juego
    somebodyWon = False
    shoot = True
    turno = 1
    falling = 1
    end = False
    run = True
    start = 0

    playersInGame = []
    playersInGame.append(player1)
    playersInGame.append(player2)

    LAYERS = [] #indice 0 terreno y background, indice 1 jugadores
    LAYERS.append(terrain.drawTerrain())
    LAYERS.append(playersInGame)
    
    surfaceJuego.blit(LAYERS[0],(0,0))
    if falling !=0:
        LAYERS[1][0].draw_tank(False)
        LAYERS[1][1].draw_tank(False)
    
        tempWindows = []
        tempWindows.append(surfaceJuego.copy())
        tempWindows.append(surfaceJuego.copy())
        tempWindows.append(surfaceJuego.copy())

        LAYERS[1][0].draw_tank(True)
        LAYERS[1][1].draw_tank(True)
    
    
    
        


    #draw objetcs
    terrain.drawTerrain()
    #chooseMenu1.choosing(1,surfaceJuego)
    #pygame.draw.rect(window, (255, 213, 158), (0, HEIGHT * 0.7, WIDTH, HEIGHT * 0.3))
    
    infoPlayer1.drawInfoBlock(surfaceJuego,potencia,angleBullet1,lastPower1,lastAngulo1,range1,alturamaxima1,)
    infoPlayer2.drawInfoBlock(surfaceJuego,potencia, angleBullet2 + 180, lastPower2, lastAngulo2, range2, alturamaxima2)
    chooseState = []
    chooseState.append(0)
    chooseState.append(0)
    #comienzo juego
    while run:
        try:
            window.blit(superficies[actualScreen], (0,0))
            pygame.display.update()
            if actualScreen ==2:
                #inicia el juego
                tiempo_actual = pygame.time.get_ticks() / 1000.0
                chooseMenu1.drawChooseMenu(surfaceJuego,0)
                if turno == 1:
                    #mover el cañon 1
                    LAYERS[1][0].moveCannon(tempWindows)
                    angleBullet1 = LAYERS[1][0].getAngle()
                    infoPlayer1.deleteLast(surfaceJuego)
                    # escrbir informacion jugador 1
                    infoPlayer1.drawInfoBlock(surfaceJuego,potencia,angleBullet1,lastPower1,lastAngulo1,range1,alturamaxima1)
                    chooseMenu1.drawChooseMenu(surfaceJuego,chooseState[0])
                    
                elif turno == 2:
                    #mover el cañon 2
                    LAYERS[1][1].moveCannon(tempWindows)
                    angleBullet2 =180- LAYERS[1][1].getAngle()
                    infoPlayer2.deleteLast(surfaceJuego)
                    #escrbir informacion jugador 2
                    infoPlayer2.drawInfoBlock(surfaceJuego,potencia,angleBullet2,lastPower2,lastAngulo2,range2,alturamaxima2)
                    chooseMenu2.drawChooseMenu(surfaceJuego,chooseState[1])
                    
                
                    
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    sys.exit()

                elif event.type == pygame.MOUSEBUTTONDOWN:

                    #Botones menu
                    if actualScreen == 0:

                        if listaBotones[0].collidepoint(event.pos):
                            
                            actualScreen = 2

                        elif listaBotones[1].collidepoint(event.pos):
                            #abre las instrucciones
                            
                            actualScreen = 1

                        elif listaBotones[2].collidepoint(event.pos):

                            #cierra el juego
                            run = False
                            pygame.quit()
                            sys.exit()

                    elif actualScreen == 1:
                        if listaBotones[3].collidepoint(event.pos):
                            #vuelve al menu
                            actualScreen = 0
                            
                    elif actualScreen == 2:
                        start =1
                        #('a')
                    elif actualScreen == 3:
                        #('aaaaaaaaaaaaaaaaaaa')
                        if listaBotones[4].collidepoint(event.pos):
                            #vuelve al menu
                            #('a')
                            actualScreen = 0
                            terrain.resetTerrain()
                            end = False
                            turno = 1
                elif event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_1:#boton 1
                        if turno == 1:
                            if ammoPlayer1[0] > 0: #revisa que queden
                                chooseState[0] = 1
                                typeBullet = 1 #cambia el proyectil al tipo 1 que es 100mm
                                bulletTypePlayer1 = typeBullet
                            
                        elif turno == 2:
                            if ammoPlayer2[0] > 0:
                                chooseState[1] = 1
                                typeBullet = 1
                                bulletTypePlayer2 = typeBullet
                            
                    if event.key == pygame.K_2:#boton 2
                        if turno == 1:
                            if ammoPlayer1[1] > 0:
                                chooseState[0] = 2
                                typeBullet = 2
                                bulletTypePlayer1 = typeBullet
                            
                        elif turno == 2:
                            if ammoPlayer2[1] > 0:
                                chooseState[1] = 2
                                typeBullet = 2
                                bulletTypePlayer2 = typeBullet
                            
                    if event.key == pygame.K_3:#boton 3
                        if turno == 1:
                            if ammoPlayer1[2] > 0:
                                chooseState[0] = 3
                                typeBullet = 3
                                bulletTypePlayer1 = typeBullet
                            
                        elif turno == 2:
                            if ammoPlayer2[2] > 0:
                                chooseState[1] = 3
                                typeBullet = 3
                                bulletTypePlayer2 = typeBullet
                            
                    if event.key == pygame.K_SPACE:
                        tiempo_presionado = tiempo_actual
                        presionado = True

                    if event.key == pygame.K_RETURN:
                        if turno == 1:
                            if ammoPlayer1[bulletTypePlayer1 - 1] > 0:
                                bulletTypePlayer1 = typeBullet
                            else:
                                #('no quedan')
                                bulletTypePlayer1 = 5 #5 es que no quedan
                            bullet1 = projectile.Projectile(LAYERS[1][0].end,bulletTypePlayer1,potencia,angleBullet1,window,)
                            
                            bullet1.shoot(terrainPoints, player1Hitbox, player2Hitbox,surfaceJuego)
                            ammoPlayer1[bulletTypePlayer1 - 1] -= 1
                            lastAngulo1 = angleBullet1
                            lastPower1 = potencia
                            potencia = 0
                            range1 = bullet1.getRange()
                            alturamaxima1 = bullet1.getMaxHeight()
                            alturamaxima1 = bullet1.getMaxHeight()
                            if player2.getHeath() <= 0:  
                                ganador = turno
                                actualScreen = 3
                                end = True
                            else:
                                if bullet1.returnHit() == 1:
                                    """
                                    ganador = turno
                                    actualScreen = 3
                                    end = True
                                    """
                                    print("el enemigo aun tiene vida!")
                                    if bulletTypePlayer1 == 1:
                                        player2.loseHealth(1)
                                        print("-50")
                                        turno = 2
                                    elif bulletTypePlayer1 == 2:
                                        player2.loseHealth(2)
                                        print("-40")
                                        turno = 2
                                    elif bulletTypePlayer1 == 3:
                                        player2.loseHealth(3)
                                        print("-30")
                                        turno = 2

                                    if player2.getHeath() <= 0:
                                        ganador = 1
                                        actualScreen = 3
                                        end = True
                                        
                                elif bullet1.returnHit() == 2:
                                    ganador = turno
                                    actualScreen = 3
                                    end = True

                                else:
                                    turno = 2

                        elif turno == 2:
                            if ammoPlayer2[bulletTypePlayer2 - 1] > 0:
                                bulletTypePlayer2 = typeBullet
                            else:
                                #('no quedan')
                                bulletTypePlayer2 = 5
                            
                            bullet2 = projectile.Projectile(LAYERS[1][1].end,bulletTypePlayer2,potencia,angleBullet2,window,)
                            
                            bullet2.shoot(terrainPoints, player2Hitbox, player1Hitbox,surfaceJuego)
                            
                            ammoPlayer2[bulletTypePlayer2 - 1] -= 1
                            lastAngulo2 = 180 - angleBullet2 

                            lastPower2 = potencia
                            
                            potencia = 0
                            
                            range2 = bullet2.getRange() * -1
                            
                            alturamaxima2 = bullet2.getMaxHeight()
                            
                            if player1.getHeath() <= 0:
                                ganador = turno
                                actualScreen = 3
                                end = True
                                
                            else:
                                if bullet2.returnHit() == 1:
                                    """
                                    ganador = turno
                                    actualScreen = 3
                                    end = True
                                    """
                                    print("el enemigo aun tiene vida!")
                                    if bulletTypePlayer2 == 1:
                                        player1.loseHealth(1)
                                        print("-50")
                                        turno = 1
                                    elif bulletTypePlayer2 == 2:
                                        player1.loseHealth(2)
                                        print("-40")
                                        turno = 1
                                    elif bulletTypePlayer2 == 3:
                                        player1.loseHealth(3)
                                        print("-30")
                                        turno = 1
                                    
                                    if player1.getHeath() <= 0:
                                        ganador = 2
                                        actualScreen = 3
                                        end = True

                                elif bullet2.returnHit() == 2:
                                    ganador = turno
                                    actualScreen = 3
                                    end = True

                                else:
                                    turno = 1

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if (
                            tiempo_actual - tiempo_presionado >= 10.0
                        ):  # MÁXIMO 5 SEGUNDOS PARA LLEGAR A 100
                            potencia = 200
                        else:
                            potencia = min(
                                (tiempo_actual - tiempo_presionado) * 20, 200
                            )
                        tiempo_anterior = tiempo_actual
                        presionado = False

            if actualScreen ==2:
                pygame.draw.rect(surfaceJuego, (255, 213, 158), (WIDTH*0.4, 620, 200, 40))
                pygame.draw.rect(surfaceJuego, "grey", (WIDTH*0.4, 600, 200, 20))
                if presionado:
                    tiempo_presion = tiempo_actual - tiempo_presionado
                    llenado = min(tiempo_presion * 20, 200)  # Ajustamos el llenado
                    pygame.draw.rect(surfaceJuego, "red", (WIDTH*0.4, 600, llenado, 20))
                elif end:
                    ganador = turno
                    actualScreen = 3
                elif end:
                    ganador = turno
                    actualScreen = 3
                if presionado:
                    potencia_actual = min(tiempo_presion * 20, 200)
                    texto_potencia_actual = fuente.render(
                        f"POWER NOW: {potencia_actual:.1f}", True, "black"
                    )
                    surfaceJuego.blit(texto_potencia_actual, (WIDTH*0.4, 620))
                elif end: 
                    ganador = turno
                    actualScreen = 3
                clock.tick(60)
                pygame.display.update()

        except (ZeroDivisionError, UnboundLocalError,AttributeError,IndexError):
            textoError = fuente.render("Espera tu turno", True, "black")

game()