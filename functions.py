import math, params, player, nTank, random

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

def resetIventario(listaJugadores):
    for i in range(len(listaJugadores)):
        listaJugadores[i].inventory[0] = 0
        listaJugadores[i].inventory[3] = 0
        listaJugadores[i].inventory[4] = 0
        listaJugadores[i].inventory[5] = 1
