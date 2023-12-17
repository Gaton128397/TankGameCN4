import drawFunctions, pygame, params, scoreBoard, functions, proporciones, params,scoreBoard,math, sys
from button import Button
def pantallaEmpiezaJuego(screen, variableReseteo):
    drawFunctions.backgroundDraw(screen,'Pantallas/juegoPrev.png')
    WIDTH = params.size*16
    HEIGHT = params.size*9
    miniTankSurface = pygame.Surface((int(WIDTH * 0.7), int(HEIGHT * 0.15)))
    alphaColor = (255,0,255)
    miniTankSurface.set_alpha()
    miniTankSurface.set_colorkey(alphaColor)
    miniTankSurface.fill((255,0,255))
    for i in range(params.playersNumber):
        tanque = scoreBoard.imgTank(variableReseteo[i][0],0.1)
        miniTankSurface.blit(tanque.surfaceTank,(int(miniTankSurface.get_width()*0.05*i*3.4), int(miniTankSurface.get_height() *0.2)))
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
        screen.blit(miniTankSurface,(int(WIDTH * 0.153), int(HEIGHT * 0.43)))
        pygame.display.update()