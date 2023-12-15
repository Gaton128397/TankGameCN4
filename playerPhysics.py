import pygame, drawFunctions, params

def playerSpawn(window,listaJugadores,terrain,surface,gravity):
    WIDTH = params.size*16
    HEIGHT = params.size*9
    clock = pygame.time.Clock()
    falling = True
    fallingTanks = []
    copy = []
    for i in range(len(listaJugadores)):
        if listaJugadores[i].getFallPoint() not in terrain.getDiccionary():
            fallingTanks.append(i)
            copy.append(listaJugadores[i].surfaceTank.copy())
            drawFunctions.cargarImagen(listaJugadores[i].surfaceTank,"imgs/items/parachute.png",0.2,0.5,(0.32,0.03))
    g = gravity//3
    if not fallingTanks:
        falling = False
    while falling:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                falling = False
                pygame.quit()
        if not fallingTanks:
            falling = False
        else:
            for i in fallingTanks:
                listaJugadores[i].ypos += g
                surfaceCopy = surface.copy()
                surfaceCopy.blit(surface,(0,0))
                for j in listaJugadores:
                    surfaceCopy.blit(j.surfaceTank,j.getPos())
                if listaJugadores[i].getFallPoint() in terrain.getDiccionary():
                    listaJugadores[i].surfaceTank = copy[i]
                    listaJugadores[i].ypos = int(listaJugadores[i].ypos)
                    fallingTanks.remove(i)
                    listaJugadores[i].hitBox = {}
                    listaJugadores[i].getHitBox()
                    listaJugadores[i].recalcularCordCanon()
            window.blit(surfaceCopy,(0,0))
            clock.tick(60)
            pygame.display.flip()
            
def fallTanks(window,listaJugadores, terrainPoints,listaPlayers,listaJugadoresDerrotados, surface, gravity):
    clock = pygame.time.Clock()
    WIDTH = params.size*16
    falling = True
    fallingTanks = []
    copy = []
    falldmg = WIDTH*0.005
    for i in range(len(listaJugadores)):
        if listaJugadores[i].getFallPoint() not in terrainPoints:
            fallingTanks.append(i)
    g = gravity
    if not fallingTanks:
        falling = False
    while falling:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                falling = False
                pygame.quit()
        if not fallingTanks:
            falling = False
        else:
            for i in fallingTanks:
                listaJugadores[i].ypos += g
                listaJugadores[i].fallDmg += g
                surfaceCopy = surface.copy()
                surfaceCopy.blit(surface,(0,0))
                for j in listaJugadores:
                    surfaceCopy.blit(j.surfaceTank,j.getPos())
                if listaJugadores[i].getFallPoint() in terrainPoints:
                    listaJugadores[i].ypos = int(listaJugadores[i].ypos)
                    listaJugadores[i].actualizarVida(listaJugadores[i].fallDmg//falldmg)
                    if listaJugadores[i].getVida() <= 0:
                        if listaJugadores[i] not in listaJugadoresDerrotados:
                            listaJugadoresDerrotados.append(listaJugadores[i])
                            listaPlayers[listaJugadores[i].playerID].kda[1] += 1
                    listaJugadores[i].fallDmg = 0
                    fallingTanks.remove(i)
                    listaJugadores[i].hitBox = {}
                    listaJugadores[i].getHitBox()
            window.blit(surfaceCopy,(0,0))
            clock.tick(60)
            pygame.display.flip()