from random import randint
import pygame,projectile,nTank,nTerrain,time,sys,chooseMenu, params, drawFunctions,  infoBlock, player, random

class gameLogic:
    
    def __init__(self, windowGame,listaJugadores):
        self.screen = windowGame
        
        #background
        self.backGround = pygame.Surface((params.WIDTH,params.HEIGHT))
        drawFunctions.backgroundDraw(self.backGround)
        self.screen.blit(self.backGround,(0,0))
        
        #Terreno
        self.terrain = nTerrain.TerrenoVariado()
        
        #print(self.terrain.getPoints())
        self.screen.blit(self.terrain.surfTerrain,(0,0))
        
        #players
        self.surfaceJugadores = pygame.Surface((params.WIDTH,params.HEIGHT))
        self.surfaceJugadores.fill((255,0,255))
        self.surfaceJugadores.set_alpha()
        self.surfaceJugadores.set_colorkey((255,0,255))
        self.listaJugadores = []
        #self.updPlayers()
            
            
    def updPlayers(self):
        for i in range(len(self.listaJugadores)):
            self.listaJugadores[i].draw_tank(True)
        self.screen.blit(self.surfaceJugadores,(0,0))
        
    def unUpdate(self):#unnamed update
        self.screen.blit(self.backGround,(0,0))
        self.screen.blit(self.terrain.surfTerrain,(0,0))
        #self.updPlayers()
    
    def tankPos(self):
        return 0
        
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
                    return None
                    running = False
                if pygame.mouse.get_pressed()[2]:
                    self.terrain.updateImpact(pygame.mouse.get_pos(),100)
                    self.unUpdate()
                elif pygame.mouse.get_pressed()[0]:
                    if pygame.mouse.get_pos() in self.terrain.getDiccionary():
                    #pygame.draw.circle(self.surfaceTerrain, (255, 0, 255), pygame.mouse.get_pos(), 100)
                        print("hit")
                    else:
                        print("not hit")
                    #self.unUpdate()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        playerWinner = 1
                        running = False
                    
            #clock.tick(60)
            
            pygame.display.update()
        
        
def tstgm():#Logica de mainScreen()
    pygame.init()
    print("hola")
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    playerWon = None
    run = True
    numeroPartidos = 3
    while run:
        try:
            for event in pygame.event.get():
                partidosActuales = 0
                listaJugadores = []
                for i in range(params.playersNumber):
                    listaJugadores.append(player.Player())
                colores = ["red", "green", "blue", "yellow", "orange", (128, 0, 128)]
                for i in range(len(listaJugadores)):
                    choise = random.randint(0,len(colores)-1)
                    listaJugadores[i].asignTank(nTank.Tank(colores[choise],window))
                    colores.pop(choise)
                while partidosActuales < numeroPartidos:
                    game = gameLogic(window,listaJugadores)
                    game.run(clock)
                    partidosActuales += 1
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
            return True
tstgm()