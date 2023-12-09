import pygame,random,sys,player,runShop,createMap,params,runMenu,runSettings,runGanador1,runGanador2,runPausa,runPlaymode,runControles,runDificultad,runPausaSettings, runMapsScreen

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

    """game = runGame()#crea el game"""
    
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
    dificultad = 0

    #Jugadores
    jugador1 = player.Player()#crea el jugador 1
    jugador2 = player.Player()#crea el jugador 2
    jugador3 = player.Player()#crea el jugador 3
    listaJugadores = [jugador1, jugador2, jugador3]#lista de jugadores

    while True:#loop principal

        if actualScreen == 0:#Menu
            actualScreen = menu.runMenu()

        elif actualScreen == 1:#Playmode
            playMode = playmode.runPlaymode()
            actualScreen = playMode[0]
            modo = actualScreen[2]

        elif actualScreen == 2:#tienda
            actualScreen = shop.openShop(listaJugadores)#requiere una lista de jugadores

        elif actualScreen == 3:#settings
            settings = settings.runSettings()
            actualScreen = settings[0]
            jugadores = settings[1] #jugadores 
            rondas = settings[2] #rondas

        elif actualScreen == 4:#mapas
            mapBool = mapScreen.runMaps()
            actualScreen = mapBool[0]
            mapa = mapBool[1]
            
        elif actualScreen == 5:#juego
            actualScreen = print('runGame')
            lastScreen = 5
            print("juego") #runGame()

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