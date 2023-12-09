from random import randint
import pygame,nTank,nTerrain,sys, params, drawFunctions, player, random, playerPhysics, ninfoBlock, functions

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
        potencia = 0
        jugador = 'a'
        balaID = 3 #3,4,5 son las IDs
        while running:
            if self.checkearTurno(listaTurnos,turnos):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return None
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE: #aqui debe guardar la potencia
                            print("cargando potencia. . . ")
                            playerPhysics.fallTanks(self.screen,self.listaJugadores,self.terrain.getDiccionary(),drawFunctions.returnSurface([self.backGround,self.terrain.surfTerrain]))
                        
                        if event.key == pygame.K_RETURN: #recien aqui recibe la potencia para disparar
                            #debe revisar que haya una bala seleccionada o partir de la mas chica
                            if potencia >0:
                                if jugador.inventario[balaID] > 0:
                                    print('disparo') #metodo shoot
                                    jugador.inventario[balaID]-=1 #bala
                                else:
                                    print('no quedan')
                                #cuando dispara se saca el jugador de la lista de turnos
                                #siguiente jugador dispara
                                
                        
                        if event.key == pygame.K_1: #bala 1
                            balaID = 3#pequena
                        if event.key == pygame.K_2:
                            balaID = 4#mediana
                        if event.key == pygame.K_3:
                            balaID = 5#grande
                        if event.key == pygame.K_ESCAPE:
                            print('pausa') #yo (mariano) lo arreglo dsps
            else:
                running = False
            clock.tick(60)
            self.unUpdate()
            pygame.display.update()
        



def testgame(window):#Logica de mainScreen()
    pygame.init()
    clock = pygame.time.Clock()
    window = window#pygame.display.set_mode((params.WIDTH, params.HEIGHT))
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
# tstgm()