import pygame,random,sys,player,runShop,createMap,params,runMenu,runSettings,runGanador1,runGanador2,runPausa,runPlaymode,runControles,runDificultad,runPausaSettings, runMapsScreen,runGame,functions

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

def mainScreen():#Logica de mainScreen()

    #screen
    menu = runMenu.Menu()#crea el menu
    playmode = runPlaymode.Playmode()#crea el playmode
    shop = runShop.Shop()#crea el shop
    settings = runSettings.Settings()#crea el settings
    mapScreen = runMapsScreen.Maps()#crea el maps
    pausa = runPausa.Pausa()#crea el pausa
    controles = runControles.Controles()#crea el controles
    ganador1 = runGanador1.Ganador1()#crea el ganador1
    ganador2 = runGanador2.Ganador2()#crea el ganador2
    dificultad = runDificultad.Difficulty()#crea el dificultad

    #game
    pygame.init()#inicia pygame
    pygame.display.set_caption('TANKS')#titulo de la ventana
    screen = pygame.display.set_mode((params.WIDTH, params.HEIGHT))#crea la ventana
    clock = pygame.time.Clock()#crea el reloj
    
    #variables de flujo
    actualScreen = 0 #pantalla actual
    lastScreen = 0 #pantalla anterior
    mapa = None #Ninguno
    modo = 1 #CPU 
    jugadores = 2 #jugadores
    
    rondas = 1 #rondas
    run = True
    dificultad = 0

    #jugadores
    # resetTanks = functions.loadPlayers(listaJugadores,screen)
    params.WIDTH = 1200
    params.HEIGHT = 700
    screen = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    while True:#loop principal

        if actualScreen == 0:#Menu
            actualScreen = menu.runMenu()

        elif actualScreen == 1:#Playmode
            playMode = playmode.runPlaymode()
            actualScreen = playMode[0]
            modo = playMode[1]

        #elif actualScreen == 2:#tienda
            #actualScreen = shop.openShop(listaJugadores)#requiere una lista de jugadores

        elif actualScreen == 3:#settings
            settingsBool = settings.runSettings()
            actualScreen = settingsBool[0]
            #jugadores = settingsBool[1] #jugadores 
            #rondas = settingsBool[2] #rondas

        elif actualScreen == 4:#mapas
            print("mapas")
            mapBool = mapScreen.runMaps()
            actualScreen = mapBool[0]
            mapa = mapBool[1]
            
        elif actualScreen == 5:#juego
            rondaActual = 0
            listaJugadores = []
            ia = True
            resetTanks = functions.loadPlayers(listaJugadores,screen,ia)
            winner = None
            while rondaActual < rondas:
                functions.resetTanks(listaJugadores,resetTanks,screen)
                functions.resetIventario(listaJugadores)
                abierta = shop.openShop(listaJugadores)
                if abierta == 1:
                    game = runGame.gameLogic(screen,listaJugadores,mapa)
                    game.run(clock)
                    rondaActual += 1
            print("ganador")

        elif actualScreen == 6:#pausa
            pausa_result = pausa.runPausa(lastScreen)
            actualScreen = pausa_result[0]

        elif actualScreen == 7: #controles
            actualScreen = controles.runControles(lastScreen)
            
        elif actualScreen == 8:
            ganador1_result = ganador1.runGanador1()

        elif actualScreen == 9:
            ganador2_result = ganador2.runGanador2()
            
        elif actualScreen == 10:
            dificulty = dificultad.runDificultad()
            actualScreen = dificulty[0]
            dificultad = dificulty[1]

        elif actualScreen == 12:
            pygame.quit()
            sys.exit()

mainScreen()