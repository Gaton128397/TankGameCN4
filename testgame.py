import pygame,random,sys,player,runShop,params,runMenu,runSettings,runGanador1,runGanador2,runPausa,runPlaymode,runControles,runDificultad,runPausaSettings

def tstgm():#Logica de mainScreen()
    jugadorTest = player.Player()
    jugadorTest2 = player.Player()
    jugadorTest3 = player.Player()
    jugadorTest4 = player.Player()
    listaJugadores = [jugadorTest,jugadorTest2,jugadorTest3,jugadorTest4]

    clock = pygame.time.Clock()
    window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))

    menu = runMenu.Menu(window)#crea el menu
    shop = runShop.Shop(window)#crea la tienda
    settings = runSettings.settings(window)#crea la configuracion
    playmode = runPlaymode.Playmode(window)#crea el modo de juego
    ganador1 = runGanador1.Ganador1(window)#crea el ganador1
    ganador2 = runGanador2.Ganador2(window)#crea el ganador2
    pausa = runPausa.Pausa(window)#crea la pausa
    controles = runControles.Controles(window)#crea los controles
    screen = 0
    run = True
    while run:
        if screen == 0:
            print('menu')
            screen = menu.runMenu()
        if screen == 1:
            print('playmode')
            screen = playmode.runPlaymode()            
        if screen == 2:
            print('shop')
            screen = shop.openShop(listaJugadores)
        if screen == 3:
            print('controles')
            screen = controles.runControles()
        if screen == 3.5:
            print('pausa Settings')
            screen = pausa.runPausaSettings()

        if screen == 4:
            print('settings')
            screen = settings.runSettings()
        if screen == 5:
            print('ganador 1')
            screen = ganador1.runGanador1()
        if screen == 6:
            print('ganador 2')
            screen = ganador2.runGanador2()
        if screen == 7:
            print('running game')
        if screen == 8:
            screen = pausa.runPausa()
        if screen == 10:
            img = params.bgMapas
            window.blit(img,(0,0))
            pygame.display.flip()
            
tstgm()