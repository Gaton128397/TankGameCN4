import pygame,random,sys,player,runShop,createMap,params,runMenu,runSettings,runGanador1,runGanador2,runPausa,runPlaymode,runControles, runMapsScreen,runGame,functions, scoreBoard

#0 = menu
#1 = playmode
#2 = shop
#3 = configuracion
#4 = mapas
#5 = juego
#6 = pausa
#7 = controles
#8 = ganador1
#9 = ganador2
#10 = dificultad
def getColores(listaJugadores):
    colores = []
    for jugador in listaJugadores:
        colores.append(jugador.tanque.color)
    return colores

def mainScreen():#Logica de mainScreen()

    shop = runShop.Shop()#crea shop
    #game
    pygame.init()#inicia pygame
    pygame.display.set_caption('TANKS')#titulo de la ventana
    clock = pygame.time.Clock()#crea el reloj
    
    #variables de flujo
    actualScreen = 0 #pantalla actual
    lastScreen = 0 #pantalla anterior
    mapa = None #Ninguno
    modo = 1 #CPU 
    jugadores = 2 #jugadores
    ia = False
    partidas = 3 #rondas
    run = True
    dificultad = 0

    #jugadores
    # resetTanks = functions.loadPlayers(listaJugadores,screen)
    
    
    while True:#loop principal
        if actualScreen == 0:#Menu
            actualScreen = runMenu.runMenu()

        elif actualScreen == 1:#Playmode
            playMode = runPlaymode.runPlaymode() #amigo o cpu
            if playMode == 'Amigos':
                ia = False
            else:
                ia = True    
            actualScreen+=1 #pasa a settings
            

        elif actualScreen == 2:#settings
            settingsInfo= runSettings.runSettings()
            actualScreen,jugadores,rondas = settingsInfo[0],settingsInfo[1],settingsInfo[2]
            # actualScreen = 5
        elif actualScreen == 3:#juego
            partidaActual = 0
            listaJugadores = []
            
            resetTanks = functions.loadPlayers(listaJugadores,params.screen,ia)
            coloresJuagadores = getColores(listaJugadores)
            winner = None
            mapaReturn = runMapsScreen.runMaps() #recibe un mapa
            if mapaReturn[0] == 0:
                actualScreen = 0
            elif mapaReturn[0] == 2:
                actualScreen = 2
            elif mapaReturn[0] == 4:
                mapa = mapaReturn[1]
            if mapa != None:
                while partidaActual < partidas:
                    functions.resetTanks(listaJugadores,resetTanks,params.screen)
                    functions.resetIventario(listaJugadores)
                    shop.openShop(listaJugadores)
                    
                    game = runGame.gameLogic(params.screen,listaJugadores,mapa)
                    game.run(clock)
                    partidaActual += 1
                    print ("partida actual: ",partidaActual)
                summary = scoreBoard.scoreBoard(listaJugadores,params.screen, coloresJuagadores,"imgs/pantallas/scoreGeneral.png",True)
                summary.sb_run()
                print("ganador")

        elif actualScreen == 7: #controles
            actualScreen = runControles.runControles()
            
        elif actualScreen == 12:
            pygame.quit()
            sys.exit()

mainScreen()