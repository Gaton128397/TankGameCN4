import math, params, player, nTank, random, runGame, gameScreens, drawFunctions, gameScreens, scoreBoard
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
    colores = ["red", "green", "blue", "yellow", "orange", (128, 0, 128)]
    for i in range(params.playersNumber):
        choise = random.randint(0,len(colores)-1)
        resetTanks.append([colores[choise],i])
        colores.pop(choise)
    
    if ia == False:
        for i in range(params.playersNumber):
            listaJugadores.append(player.Player())
    elif ia ==True:
        for i in range(params.playersNumber):
            listaJugadores.append(player.Player())
            listaJugadores[i].ia = True
        notIa = random.randint(0,len(listaJugadores)-1)
        listaJugadores[notIa].ia = False  

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
    

    while True:
        
        background = pygame.image.load(img1)
        background = pygame.transform.scale(background, (params.size*16, params.size*9))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            for btns in crearButtons(propBotonesPantalla):
                for btn in btns:
                    if btn.check_click(event):
                        
                        #controles menu
                        if pantalla == 0:
                            if btn.item == 0: 
                                return 4

                        #controles pausa 
                        elif pantalla == 1: 
                            if btn.item == 1:
                                return 5
                        
                        #ganadores  
                        elif pantalla == 2:
                            if btn.item == 2:
                                return 4
                                
                            elif btn.item == 3:
                                return -1
                        
                        #mapas
                        elif pantalla == 3:
                            if btn.item == 4:
                                if params.mapa != None:
                                    return 12
                            elif btn.item == 5:
                                params.mapa = random.choice(crearMapas())
                                #('mapa random')
                            elif btn.item == 6:
                                params.mapa = crearMapas()[0]
                                #('mapa selva')
                            elif btn.item == 7:
                                params.mapa = crearMapas()[1]
                                #('mapa galaxia')
                            elif btn.item == 8:
                                params.mapa = crearMapas()[2]
                                #('mapa nieve')
                            elif btn.item == 9:
                                params.mapa = crearMapas()[3]
                                #('mapa desierto')
                            elif btn.item == 10:
                                params.mapa = crearMapas()[4]
                                #('mapa ciudad')

                        #menu
                        elif pantalla == 4:                           
                            if btn.item == 11:
                                return 6
                            elif btn.item == 12:
                                return 10                               
                            elif btn.item == 13:
                                return 0
                            elif btn.item == 14:
                                return -1
                                

                        #pausa 
                        elif pantalla == 5:
                            if btn.item == 15:
                                return 12
                            elif btn.item == 16:
                                return 4
                            elif btn.item == 17:
                                return 1
                            elif btn.item == 18:
                                return -1
                            
                        #playMode
                        if pantalla == 6:
                            if btn.item == 19:
                                params.modo = 0
                                #('Modo amigos')
                            elif btn.item == 20:
                                params.modo = 1
                                #('Modo CPU')
                            elif btn.item == 21:
                                if params.modo !=None:
                                    return 9
                                
                        #score
                        if pantalla == 7:
                            if btn.item == 22:
                                return 2

                        #scoreRound
                        if pantalla == 8:
                            if btn.item == 23:
                                pass

                        #settingsGame
                        if pantalla == 9:
                            if btn.item == 24:
                                return 3
                            elif btn.item == 25:
                                if params.playersNumber < 6:
                                    params.playersNumber += 1
                            elif btn.item == 26:
                                if params.playersNumber > 2:
                                    params.playersNumber -= 1
                                else:
                                    print('No se puede disminuir más. Mínimo 2 jugadores.')
                            elif btn.item == 27:
                                if params.roundNumber < 20:
                                    params.roundNumber += 1
                            elif btn.item == 28:
                                if params.roundNumber > 1:
                                    params.roundNumber -= 1
                                else:
                                    print('No se puede disminuir más. Mínimo 1 ronda.')

                        #settingsMenu
                        if pantalla == 10:
                            if btn.item == 29:
                                return 4                              
                            elif btn.item == 30:
                                if params.size < 120:
                                    params.size+=10
                                    cambiar_tamano_pantalla()
                            elif btn.item == 31:
                                if params.size > 50:
                                    params.size-=10
                                    cambiar_tamano_pantalla()
                        
                        #SHOP 
                        if pantalla == 11:     
                            return 12

        #JUEGO
        if pantalla == 9:
            width = params.size*16
            height = params.size*9
            surfaceIndicadorJugadores = pygame.Surface((width*0.03,height*0.05))
            surfaceIndicadorJugadores.fill((255,255,255))
            surfaceIndicadorJugadores.set_alpha()
            surfaceIndicadorJugadores.set_colorkey((255,255,255))
            surfaceIndicadorRondas = pygame.Surface((width*0.035,height*0.05))
            surfaceIndicadorRondas.fill((255,255,255))
            surfaceIndicadorRondas.set_alpha()
            surfaceIndicadorRondas.set_colorkey((255,255,255))
            drawFunctions.blitIndicador(surfaceIndicadorJugadores,params.playersNumber,1.3)
            drawFunctions.blitIndicador(surfaceIndicadorRondas,params.roundNumber,1)
            params.screen.blit(background, (0, 0))
            params.screen.blit(surfaceIndicadorJugadores,(width*0.487,height*0.4))
            params.screen.blit(surfaceIndicadorRondas,(width*0.48,height*0.84))
            pygame.display.flip()
            clock.tick(60)
            
        elif pantalla == 12:
            exitCmd = 0
            window = params.screen
            partidosActuales = 0
            listaJugadores = []
            if params.modo == 0:
                ia = False
            elif params.modo == 1:
                ia = True
            variableReseteo = loadPlayers(listaJugadores,window,ia)
            while partidosActuales < params.roundNumber:
                resetTanks(listaJugadores,variableReseteo,window)
                anhadirDiezmo(listaJugadores)
                runShop.openShop(listaJugadores,ia)
                gameScreens.pantallaEmpiezaJuego(window, variableReseteo)
                game = runGame.gameLogic(window,listaJugadores,params.mapa)
                exitCmd = game.run(clock)
                if exitCmd == -1:
                    return -1
                if exitCmd == 4:
                    return 4
                partidosActuales += 1
            actualizarKDAFinal(listaJugadores)
            summary = scoreBoard.scoreBoardShow(listaJugadores,window, devolverColores(variableReseteo),"Pantallas/scorePartidaGlobal.png",True)
            summary.sb_run()
            return gameScreens.ganadorScreen(window,variableReseteo[definirGanador(listaJugadores)][0])
        
        else:
            params.screen.blit(background, (0, 0))
            pygame.display.flip()
            clock.tick(60)

def definirGanador(listaDeJugadores):
    listaProporcionKD = []
    for i in range(len(listaDeJugadores)):
        if listaDeJugadores[i].generalkda[1] != 0:
            listaProporcionKD.append(listaDeJugadores[i].generalkda[0]/listaDeJugadores[i].generalkda[1])
        else:
            listaProporcionKD.append(listaDeJugadores[i].generalkda[0]) # o cualquier otro valor que quieras asignar cuando las muertes son 0
    print(listaProporcionKD)
    maxKD = max(listaProporcionKD)
    print(maxKD)
    listaDeJugadoresEmpatados = []
    for i in range(len(listaDeJugadores)):
        if listaProporcionKD[i] == maxKD:
            listaDeJugadoresEmpatados.append(i)
    
    if len(listaDeJugadoresEmpatados) == 1:
        print("El ganador es el jugador", listaDeJugadoresEmpatados[0])
        return listaDeJugadoresEmpatados[0]
    else:
        maxMoney = 0
        jugadorGanador = 0
        for i in range(len(listaDeJugadoresEmpatados)):
            if listaDeJugadores[listaDeJugadoresEmpatados[i]].money > maxMoney:
                maxMoney = listaDeJugadores[listaDeJugadoresEmpatados[i]].money
                jugadorGanador = listaDeJugadoresEmpatados[i]
        print("El ganador es el jugador", jugadorGanador)
        return jugadorGanador
        #print("Hay un empate entre los jugadores", listaDeJugadoresEmpatados)

def devolverColores(listaColores):
    colores = []
    for i in range(len(listaColores)):
        colores.append(listaColores[i][0])
    return colores

def actualizarKDAFinal(listaJugadores):
    for i in range(len(listaJugadores)):
        listaJugadores[i].generalkda[0] += listaJugadores[i].kda[0]
        listaJugadores[i].generalkda[1] += listaJugadores[i].kda[1]
        listaJugadores[i].kda[0] = 0
        listaJugadores[i].kda[1] = 0

def crearButtons(listaProporciones):
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
