from endDisplay import drawEnd
from newMenu import draw_menu
from instrucciones import draw_instrucciones
from pausa import drawPausa
from random import randint
from shop import Shop
import pygame,projectile,tank,terreno,time,sys,chooseMenu, params, drawFunctions,  infoBlock

WIDTH,HEIGHT = params.WIDTH,params.HEIGHT
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
    
    ganador = 1

    
    
    

    superficies = []
    actualScreen = 0

    surfaceMenu = pygame.Surface((WIDTH,HEIGHT))
    surfaceJuego = pygame.Surface((WIDTH,HEIGHT))
    surfaceControles = pygame.Surface((WIDTH,HEIGHT))
    surfaceWinner =pygame.Surface((WIDTH,HEIGHT))
    surfacePausa = pygame.Surface((WIDTH//2,HEIGHT//2))
    surfaceTienda = pygame.Surface((WIDTH,HEIGHT))


    listaBotones = draw_menu(surfaceMenu, WIDTH, HEIGHT)#0,1,2
    listaBotones.append(draw_instrucciones(surfaceControles, WIDTH, HEIGHT))#3
    listaBotones.append(drawPausa(surfacePausa,WIDTH//4, HEIGHT//4))#4
    listaBotones.append(drawEnd(surfaceWinner, WIDTH, HEIGHT, ganador))#5

    superficies.append(surfaceMenu) #0
    superficies.append(surfaceControles) #1
    superficies.append(surfaceJuego) #2
    superficies.append(surfaceWinner) #3
    superficies.append(surfacePausa) #4
    superficies.append(surfaceTienda) #5
    
    #crear tienda
    tiendita1 = Shop(1,'blue')
    tiendita2 = Shop(2,'red')
    # infoTiendita1 = 
    tiendita1.drawShop(surfaceTienda, WIDTH, HEIGHT)
    # infoTiendita2 = tiendita2.drawShop(surfaceTienda, WIDTH, HEIGHT)

    # botonesStats1 = infoTiendita1[0]
    # botonesStats2 = infoTiendita2[0]
    
    # botonesAmmo1 = infoTiendita1[1]
    # botonesAmmo2 = infoTiendita2[1]

    #variables globales para la potencia
    global potencia, tiempo_presionado, tiempo_anterior, presionado,seconds,minutes


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
    # player1 = tank.Tank(terrainPoints[randint(0, WIDTH - 700)], "blue", 1, surfaceJuego)
    # player2 = tank.Tank(terrainPoints[randint(WIDTH - 300, WIDTH - 300)], "red", 0, surfaceJuego)

    player1 = tank.Tank((randint(20,int(WIDTH*0.5)),10), "blue", 1, surfaceJuego,terrainPoints)
    player2 = tank.Tank((randint(int(WIDTH*0.5),WIDTH),10), "red", 0, surfaceJuego,terrainPoints)

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
    end = False
    run = True
    start = 0
    #timer
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    
    surfaceTimer = pygame.Surface((80, 25))
    surfaceTimer.fill((255, 255, 255))
    font = pygame.font.SysFont('Consolas', 28)
    minutes = 5#10
    seconds = 59#59


    
    # terrain.drawTerrain()

    def creaLayer(surfaceJuego,pos1,pos2):
        LAYERS = [] #indice 0 terreno y background, indice 1 jugadores
        #terreno
        terrain = terreno.TerrenoVariado(surfaceJuego, WIDTH, HEIGHT)
        terrain.getTerrain()

        

        terrainYpoints = terrain.yPoint()
        terrainPoints = terrain.getPoints()
        
        player1 = tank.Tank((0,0), "blue", 1, surfaceJuego,terrainPoints)
        player2 = tank.Tank((0,0), "red", 0, surfaceJuego,terrainPoints)

        positionTank1 = (randint(20,WIDTH*0.5),10)
        positionTank2 = (randint(WIDTH*0.5,WIDTH),10)
        
        # position =[positionTankX,positionTankY]
        
        playersInGame = []
        playersInGame.append(player1)
        playersInGame.append(player2)
        
        
        LAYERS.append(terrain) #0 añade el terreno a las capas
        LAYERS.append(playersInGame) #1 añade los jugadores a las capas

        
        surfaceJuego.blit(LAYERS[0].drawTerrain(),(0,0))

        tempWindows = []
        tempWindows.append(LAYERS[0].drawTerrain()) #guarda el terreno para poder ir dibujandolo con cada movimiento del  cañon
        tempWindows.append(LAYERS[1])
        # tempWindows.append(LAYERS[1])
        # tempWindows.append(playersInGame)

        # LAYERS.append(tempWindows)
        
        LAYERS[1][0].draw_tank(pos1,False)#añade los tanques a la capa sin el cañon
        LAYERS[1][1].draw_tank(pos2,False)
        tempWindows.append(surfaceJuego)
        LAYERS.append(tempWindows)

        LAYERS[1][0].draw_tank(pos1,True) #los añade denuevo pero con el cañon
        LAYERS[1][1].draw_tank(pos2,True)
        # LAYERS[2][1][0].draw_tank(positionTank1,True)
        

        return LAYERS #retorna todas las capas  
    
    #crear nueva partida
    
    positionTank1 = (randint(20,WIDTH*0.4),10)
    positionTank2 = (randint(WIDTH*0.6,WIDTH),10)
    layer1 = creaLayer(surfaceJuego,positionTank1,positionTank2) #crea una capa con toda la informacion


    infoPlayer1.drawInfoBlock(surfaceJuego,potencia,angleBullet1,lastPower1,lastAngulo1,range1,alturamaxima1,) #escribe la info del tanque
    infoPlayer2.drawInfoBlock(surfaceJuego,potencia, angleBullet2 + 180, lastPower2, lastAngulo2, range2, alturamaxima2)

    chooseState = []#define los estados de la seleccion de balas
    chooseState.append(1)
    chooseState.append(1)
    #comienzo juego
    
    while run:
        try:
            if actualScreen != 4:
                window.blit(superficies[actualScreen], (0,0))
                pygame.display.update()
            if actualScreen == 4:
                window.blit(superficies[actualScreen], (WIDTH//4,HEIGHT//4))
                pygame.display.update()
            if actualScreen ==2 and minutes >-1: #si la pantalla es la de juego (2) y el tiempo es mayor que -1

                #inicia el juego
                tiempo_actual = pygame.time.get_ticks() / 1000.0
                #chooseMenu1.drawChooseMenu(surfaceJuego,0)
                
                #pygame.display.update()
                if turno == 1:

                    #mover el cañon 1
                    layer1[1][0].moveCannon(layer1[2])
                    layer1[2][1][0].draw_tank(positionTank1,True)
                    layer1[2][1][1].draw_tank(positionTank2,True)
                    angleBullet1 = layer1[1][0].getAngle()
                    infoPlayer1.deleteLast(surfaceJuego)
                    # escrbir informacion jugador 1
                    infoPlayer2.deleteLast(surfaceJuego)
                    infoPlayer1.drawInfoBlock(surfaceJuego,potencia,angleBullet1,lastPower1,lastAngulo1,range1,alturamaxima1)
                    infoPlayer2.drawInfoBlock(surfaceJuego,potencia,angleBullet2,lastPower2,lastAngulo2,range2,alturamaxima2)
                    chooseMenu1.drawChooseMenu(surfaceJuego,chooseState[0],ammoPlayer1)
                    
                elif turno == 2:
                    #mover el cañon 2
                    layer1[1][1].moveCannon(layer1[2])
                    layer1[2][1][1].draw_tank(positionTank2,True)
                    layer1[2][1][0].draw_tank(positionTank1,True)
                    angleBullet2 =180- layer1[1][1].getAngle()
                    infoPlayer1.deleteLast(surfaceJuego)
                    infoPlayer2.deleteLast(surfaceJuego)
                    #escrbir informacion jugador 2
                    infoPlayer1.drawInfoBlock(surfaceJuego,potencia,angleBullet1,lastPower1,lastAngulo1,range1,alturamaxima1)
                    infoPlayer2.drawInfoBlock(surfaceJuego,potencia,angleBullet2,lastPower2,lastAngulo2,range2,alturamaxima2)
                    chooseMenu2.drawChooseMenu(surfaceJuego,chooseState[1],ammoPlayer2)
                    
                
                    
            for event in pygame.event.get():
                
                if event.type == pygame.USEREVENT:
                    if actualScreen == 2:    
                        seconds-=1
                        if seconds <=0:
                            minutes -=1
                            seconds = 59
                        if minutes <0:
                            actualScreen = 3
                            minutes = 5
                            seconds = 59
                            listaBotones.append(drawEnd(surfaceWinner, WIDTH, HEIGHT, 0))
                    
                if event.type == pygame.QUIT:
                    pygame.quit()
                    run = False
                    sys.exit()


                #Botones menu
                elif event.type == pygame.KEYDOWN:
                    if actualScreen == 5:
                        # print('tiendita')
                        # tiendita1.drawShop(surfaceTienda, WIDTH, HEIGHT)
                        if event.key == pygame.K_1:
                            tiendita1.drawShop(surfaceTienda, WIDTH, HEIGHT)
                            
                        if event.key == pygame.K_2:
                            tiendita2.drawShop(surfaceTienda, WIDTH, HEIGHT)
                            
                        if event.key == pygame.K_RETURN:
                            actualScreen = 2
                            print('stats')
                            # statsPlayer1 = tiendita1.getStats()
                            # statsPlayer2 = tiendita2.getStats()
                    if actualScreen == 0:
                        if event.key == pygame.K_RETURN:
                            print('a?')
                            actualScreen = 5
                        if event.key == pygame.K_i:
                            actualScreen = 1
                        if event.key == pygame.K_ESCAPE:
                            run = False
                            pygame.quit()
                            sys.exit()

                    elif actualScreen == 1:
                        if event.key == pygame.K_ESCAPE:
                            actualScreen = 0
                    
                    
                    
                    elif actualScreen == 3:
                        if event.key == pygame.K_r:
                            actualScreen = 0
                            layer1[1][0].setHealth(100)
                            layer1[1][1].setHealth(100)
                            ammoPlayer1 = [3, 10, 3]
                            ammoPlayer2 = [3, 10, 3]
                            chooseState = [0,0]
                            turno = 1
                            positionTank1 = (randint(20,WIDTH*0.4),10)
                            positionTank2 = (randint(WIDTH*0.6,WIDTH),10)
                            layer1 = creaLayer(surfaceJuego,positionTank1,positionTank2)
                        if event.key == pygame.K_q:
                            run = False
                            pygame.quit()
                            sys.exit()    
                        
                    if actualScreen ==4:        
                        if event.key == pygame.K_ESCAPE:
                            actualScreen = 2
                        if event.key == pygame.K_r:
                            actualScreen = 0
                            layer1[1][0].setHealth(100)
                            layer1[1][1].setHealth(100)
                            ammoPlayer1 = [3, 10, 3]
                            ammoPlayer2 = [3, 10, 3]
                            chooseState = [0,0]
                            turno = 1
                            positionTank1 = (randint(20,WIDTH*0.4),10)
                            positionTank2 = (randint(WIDTH*0.6,WIDTH),10)
                            layer1 = creaLayer(surfaceJuego,positionTank1,positionTank2)
                        if event.key == pygame.K_q:
                            run = False
                            pygame.quit()
                            sys.exit()
                        
                        

                        

                
                    elif actualScreen ==2 and minutes >-1:
                        if event.key == pygame.K_ESCAPE:
                                actualScreen = 4
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
                            bullet1 = projectile.Projectile(LAYERS[1][0].end,bulletTypePlayer1,potencia,angleBullet1,window)
                           
                            bullet1.shoot(terrainPoints, player1Hitbox, player2Hitbox,surfaceJuego,LAYERS,tempWindows)
                            
                            
                            #newSurfaceJuego = terrain.drawTerrain()
                            #surfaceJuego.blit(newSurfaceJuego,(0,0))
                            
                            #surfaceJuego.blit(newSurfaceJuego,(0,0))
                            #tempWindows[0].blit(surfaceJuego,(0,0))
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
                                else:
                                    if bullet1.returnHit() == 1: #te avisa si le diste

                                        #("el enemigo aun tiene vida!")
                                        if bulletTypePlayer1 == 1:
                                            layer1[1][1].loseHealth(1)
                                            #("-50")
                                            turno = 2
                                        elif bulletTypePlayer1 == 2:
                                            layer1[1][1].loseHealth(2)
                                            #("-40")
                                            turno = 2
                                        elif bulletTypePlayer1 == 3:
                                            layer1[1][1].loseHealth(3)
                                            #("-30")
                                            turno = 2

                                        if layer1[1][1].getHealth() <= 0:
                                            # listaBotones.append(drawEnd(surfaceWinner, WIDTH, HEIGHT, 1))
                                            ganador = 1
                                            actualScreen = 3
                                            end = True
                                            
                                    elif bullet1.returnHit() == 2:
                                        # listaBotones.append(drawEnd(surfaceWinner, WIDTH, HEIGHT, turno))
                                        ganador = 2
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
                            
                            bullet2 = projectile.Projectile(LAYERS[1][1].end,bulletTypePlayer2,potencia,angleBullet2,window)
                            
                            bullet2.shoot(terrainPoints, player2Hitbox, player1Hitbox,surfaceJuego,LAYERS, tempWindows)
                            
                            ammoPlayer2[bulletTypePlayer2 - 1] -= 1
                            lastAngulo2 = 180 - angleBullet2 

                                lastPower2 = potencia
                                
                                potencia = 0
                                
                                range2 = bullet2.getRange() * -1
                                
                                alturamaxima2 = bullet2.getMaxHeight()
                                
                                if layer1[1][0].getHealth() <= 0:
                                    # listaBotones.append(drawEnd(surfaceWinner, WIDTH, HEIGHT, turno))
                                    ganador = 2
                                    actualScreen = 3
                                    end = True
                                    
                                else:
                                    if bullet2.returnHit() == 1:
                                        #("el enemigo aun tiene vida!")
                                        if bulletTypePlayer2 == 1:
                                            layer1[1][0].loseHealth(1)
                                            #("-50")
                                            turno = 1
                                        elif bulletTypePlayer2 == 2:
                                            layer1[1][0].loseHealth(2)
                                            #("-40")
                                            turno = 1
                                        elif bulletTypePlayer2 == 3:
                                            layer1[1][0].loseHealth(3)
                                            #("-30")
                                            turno = 1
                                        
                                        if layer1[1][0].getHealth() <= 0:
                                            # listaBotones.append(drawEnd(surfaceWinner, WIDTH, HEIGHT, 2))
                                            ganador = 1
                                            actualScreen = 3
                                            end = True

                                    elif bullet2.returnHit() == 2:
                                        # listaBotones.append(drawEnd(surfaceWinner, WIDTH, HEIGHT, turno))
                                        # ganador = 2
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
                # elif end:
                #     ganador = turno
                #     actualScreen = 3
                # elif end:
                #     ganador = turno
                #     actualScreen = 3
                if presionado:
                    potencia_actual = min(tiempo_presion * 20, 200)
                    texto_potencia_actual = fuente.render(f"POWER NOW: {potencia_actual:.1f}", True, "black")
                    surfaceJuego.blit(texto_potencia_actual, (WIDTH*0.4, 620))
                # elif end: 
                #     ganador = turno
                #     actualScreen = 3
                
                clock.tick(60)
                pygame.display.update()

        except (ZeroDivisionError, UnboundLocalError,AttributeError,IndexError):
            textoError = fuente.render("Espera tu turno", True, "black")

game()