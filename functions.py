import params,pygame,sys
from button import Button

def cambiar_tamano_pantalla():
    # if params.size <= 50:  
        # params.screen = pygame.display.set_mode((800,800))
    # else:
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

                        #controles pausa   
                        elif pantalla == 1: 
                            if btn.item == 1:#volver a la pantalla de pausa
                                print('Vuelve a la pantalla de pausa')
                                return 5
                        
                        #ganadores
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
                                print('mapa random')
                            elif btn.item == 6:
                                print('mapa selva')
                            elif btn.item == 7:
                                print('mapa galaxia')
                            elif btn.item == 8:
                                print('mapa nieve')
                            elif btn.item == 9:
                                print('mapa desierto')
                            elif btn.item == 10:
                                print('mapa ciudad')

                        #menu
                        elif pantalla == 4:                           
                            if btn.item == 11:
                                print('starting. . . ')
                                return 6
                            elif btn.item == 12:
                                return 10
                                print('Settings')
                            elif btn.item == 13:
                                return 0
                                print('Controles')
                            elif btn.item == 14:
                                return -1
                                print('salir 2')

                        #pausa
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
                                print('Modo amigos')
                            elif btn.item == 20:
                                print('Modo CPU')
                            elif btn.item == 21:
                                print('Confirmar eleccion')
                                return 9
                        #score
                        if pantalla == 7:
                            if btn.item == 22:
                                print('Confirmar eleccion')
                                return 2

                        #scoreRound
                        if pantalla == 8:
                            if btn.item == 23:
                                print('Confirmar eleccion')
                                return 11

                        #settingsGame
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
                            elif btn.item == 31:
                                print('Disminuir resolucion')
                        
                        #SHOP PROVISIONAL
                        if pantalla == 11:
                            if btn.item == 32:
                                print('Siguiente')
                                return 12                              
                            elif btn.item == 33:
                                print('Comprar')
                            elif btn.item == 34:
                                print('Vender')

                        #PANTALLA PROVISORIA DE JUEGO
                        if pantalla == 12:
                            if btn.item == 35:
                                print('Siguiente')
                                return 8       
                        

        params.screen.blit(background, (0, 0))
        pygame.display.flip()
        clock.tick(60)

def crearButtons(listaProporciones):#resizeButtons:
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
