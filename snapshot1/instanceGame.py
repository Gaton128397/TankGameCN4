from random import randint
import pygame,projectile,tank,nTerrain,time,sys,chooseMenu, params, drawFunctions,  infoBlock

class gameLogic:
    
    def __init__(self, windowGame):
        self.screen = windowGame
        #background
        self.backGround = pygame.Surface((params.WIDTH,params.HEIGHT))
        drawFunctions.backgroundDraw(self.backGround)
        self.screen.blit(self.backGround,(0,0))
        #Terreno
        self.terrain = nTerrain.TerrenoVariado(params.WIDTH, params.HEIGHT)
        self.surfaceTerrain = self.terrain.drawTerrain()
        self.screen.blit(self.surfaceTerrain,(0,0))
        
        
        
    def run(self,clock):
        playerWinner = -1
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return playerWinner
                    running = False
                if pygame.mouse.get_pressed()[0]:
                    pygame.draw.circle(self.surfaceTerrain, (255, 0, 255), pygame.mouse.get_pos(), 100)
                    print("hit")
                    self.screen.blit(self.backGround,(0,0))
                    self.screen.blit(self.surfaceTerrain,(0,0))
            #clock.tick(60)
            
            pygame.display.update()
        
        
def tstgm():
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    game = gameLogic(window)
    playerWon = None
    run = True
    while run:
        for event in pygame.event.get():
            playerWon = game.run(clock)
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            elif playerWon == -1:
                pygame.quit()
                run = False
        print("not reach")
        clock.tick(60)
        pygame.display.update()
tstgm()