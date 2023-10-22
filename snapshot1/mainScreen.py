from random import randint
from menu import Menu
import pygame,projectile,tank,terreno,time,sys,chooseMenu, params, drawFunctions
WIDTH,HEIGHT = params.WIDTH,params.HEIGHT
hills = []
canyons = []
potencia = 0
tiempo_presionado = 0
tiempo_anterior = 0
presionado = False

#choose bullet 
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------    


#Game
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def game():
    pygame.init()
    window = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("Tank v Tank")
    menu1 = Menu(window,WIDTH,HEIGHT)
    start = 0
    if start ==0:
        menu1.draw_menu()
        pygame.display.update()
    
    fuente = pygame.font.Font(None, 30)
    fuente2 = pygame.font.Font(None, 60)

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
    potencia1 = 0
    potencia2 = 0
    angulo1 = 0
    angulo2 = 0
    alturamaxima1 = 0
    alturamaxima2 = 0
    range1 = 0
    range2 = 0
    end = False
    playersInGame = []
    playersInGame.append(player1)
    playersInGame.append(player2)
    LAYERS = [] #indice 0 terreno y background, indice 1 jugadores
    LAYERS.append(terrain.drawTerrain())
    LAYERS.append(playersInGame)
    window.blit(LAYERS[0],(0,0))
    LAYERS[1][0].draw_tank(False)
    LAYERS[1][1].draw_tank(False)
    run = True
    menuChoose = chooseMenu.ChooseMenu(window,WIDTH,HEIGHT)
    #menuChoose.choosing()
    tempWindow = window.copy()
    while run:
        try:
            
            if start ==1:
                
                tiempo_actual = pygame.time.get_ticks() / 1000.0
                menuChoose.choosing()
                
                if turno == 1:
                    player1.moveCannon(tempWindow)
                    
                    
                    angleBullet1 = player1.getAngle()
                    
                elif turno ==2:
                    
                    positionBullet2 = player2.moveCannon()
                    angleBullet2 = 180-player2.getAngle()
                    #projectileSize2 = menuChoose.choosing()
                    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu1.buttonPlay.collidepoint(event.pos):

                        start = 1
                    elif menu1.buttonExit.collidepoint(event.pos):
                        run = False
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        print(1)
                    if event.key == pygame.K_SPACE:
                        tiempo_presionado = tiempo_actual
                        presionado = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_SPACE:
                        if tiempo_actual - tiempo_presionado >= 10.0:  # MÁXIMO 5 SEGUNDOS PARA LLEGAR A 100
                            potencia = 200
                        else:
                            potencia = min((tiempo_actual - tiempo_presionado) * 20, 200)

                        tiempo_anterior = tiempo_actual
                        presionado = False
                        if turno == 1:
                            bullet1 = projectile.Projectile(player1.end,1,potencia,angleBullet1,window)
                            #bullet1 = projectile.Projectile(positionBullet1,potencia,angleBullet1,window)
                            #deleteBullet = projectile.Projectile(positionBullet1,1,potencia,angleBullet1,window)
                            bullet1.shoot(terrainPoints,player1Hitbox,player2Hitbox,window) 
                            
                            potencia1 = potencia
                            angulo1 = player1.getAngle()
                            alturamaxima1 = bullet1.getMaxHeight()
                            range1 = bullet1.getRange()
                            ##(potencia1)
                            
                            if bullet1.returnHit() ==1:
                                player2.draw_tank('lightblue')
                                window.fill('gold')
                                textoGanar = fuente2.render(f'GANA PLAYER {turno}', True, 'black')
                                time.sleep(0.2)
                                window.blit(textoGanar, (400, 300))
                                end = True
                                
                            elif bullet1.returnHit() ==2:
                                player2.draw_tank('lightblue')
                                window.fill('gold')
                                textoGanar = fuente2.render(f'GANA PLAYER {2}', True, 'black')
                                time.sleep(0.2)
                                window.blit(textoGanar, (400, 300))
                                end = True
                            else:
                                #deleteBullet.delete(terrainPoints,player1Hitbox,player2Hitbox)
                                turno = 2

                        elif turno == 2:

                            bullet2 = projectile.Projectile(positionBullet2,2,potencia,angleBullet2,window) 
                            deleteBullet2 = projectile.Projectile(positionBullet2,2,potencia,angleBullet2,window) 
                            bullet2.shoot(terrainPoints,player2Hitbox,player1Hitbox) 
                            
                            potencia2 = potencia
                            angulo2 = player2.getAngle()
                            alturamaxima2 = bullet2.getMaxHeight()
                            range2 = bullet2.getRange()
                            ##(potencia2)

                            if bullet2.returnHit() ==1:
                                player1.draw_tank('lightblue')
                                window.fill('gold')
                                textoGanar = fuente2.render(f'GANA PLAYER {turno}', True, 'black')
                                time.sleep(0.2)
                                window.blit(textoGanar, (400, 300))
                                end = True

                            elif bullet2.returnHit() ==2:
                                player1.draw_tank('lightblue')
                                window.fill('gold')
                                textoGanar = fuente2.render(f'GANA PLAYER {1}', True, 'black')
                                time.sleep(0.2)
                                window.blit(textoGanar, (400, 300))
                                end = True
                            else:
                                deleteBullet2.delete(terrainPoints,player2Hitbox,player1Hitbox)
                                turno = 1
            if start == 1:
                pygame.draw.rect(window, 'lightblue', (40,20,350, 70))            
                pygame.draw.rect(window, 'grey', (50, 50, 200, 20))  

            #pygame.draw.rect(window, 'green', ((600,20),(200, 100)),0)
                if presionado:
                    tiempo_presion = tiempo_actual - tiempo_presionado
                    llenado = min(tiempo_presion * 20, 200)  # Ajustamos el llenado
                    pygame.draw.rect(window, 'red', (50, 50, llenado, 20))
                elif end:
                    window.fill('gold')
                    textoGanar = fuente2.render(f'GANA PLAYER {turno}', True, 'black')
                    time.sleep(0.2)
                    window.blit(textoGanar, (400, 300))
                if turno ==1:
                    texto_potencia = fuente.render(f'LAST POWER PLAYER {turno}: {potencia1:.1f}', True, 'black')
                    window.blit(texto_potencia, (50, 30))
                    
                    textoRange1 = fuente.render(f'LAST RANGE PLAYER {turno}: {range1:.1f}', True, 'black')
                    pygame.draw.rect(window, (255, 213, 158), (50,580,500, 50))
                    window.blit(textoRange1, (50, 590))

                    textoAngulo = fuente.render(f'LAST ANGLE PLAYER {turno}: {angulo1:.1f}', True, 'black')
                    pygame.draw.rect(window, (255, 213, 158), (50,620,300, 50))
                    window.blit(textoAngulo, (50, 630))
                    textoAltura2 = fuente.render(f'LAST HEIGHT PLAYER {turno}: {alturamaxima2:.1f}', True, 'black')
                    pygame.draw.rect(window, (255, 213, 158), (50,660,300, 50))
                    window.blit(textoAltura2, (50, 670))

                if turno ==2:
                    
                    texto_potencia = fuente.render(f'LAST POWER PLAYER {turno}: {potencia2:.1f}', True, 'black')
                    window.blit(texto_potencia, (50, 30))
                    
                    textoRange2 = fuente.render(f'LAST RANGE PLAYER {turno}: {-1*range2:.1f}', True, 'black')
                    pygame.draw.rect(window, (255, 213, 158), (900,580,500, 50))
                    window.blit(textoRange2, (900, 590))

                    textoAngulo2 = fuente.render(f'LAST ANGLE PLAYER {turno}: {angulo2:.1f}', True, 'black')
                    pygame.draw.rect(window, (255, 213, 158), (900,620,300, 50))
                    window.blit(textoAngulo2, (900, 630))

                    textoAltura2 = fuente.render(f'LAST HEIGHT PLAYER {turno}: {alturamaxima2:.1f}', True, 'black')
                    pygame.draw.rect(window, (255, 213, 158), (900,660,300, 50))
                    window.blit(textoAltura2, (900, 670))
            
                elif end:
                    
                    window.fill('gold')
                    textoGanar = fuente2.render(f'GANA PLAYER {turno}', True, 'black')
                    time.sleep(0.2)
                    window.blit(textoGanar, (400, 300))

                if presionado:
                    potencia_actual = min(tiempo_presion * 20, 200)
                    
                    texto_potencia_actual = fuente.render(f'POWER NOW: {potencia_actual:.1f}', True, 'black')
                    window.blit(texto_potencia_actual, (50, 70))
                elif end:
                    window.fill('gold')
                    textoGanar = fuente2.render(f'GANA PLAYER {turno}', True, 'black')
                    time.sleep(0.2)
                    window.blit(textoGanar, (400, 300))
                                
                clock.tick(60)
                pygame.display.update()
        except ZeroDivisionError:
            textoError = fuente.render("Espera tu turno", True, 'black')
            
game()