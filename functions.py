import math, params, player, nTank, random, runGame, gameScreens
import pygame,sys,runShop
from button import Button
from createMap import Map
def frange(start, final, increment):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + increment 
    return numbers


def draw_trajectory(u, theta, gravity, xPositions, yPositions,pos,wind):
    WIDTH = params.size*16
    theta = math.radians(theta)
    # Time of flight
    t_flight = 2 * u * math.sin(theta) / gravity
    intervals = frange(0, t_flight+WIDTH, 0.05) 

    for t in intervals:
        xPositions.append(pos[0]+ (u * math.cos(theta) * t) + (wind * t))
        yPositions.append(pos[1]+ (u * math.sin(theta) * t - 0.5 * gravity * t *t))

def divideScreenIn9(width,height):    
    x1 = width*1/3
    y1 = height*1/3
    x2 = width*2/3
    y2 = height*2/3
    x3 = width
    y3 = height
    listaTercios = [(x1,y1),(x2,y1),(x3,y1),(x1,y2),(x2,y2),(x3,y2),(x1,y3),(x2,y3),(x3,y3)]
    return listaTercios
    
def calcular_distancia(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2
    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distancia

def calcularDMG(distancia, dano_maximo, radio,tipoProyectil):
    if not tipoProyectil == 3:
        if distancia < radio*0.4:
            return dano_maximo
        elif (distancia > radio*0.4) and (distancia < radio*0.8):
            return dano_maximo*0.5
        else:
            return dano_maximo*0.2
    else:
        if distancia < radio*0.8:
            return dano_maximo
        else:
            return dano_maximo*0.5
    
def loadPlayers(listaJugadores,window,ia):
    resetTanks = []
    if ia == False:
        for i in range(params.playersNumber):
            listaJugadores.append(player.Player())
    elif ia == True:
        choosePlayer = False
        for i in range(params.playersNumber):
            if choosePlayer:
                randomPlayer = random.randint(0,1)
                if randomPlayer == 0:
                    listaJugadores.append(player.Player())
                    choosePlayer = False
                else:
                    listaJugadores.append(player.Player())
                    listaJugadores[i].ia = True
            else:
                listaJugadores.append(player.Player())
                listaJugadores[i].ia = True
                
    colores = ["red", "green", "blue", "yellow", "orange", (128, 0, 128)]
    for i in range(len(listaJugadores)):
        choise = random.randint(0,len(colores)-1)
        listaJugadores[i].asignTank(nTank.Tank(colores[choise],window,i))
        resetTanks.append([colores[choise],i])
        colores.pop(choise)
    return resetTanks

def resetTanks(listaJugadores,paramsTanks,window):
    for i in range(len(listaJugadores)):
        listaJugadores[i].asignTank(None)
    for i in range(len(listaJugadores)):
        listaJugadores[i].asignTank(nTank.Tank(paramsTanks[i][0],window,paramsTanks[i][1]))

def anhadirDiezmo(listaJugadores):
    diezmo = 10000
    for i in range(len(listaJugadores)):
        listaJugadores[i].money += diezmo
        if listaJugadores[i].selfKill == True:
            listaJugadores[i].money -= 5000
            listaJugadores[i].selfKill = False
        else:
            listaJugadores[i].money += (5000)*listaJugadores[i].kda[0]    
        listaJugadores[i].generalkda[0] += listaJugadores[i].kda[0]
        listaJugadores[i].kda[0] = 0
        listaJugadores[i].generalkda[1] += listaJugadores[i].kda[1]
        listaJugadores[i].kda[1] = 0
            
jugadorTest = player.Player()
jugadorTest2 = player.Player()
jugadorTest3 = player.Player()
jugadorTest4 = player.Player()
listaJugadores = [jugadorTest,jugadorTest2,jugadorTest3,jugadorTest4]
def crearMapas():
    desierto = Map(0,pygame.image.load('Mapas/desierto.png'),9.5,("#C9B26D"))
    selva = Map(1,pygame.image.load('Mapas/selva.png'),8,("#003E30"))
    galaxia = Map(2,pygame.image.load('Mapas/galaxia.png'),5.2,("#896DC9"))
    nieve = Map(3,pygame.image.load('Mapas/nieve.png'),10.5,("#CEFDFF"))
    ciudad = Map(4,pygame.image.load('Mapas/ciudad.png'),9.8,("#868686"))
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
            #checkResize(event)
            for btns in crearButtons(propBotonesPantalla):
                for btn in btns:
                    if btn.check_click(event):
                        
                        #controles menu
                        if pantalla == 0:
                            if btn.item == 0: #volver al menu
                                #print('volver al menu')
                                return 4

                        #controles pausa   #METER EN JUEGO GASTON
                        elif pantalla == 1: 
                            if btn.item == 1:#volver a la pantalla de pausa
                                #print('Vuelve a la pantalla de pausa')
                                return 5
                        
                        #ganadores    #METER EN JUEGO GASTON
                        elif pantalla == 2:
                            if btn.item == 2:
                                #print('Volver al menu')
                                return 4
                                
                            elif btn.item == 3:
                                #print('Cierra el juego')
                                return -1
                        
                        #mapas
                        elif pantalla == 3:
                            if btn.item == 4:
                                #print('Confirmar seleccion')
                                #print('parte del juego')
                                return 12
                            elif btn.item == 5:
                                params.mapa = random.choice(crearMapas())
                                #print('mapa random')
                            elif btn.item == 6:
                                params.mapa = crearMapas()[0]
                                #print('mapa selva')
                            elif btn.item == 7:
                                params.mapa = crearMapas()[1]
                                #print('mapa galaxia')
                            elif btn.item == 8:
                                params.mapa = crearMapas()[2]
                                #print('mapa nieve')
                            elif btn.item == 9:
                                params.mapa = crearMapas()[3]
                                #print('mapa desierto')
                            elif btn.item == 10:
                                params.mapa = crearMapas()[4]
                                #print('mapa ciudad')

                        #menu
                        elif pantalla == 4:                           
                            if btn.item == 11:
                                #print('starting. . . ')
                                return 6
                            elif btn.item == 12:
                                #print('Settings')
                                return 10                               
                            elif btn.item == 13:
                                #print('Controles')
                                return 0
                            elif btn.item == 14:
                                #print('salir')
                                return -1
                                

                        #pausa     #METER EN JUEGO GASTON
                        elif pantalla == 5:
                            if btn.item == 15:
                                #print('Volver al juego')
                                return 12
                            elif btn.item == 16:
                                #print('Vuelve al menu')
                                return 4
                            elif btn.item == 17:
                                #print('Controles pausa')
                                return 1
                            elif btn.item == 18:
                                #print('salir')
                                return -1
                            
                        #playMode
                        if pantalla == 6:
                            if btn.item == 19:
                                modo = 0
                                #print('Modo amigos')
                            elif btn.item == 20:
                                modo = 1
                                #print('Modo CPU')
                            elif btn.item == 21:
                                if modo !=None:
                                    #print('Confirmar eleccion')
                                    return 9
                                
                        #score      #METER EN JUEGO GASTON
                        if pantalla == 7:
                            if btn.item == 22:
                                #print('Confirmar eleccion')
                                return 2

                        #scoreRound     #METER EN JUEGO GASTON
                        if pantalla == 8:
                            if btn.item == 23:
                                pass
                                #print('Confirmar eleccion')
                                #print('parte del juego')

                        #settingsGame     #METER EN JUEGO GASTON
                        if pantalla == 9:
                            if btn.item == 24:
                                print('Confirmar eleccion')
                                return 3
                            elif btn.item == 25:
                                params.playersNumber += 1
                                print('Aumentar Jugadores')
                            elif btn.item == 26:
                                # Verificar si hay al menos 2 jugadores antes de disminuir
                                if params.playersNumber > 2:
                                    params.playersNumber -= 1
                                    print('Disminuir Jugadores')
                                else:
                                    print('No se puede disminuir más. Mínimo 2 jugadores.')
                            elif btn.item == 27:
                                params.roundNumber += 1
                                print('Aumentar Rondas')
                            elif btn.item == 28:
                                # Verificar si hay al menos 1 ronda antes de disminuir
                                if params.roundNumber > 1:
                                    params.roundNumber -= 1
                                    print('Disminuir Rondas')
                                else:
                                    print('No se puede disminuir más. Mínimo 1 ronda.')

                        #settingsMenu
                        if pantalla == 10:
                            if btn.item == 29:
                                #print('Confirmar eleccion')
                                return 4                              
                            elif btn.item == 30:
                                #print('Aumentar resolucion')
                                if params.size < 120:
                                    params.size+=10
                                    cambiar_tamano_pantalla()
                            elif btn.item == 31:
                                if params.size > 50:
                                    params.size-=10
                                    cambiar_tamano_pantalla()
                                #print('Disminuir resolucion')
                        
                        #SHOP PROVISIONAL      #METER EN JUEGO GASTON
                        if pantalla == 11:     
                            #pantalla = runShop.openShop(listaJugadores)
                            #print('esta es la pantalla 11')
                            return 12

                        #PANTALLA PROVISORIA DE JUEGO     #METER EN JUEGO GASTON
        if pantalla == 12:
            #print('Juego')
            window = params.screen
            partidosActuales = 0
            listaJugadores = []
            ia = False
            variableReseteo = loadPlayers(listaJugadores,window,ia)
            while partidosActuales < params.roundNumber:
                #mapa = ["Mapas/galaxia.png",9.8]
                #mapa = crearMapas()[random.randint(0,4)]
                resetTanks(listaJugadores,variableReseteo,window)
                anhadirDiezmo(listaJugadores)
                runShop.openShop(listaJugadores)
                #player.Player().comprarIa() #solo compra si es IA
                gameScreens.pantallaEmpiezaJuego(window)
                game = runGame.gameLogic(window,listaJugadores,params.mapa)
                game.run(clock)
                partidosActuales += 1
            return 4
        #print(pantalla)
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
