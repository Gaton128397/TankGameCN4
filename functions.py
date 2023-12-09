import math, params, player, nTank, random

radius = 160

def toRadian(theta):
    return theta * math.pi / 180

def toDegrees(theta):
    return theta * 180 / math.pi

def getGradient(p1, p2):
    if p1[0] == p2[0]:
        m = toRadian(90)
    else:
        m = (p2[1] - p1[1]) / (p2[0] - p1[0])
    return m

def getAngleFromGradient(gradient):
    return math.atan(gradient)

def getAngle(pos, origin):
    m = getGradient(pos, origin)
    thetaRad = getAngleFromGradient(m)
    theta = round(toDegrees(thetaRad), 2)
    return theta

def getPosOnCircumeference(theta, origin):
    theta = toRadian(theta)
    x = origin[0] + radius * math.cos(theta)
    y = origin[1] + radius * math.sin(theta)
    return (x, y)

def divideScreenIn9(width,height):    
    x1 = width*1/3
    y1 = height*1/3
    x2 = width*2/3
    y2 = height*2/3
    x3 = width
    y3 = height
    listaTercios = [(x1,y1),(x2,y1),(x3,y1),(x1,y2),(x2,y2),(x3,y2),(x1,y3),(x2,y3),(x3,y3)]
    return listaTercios

def collide(firstObjectPos,SecondObjectPos):
    firstObjectPosX = firstObjectPos[0]
    firstObjectPosY = firstObjectPos[1]
    secondObjectPosX = SecondObjectPos[0]
    secondObjectPosY = SecondObjectPos[1]
    collided = math.sqrt((secondObjectPosX-firstObjectPosX)**2 + (secondObjectPosY-firstObjectPosY)**2)
    if collided <= 0:
        return 1
    else:
        return 0
    
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
    
def loadPlayers(listaJugadores,window):
    resetTanks = []
    for i in range(params.playersNumber):
        listaJugadores.append(player.Player())
    colores = ["red", "green", "blue", "yellow", "orange", (128, 0, 128)]
    for i in range(len(listaJugadores)):
        choise = random.randint(0,len(colores)-1)
        listaJugadores[i].asignTank(nTank.Tank(colores[choise],window,i))
        resetTanks.append(nTank.Tank(colores[choise],window,i))
        colores.pop(choise)
    return resetTanks

def resetTanks(listaJugadores,tankList):
    for i in range(len(listaJugadores)):
        listaJugadores[i].asignTank(tankList[i])