import pygame, instanceGame, params, nTerrain, drawFunctions, playerPhysics, nTank, ninfoBlock
clock = pygame.time.Clock()
window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
playerWon = None
run = True
while run:
    try:
        for event in pygame.event.get():
            game = instanceGame.gameLogic(window, )
            playerWon = game.run(clock)
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            elif playerWon == -1:
                pygame.quit()
                run = False
            if playerWon == 1:
                print("l")
                
        print("not reach")
        clock.tick(60)
        pygame.display.update()
    except (KeyboardInterrupt, SystemExit): #manejar los errores
        print("hola")