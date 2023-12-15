import drawFunctions, pygame
def pantallaEmpiezaJuego(screen):
    drawFunctions.backgroundDraw(screen,'Pantallas/juegoPrev.png')
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    run = False
        pygame.display.update()