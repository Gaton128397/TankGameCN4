from random import randint
import pygame,nTank,nTerrain,sys, params, drawFunctions, player, random, playerPhysics, ninfoBlock, functions
from ctypes import byref, c_int, pointer

class gameLogic:
    
    def __init__(self, windowGame,playerList):
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
        self.listaPlayers = playerList
        self.listaJugadores = []
        self.setPlayers()
        
        #infoBlock
        self.info = ninfoBlock.infoBlock(0.3)
        
    def setPlayers(self):
        splitPos = params.WIDTH//(params.playersNumber*2)
        contador = 0
        for i in range(params.playersNumber):
            self.listaPlayers[i].tanque.setPos((random.randint(contador,contador+splitPos),-10))
            self.listaJugadores.append(self.listaPlayers[i].tanque)
            print(splitPos)
            contador += splitPos*2
            print(contador)
    
    def updPlayers(self):
        for i in range(len(self.listaJugadores)):
            self.screen.blit(self.listaJugadores[i].surfaceTank,(self.listaJugadores[i].getPos()))
        
    def unUpdate(self):#unnamed update
        self.screen.blit(self.backGround,(0,0))
        self.screen.blit(self.terrain.surfTerrain,(0,0))
        self.updPlayers()
        
    def checkearTurno(self,listaDeTurnos,turnos): #0 para turno actual, 1 para turno anterior
        if len(self.listaJugadores) == 1:
            return False
        elif not listaDeTurnos:
            self.definirTurnos(listaDeTurnos)
            turnos[0] = random.choice(listaDeTurnos)
            turnos[1] = turnos[0]
            print("turno actual: ",turnos[0])
            print("turno anterior: ",turnos[1])
            return True
        elif turnos[0] != turnos[1]:
            turnos[0] = random.choice(listaDeTurnos)
            turnos[1] = turnos[0]
            listaDeTurnos.remove(turnos[0])
            print("turno actual: ",turnos[0])
            print("turno anterior: ",turnos[1])
            print("Lista de turnos"+str(listaDeTurnos))
            return True
        else:
            return True
    
    def definirTurnos(self,listaTurnos):
        for i in range(len(self.listaJugadores)):
            listaTurnos.append(i)
        
    def tankPos(self):
        return 0
        
    def pauseScreen(self):
        print("pause state")
    
    def loadingScreen():
        print("loading")
    
    def run(self,clock):
        running = True
        playerPhysics.playerSpawn(self.screen,self.listaJugadores,self.terrain,drawFunctions.returnSurface([self.backGround,self.terrain.surfTerrain]))
        surfaces = [self.backGround,self.terrain.surfTerrain,self.info.bloque]
        listaTurnos = []
        turnos = [0,0]
        while running:
            if self.checkearTurno(listaTurnos,turnos):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return None
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            print("disparando")
                            playerPhysics.fallTanks(self.screen,self.listaJugadores,self.terrain.getDiccionary(),drawFunctions.returnSurface([self.backGround,self.terrain.surfTerrain]))
                        if event.key == pygame.K_1:
                            turnos[0] = -1
                        if event.key == pygame.K_2:
                            del self.listaJugadores[turnos[0]]
                            turnos[0] = -1
                        if event.key == pygame.K_3:
                            print(turnos[0])
                            #print(turnoAnterior)
                        if event.key == pygame.K_4:
                            running = False
            else:
                running = False
            clock.tick(60)
            self.unUpdate()
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
        partidosActuales = 0
        listaJugadores = []
        resetTanks = functions.loadPlayers(listaJugadores,window)
        while partidosActuales < numeroPartidos:
            functions.resetTanks(listaJugadores,resetTanks)
            game = gameLogic(window,listaJugadores)
            game.run(clock)
            partidosActuales += 1
        print("partidos terminados")
        run = False     
        try:
            for event in pygame.event.get():
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