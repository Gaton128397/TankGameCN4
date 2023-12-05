import pygame, random, params, nTerrain, drawFunctions, playerPhysics, nTank, ninfoBlock, random
pygame.init()
terrain = nTerrain.TerrenoVariado()
window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
bg = pygame.Surface((params.WIDTH, params.HEIGHT))
colores = [(255,0,0),(0,255,0),(0,0,255),(255,255,0)]
listaJugadores = []

clock = pygame.time.Clock()
#clock.tick(60)
drawFunctions.backgroundDraw(bg)
info = ninfoBlock.infoBlock(0.3)
info.actualizarAngulo('10')
info.actualizarDistancia("2000")
info.actualizarEscudo(False)
info.actualizarDmg(False)
info.actualizarBotellas("0")
info.actualizarTipoBala("105")
info.actualizarCantidadBalas(0)
surperficeJuego = [bg, terrain.surfTerrain,info.bloque]
ejecutando = True
turno = 0

def setPlayers():
        splitPos = params.WIDTH//(params.playersNumber*2)
        contador = 0
        for i in range(params.playersNumber):
            listaJugadores.append(nTank.Tank((random.randint(contador,contador+splitPos)),random.choice(colores),window))
            print(splitPos)
            contador += splitPos*2
            print(contador)

setPlayers()

while ejecutando:
    info.actualizarAngulo(listaJugadores[turno].angulo)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        playerPhysics.playerSpawn(window,listaJugadores,terrain,drawFunctions.returnSurface(surperficeJuego))
        if pygame.mouse.get_pressed()[2]:#logica de disparo
            terrain.testupdateImpact(pygame.mouse.get_pos(),int(params.WIDTH*0.07),listaJugadores)
            playerPhysics.fallTanks(window,listaJugadores,terrain.getDiccionary(),drawFunctions.returnSurface(surperficeJuego))
        elif pygame.mouse.get_pressed()[0]:
            print("---------------------------punto{}---------------------------------".format(pygame.mouse.get_pos()))
            for i in listaJugadores:  
                
                if pygame.mouse.get_pos() in i.hitBox:
                    print("tanque " + str(listaJugadores.index(i)))
                else:
                    print("no xd")
            print("------------------------------------------------------------")
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                #del listaJugadores[turno]
                print("disparando")
                turno = random.randint(0, len(listaJugadores)-1)
    for key in listaJugadores[turno].listaEventos[0]:
        if keys[key]:
            listaJugadores[turno].actualizarAngulo(event)
            #info.actualizarAngulo(listaJugadores[turno].angulo)
            #print("moviendo cañon")
    #contador += 0.1
    window.blit(surperficeJuego[0],(0,0))
    window.blit(surperficeJuego[1],(0,0))
    for i in range(len(listaJugadores)):
        window.blit(listaJugadores[i].surfaceTank,listaJugadores[i].getPos())
    window.blit(info.bloque, (870, 0))
    clock.tick(60)
    pygame.display.flip()