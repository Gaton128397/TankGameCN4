import pygame, drawFunctions, params

def playerSpawn(window,listaJugadores,terrain,surface):
    clock = pygame.time.Clock()
    falling = True
    fallingTanks = []
    copy = []
    for i in range(len(listaJugadores)):
        if listaJugadores[i].getFallPoint() not in terrain.getDiccionary():
            fallingTanks.append(i)
            copy.append(listaJugadores[i].surfaceTank.copy())
            drawFunctions.cargarImagen(listaJugadores[i].surfaceTank,params.parachute,0.2,0.5,(0.32,0.03))
    g = params.gravityConstant//3
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
            window.blit(surfaceCopy,(0,0))
            clock.tick(60)
            pygame.display.flip()
            
def fallTanks(window,listaJugadores, terrainPoints, surface):
    clock = pygame.time.Clock()
    falling = True
    fallingTanks = []
    copy = []
    for i in range(len(listaJugadores)):
        if listaJugadores[i].getFallPoint() not in terrainPoints:
            fallingTanks.append(i)
    g = params.gravityConstant
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
                if listaJugadores[i].getFallPoint() in terrainPoints:
                    listaJugadores[i].ypos = int(listaJugadores[i].ypos)
                    fallingTanks.remove(i)
                    listaJugadores[i].hitBox = {}
                    listaJugadores[i].getHitBox()
            window.blit(surfaceCopy,(0,0))
            clock.tick(60)
            pygame.display.flip()