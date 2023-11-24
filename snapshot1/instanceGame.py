from random import randint
import pygame,projectile,nTank,nTerrain,time,sys,chooseMenu, params, drawFunctions,  infoBlock

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
        
        #players
        self.surfaceJugadores = pygame.Surface((params.WIDTH,params.HEIGHT))
        self.surfaceJugadores.fill((255,0,255))
        self.surfaceJugadores.set_alpha()
        self.surfaceJugadores.set_colorkey((255,0,255))
        self.listaJugadores = []
        self.setPlayers()
        self.updPlayers()
            
    def setPlayers(self):
        splitPos = params.WIDTH//params.playersNumber
        contador = 0
        for i in range(params.playersNumber-1):
            self.listaJugadores.append(nTank.Tank((randint(contador,contador+splitPos),100),"blue",randint(1,2),self.surfaceJugadores,self.terrain.getPoints()))
            contador += splitPos
            
    def updPlayers(self):
        for i in range(len(self.listaJugadores)):
            self.listaJugadores[i].draw_tank(True)
        self.screen.blit(self.surfaceJugadores,(0,0))
        
    def unUpdate(self):
        self.screen.blit(self.backGround,(0,0))
        self.screen.blit(self.surfaceTerrain,(0,0))
        
    def pauseScreen(self):
        print("pause state")
    
    def loadingScreen():
        print("loading")
    
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
                    self.unUpdate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        playerWinner = 1
                        return playerWinner
                    
            #clock.tick(60)
            
            pygame.display.update()
        
        
def tstgm():
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    playerWon = None
    run = True
    while run:
        for event in pygame.event.get():
            game = gameLogic(window)
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
tstgm()