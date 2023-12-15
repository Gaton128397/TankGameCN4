import params,pygame,sys,random,player,runShop
from button import Button
from createMap import Map
jugadorTest = player.Player()
jugadorTest2 = player.Player()
jugadorTest3 = player.Player()
jugadorTest4 = player.Player()
listaJugadores = [jugadorTest,jugadorTest2,jugadorTest3,jugadorTest4]
def crearMapas():
    desierto = Map(0,pygame.image.load('Mapas/desierto.png'),0,0,(255,255,255))
    selva = Map(1,pygame.image.load('Mapas/selva.png'),0,0,(255,255,255))
    galaxia = Map(2,pygame.image.load('Mapas/galaxia.png'),0,0,(255,255,255))
    nieve = Map(3,pygame.image.load('Mapas/nieve.png'),0,0,(255,255,255))
    ciudad = Map(4,pygame.image.load('Mapas/ciudad.png'),0,0,(255,255,255))
    return (selva,galaxia,nieve,desierto,ciudad)

def cambiar_tamano_pantalla():
    params.screen = pygame.display.set_mode((params.size*16,params.size*9))

def checkResize(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_SPACE:
            if params.size <= 120:
                params.size+=10
            cambiar_tamano_pantalla()
        if event.key == pygame.K_RETURN:
            if params.size >= 50:
                params.size-=10
            cambiar_tamano_pantalla()

def run(img,propBotonesPantalla,pantalla):
    clock = pygame.time.Clock()
    img1 = img
    screen = pantalla
    mapa = None
    modo = None

    while True:
        
        background = pygame.image.load(img1)
        background = pygame.transform.scale(background, (params.size*16, params.size*9))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            checkResize(event)
            for btns in crearButtons(propBotonesPantalla):
                for btn in btns:
                    if btn.check_click(event):
                        
                        #controles menu
                        if pantalla == 0:
                            if btn.item == 0: #volver al menu
                                print('volver al menu')
                                return 4

                        #controles pausa   #METER EN JUEGO GASTON
                        elif pantalla == 1: 
                            if btn.item == 1:#volver a la pantalla de pausa
                                print('Vuelve a la pantalla de pausa')
                                return 5
                        
                        #ganadores    #METER EN JUEGO GASTON
                        elif pantalla == 2:
                            if btn.item == 2:
                                print('Volver al menu')
                                return 4
                                
                            elif btn.item == 3:
                                print('Cierra el juego')
                                return -1
                        
                        #mapas
                        elif pantalla == 3:
                            if btn.item == 4:
                                print('Confirmar seleccion')
                                return 11
                            elif btn.item == 5:
                                mapa = random.choice(crearMapas())
                                print('mapa random')
                            elif btn.item == 6:
                                mapa = crearMapas()[0]
                                print('mapa selva')
                            elif btn.item == 7:
                                mapa = crearMapas()[1]
                                print('mapa galaxia')
                            elif btn.item == 8:
                                mapa = crearMapas()[2]
                                print('mapa nieve')
                            elif btn.item == 9:
                                mapa = crearMapas()[3]
                                print('mapa desierto')
                            elif btn.item == 10:
                                mapa = crearMapas()[4]
                                print('mapa ciudad')

                        #menu
                        elif pantalla == 4:                           
                            if btn.item == 11:
                                print('starting. . . ')
                                return 6
                            elif btn.item == 12:
                                print('Settings')
                                return 10                               
                            elif btn.item == 13:
                                print('Controles')
                                return 0
                            elif btn.item == 14:
                                print('salir')
                                return -1
                                

                        #pausa     #METER EN JUEGO GASTON
                        elif pantalla == 5:
                            if btn.item == 15:
                                print('Volver al juego')
                                return 12
                            elif btn.item == 16:
                                print('Vuelve al menu')
                                return 4
                            elif btn.item == 17:
                                print('Controles pausa')
                                return 1
                            elif btn.item == 18:
                                print('salir')
                                return -1
                            
                        #playMode
                        if pantalla == 6:
                            if btn.item == 19:
                                modo = 0
                                print('Modo amigos')
                            elif btn.item == 20:
                                modo = 1
                                print('Modo CPU')
                            elif btn.item == 21:
                                if modo !=None:
                                    print('Confirmar eleccion')
                                    return 9
                                
                        #score      #METER EN JUEGO GASTON
                        if pantalla == 7:
                            if btn.item == 22:
                                print('Confirmar eleccion')
                                return 2

                        #scoreRound     #METER EN JUEGO GASTON
                        if pantalla == 8:
                            if btn.item == 23:
                                print('Confirmar eleccion')
                                return 11

                        #settingsGame     #METER EN JUEGO GASTON
                        if pantalla == 9:
                            if btn.item == 24:
                                print('Confirmar eleccion')
                                return 3
                            elif btn.item == 25:
                                print('Aumentar Jugadores')
                            elif btn.item == 26:
                                print('Disminuir Jugadores')
                            elif btn.item == 27:
                                print('Aumentar Rondas')
                            elif btn.item == 28:
                                print('Disminuir Rondas')

                        #settingsMenu
                        if pantalla == 10:
                            if btn.item == 29:
                                print('Confirmar eleccion')
                                return 4                              
                            elif btn.item == 30:
                                print('Aumentar resolucion')
                                if params.size < 120:
                                    params.size+=10
                                    cambiar_tamano_pantalla()
                            elif btn.item == 31:
                                if params.size > 50:
                                    params.size-=10
                                    cambiar_tamano_pantalla()
                                print('Disminuir resolucion')
                        
                        #SHOP PROVISIONAL      #METER EN JUEGO GASTON
                        if pantalla == 11:     
                            pantalla = runShop.openShop(listaJugadores)
                            return 12

                        #PANTALLA PROVISORIA DE JUEGO     #METER EN JUEGO GASTON
                        if pantalla == 12:
                            if btn.item == 33:
                                print('Siguiente')
                                return 8       
                        

        params.screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(60)

def crearButtons(listaProporciones):
    #resizeButtons
    listaBotonesPantallas = []
    pantalla = []
    ID = 0
    x= 0
    for screen in listaProporciones:
        for prop in screen:
            boton = Button(prop[x],prop[x+1],prop[x+2],prop[x+3],ID)
            pantalla.append(boton)
            ID+=1
        listaBotonesPantallas.append(pantalla)
        pantalla=[]
    return listaBotonesPantallas
