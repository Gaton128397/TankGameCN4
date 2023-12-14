from random import randint
import pygame,nTank,nTerrain,sys, params, drawFunctions, player, random, playerPhysics, ninfoBlock, functions, nProyectil, scoreBoard, npowerBar

class gameLogic:
    
    def __init__(self, windowGame,playerList, mapa):
        self.screen = windowGame
        
        #variables de entorno
        self.mapa = mapa
        self.gravity = 9.8
        self.wind = self.mapa[2]
        
        #background
        self.backGround = pygame.Surface((params.WIDTH,params.HEIGHT))
        drawFunctions.backgroundDraw(self.backGround,self.mapa[0])
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
        self.cantidadbullets = self.cantidadBalas()
        
        #otros
        self.coloresJuagadores = []
        self.getColoresPlayers()
        self.powerBar = npowerBar.BarraDeCarga(0.2)
        
    def setPlayers(self):
        splitPos = params.WIDTH//(params.playersNumber*2)
        contador = 0
        for i in range(params.playersNumber):
            self.listaPlayers[i].tanque.setPos((random.randint(contador,contador+splitPos),-20))
            self.listaJugadores.append(self.listaPlayers[i].tanque)
            contador += splitPos*2
    
    def updPlayers(self):
        for i in range(len(self.listaJugadores)):
            self.screen.blit(self.listaJugadores[i].surfaceTank,(self.listaJugadores[i].getPos()))
        
    def actualizarPantallasJuego(self):#unnamed update
        self.screen.blit(self.backGround,(0,0))
        self.screen.blit(self.terrain.surfTerrain,(0,0))
        self.screen.blit(self.info.bloque, (params.WIDTH*0.68, 0))
        self.updPlayers()

    def actualizarInfo(self,player,balaID):
        self.info.actualizarAngulo(player.angulo)
        #self.info.actualizarDistancia(player.getPos()[0])
        self.info.actualizarEscudo(self.listaPlayers[player.playerID].inventory[0])
        #self.info.actualizarDmg(player.damage)
        #self.info.actualizarBotellas(player.inventory[0])
        #self.info.actualizarTipoBala(player.inventory[balaID])

        if balaID == 5: #bala 1
            self.info.actualizarTipoBala("60")
            self.info.actualizarCantidadBalas(self.listaPlayers[player.playerID].inventory[balaID])
            
        if balaID == 4:
            balaID = 4#mediana
            self.info.actualizarTipoBala("80")
            self.info.actualizarCantidadBalas(self.listaPlayers[player.playerID].inventory[balaID])
            
        if balaID == 3:
            balaID = 3#grande
            self.info.actualizarTipoBala("105")
            self.info.actualizarCantidadBalas(self.listaPlayers[player.playerID].inventory[balaID])
            
    def getColoresPlayers(self):
        for i in range(len(self.listaJugadores)):
            self.coloresJuagadores.append(self.listaJugadores[i].color)
        
    def getTankIndex(self, tank):
        for i in range(len(self.listaJugadores)):
            if tank == self.listaJugadores[i]:
                return i
        return False
    
    def checkearTurno(self,listaDeTurnos,turnos,jugadoresDerrotados,balaID): #0 para turno actual, 1 para turno anterior
        if len(self.listaJugadores) == 1:
            #mostrar pantalla de que el jugador gano
            summary = scoreBoard.scoreBoard(self.listaPlayers,self.screen, self.coloresJuagadores,"imgs/pantallas/scorePartida.png",False)
            summary.sb_run()
            summary = None
            for i in range(len(self.listaPlayers)):
                self.listaPlayers[i].generalkda[0] += self.listaPlayers[i].kda[0]
                self.listaPlayers[i].generalkda[1] += self.listaPlayers[i].kda[1]
                self.listaPlayers[i].kda[0] = 0
                self.listaPlayers[i].kda[1] = 0
            return False
        elif self.cantidadbullets <= 0:
            summary = scoreBoard.scoreBoard(self.listaPlayers,self.screen, self.coloresJuagadores,"imgs/pantallas/scorePartida.png",False)
            summary.sb_run()
            summary = None
            for i in range(len(self.listaPlayers)):
                self.listaPlayers[i].generalkda[0] += self.listaPlayers[i].kda[0]
                self.listaPlayers[i].generalkda[1] += self.listaPlayers[i].kda[1]
                self.listaPlayers[i].kda[0] = 0
                self.listaPlayers[i].kda[1] = 0
            
            #mostrar pantalla de que se los jugadores se quedaron sin balas
            return False
        elif jugadoresDerrotados:
            for i in range(len(jugadoresDerrotados)):
                print("jugador derrotado: " + str(self.getTankIndex(jugadoresDerrotados[i])))
                del self.listaJugadores[self.getTankIndex(jugadoresDerrotados[i])]
            self.definirTurnos(listaDeTurnos)
            self.cantidadbullets = self.cantidadBalas()
            self.cantidadbullets = self.cantidadBalas()
            turnos[0] = random.choice(listaDeTurnos)
            turnos[1] = turnos[0]
            self.actualizarInfo(self.listaJugadores[turnos[0]],balaID)
            self.actualizarInfo(self.listaJugadores[turnos[0]],balaID)
            listaDeTurnos.remove(turnos[0])
            jugadoresDerrotados.clear()
            print("candidad jugador: " + str(len(self.listaJugadores)))
            return True
        elif not listaDeTurnos:
            self.definirTurnos(listaDeTurnos)
            turnos[0] = random.choice(listaDeTurnos)
            turnos[1] = turnos[0]
            self.actualizarInfo(self.listaJugadores[turnos[0]],balaID)
            self.actualizarInfo(self.listaJugadores[turnos[0]],balaID)
            listaDeTurnos.remove(turnos[0])
            print("turno actual: ",turnos[0])
            print("turno anterior: ",turnos[1])
            return True
        elif turnos[0] != turnos[1]:
            turnos[0] = random.choice(listaDeTurnos)
            turnos[1] = turnos[0]
            self.actualizarInfo(self.listaJugadores[turnos[0]],balaID)
            self.actualizarInfo(self.listaJugadores[turnos[0]],balaID)
            listaDeTurnos.remove(turnos[0])
            print("turno actual: ",turnos[0])
            print("turno anterior: ",turnos[1])
            print("Lista de turnos"+str(listaDeTurnos))
            return True
        else:
            return True


    def definirTurnos(self,listaTurnos):
        listaTurnos.clear()
        for i in range(len(self.listaJugadores)):
            listaTurnos.append(i)
        print("lista de turnos: " + str(listaTurnos))
        print("lista de turnos: " + str(listaTurnos))
        
    def tankPos(self):
        return 0
        
    def pauseScreen(self):
        print("pause state")
    
    def loadingScreen():
        print("loading")
    
    def cantidadBalas(self):
        cantidadBalas = 0
        for i in range(len(self.listaJugadores)):
            cantidadBalas += self.listaPlayers[self.listaJugadores[i].playerID].inventory[3]
            cantidadBalas += self.listaPlayers[self.listaJugadores[i].playerID].inventory[4]
            cantidadBalas += self.listaPlayers[self.listaJugadores[i].playerID].inventory[5]
        return cantidadBalas
    
    def comprobarBalasJugador(self,jugador):
        if self.listaPlayers[jugador.playerID].inventory[3] <= 0 and self.listaPlayers[jugador.playerID].inventory[4] <= 0 and self.listaPlayers[jugador.playerID].inventory[5] <= 0:
            self.listaPlayers[jugador.playerID].tanque.ammo = False
        
    
    def cantidadBalas(self):
        cantidadBalas = 0
        for i in range(len(self.listaJugadores)):
            cantidadBalas += self.listaPlayers[self.listaJugadores[i].playerID].inventory[3]
            cantidadBalas += self.listaPlayers[self.listaJugadores[i].playerID].inventory[4]
            cantidadBalas += self.listaPlayers[self.listaJugadores[i].playerID].inventory[5]
        return cantidadBalas
    
    def comprobarBalasJugador(self,jugador):
        if self.listaPlayers[jugador.playerID].inventory[3] <= 0 and self.listaPlayers[jugador.playerID].inventory[4] <= 0 and self.listaPlayers[jugador.playerID].inventory[5] <= 0:
            self.listaPlayers[jugador.playerID].tanque.ammo = False
        
    def run(self,clock):
        running = True
        print(self.listaJugadores[0].getPos())
        playerPhysics.playerSpawn(self.screen,self.listaJugadores,self.terrain,drawFunctions.returnSurface([self.backGround,self.terrain.surfTerrain]),self.gravity)
        surfaces = [self.backGround,self.terrain.surfTerrain,self.info.bloque]
        listaTurnos = []
        jugadoresDerrotados = []
        self.definirTurnos(listaTurnos)
        turnos = [0,0]
        listaTurnos.remove(0)
        potencia = 100
        cargarBarra = False
        jugador = 'a'
        balaID = 3 #3,4,5 son las IDs
        self.info.actualizarCantidadBalas(self.listaPlayers[0].inventory[balaID])
        self.info.actualizarTipoBala("105")
        self.info.actualizarAngulo(self.listaJugadores[0].angulo)
        anguloIA = -1
        print("cantidad jugadores: " + str(len(self.listaJugadores)))
        while running:
            if self.checkearTurno(listaTurnos,turnos,jugadoresDerrotados,balaID):
                jugador = self.listaJugadores[turnos[0]]
                if self.listaPlayers[jugador.playerID].ia:
                    if jugador.ammo:
                        if anguloIA == -1:
                            anguloIA = randint(0,180)
                            print("angulo IA: " + str(anguloIA))
                            print("angulo jugador: " + str(jugador.angulo))
                        if jugador.angulo > anguloIA:
                            jugador.actualizarAnguloIA(-1)
                            self.info.actualizarAngulo(jugador.angulo)
                        elif jugador.angulo < anguloIA:
                            jugador.actualizarAnguloIA(1)
                            self.info.actualizarAngulo(jugador.angulo)
                        elif jugador.angulo == anguloIA:
                            if self.listaPlayers[jugador.playerID].inventory[balaID] > 0:
                                wind = randint(-10,10)
                                potenciaIA = random.randint(50,150)
                                bullet = nProyectil.Projectile(self.screen,(int(jugador.getPos()[0]+jugador.xCanon2-(params.WIDTH*0.028)),int(jugador.getPos()[1]+jugador.yCanon2-(params.HEIGHT*0.05))),balaID,potenciaIA,jugador.angulo,self.listaJugadores,self.gravity,wind)
                                self.terrain.updateImpact(bullet.shoot(surfaces,self.terrain.getDiccionary(), self.info),bullet,self.listaJugadores,self.listaPlayers,jugadoresDerrotados,turnos[0])
                                self.listaPlayers[jugador.playerID].inventory[balaID] -=1
                                self.cantidadbullets -= 1
                                self.comprobarBalasJugador(self.listaJugadores[turnos[0]])
                                print("balas totales: " + str(self.cantidadbullets))
                                self.info.actualizarCantidadBalas(self.listaPlayers[jugador.playerID].inventory[balaID])
                                playerPhysics.fallTanks(self.screen,self.listaJugadores,self.terrain.getDiccionary(),self.listaPlayers,jugadoresDerrotados,drawFunctions.returnSurface([self.backGround,self.terrain.surfTerrain]),self.gravity)
                                anguloIA = -1
                                turnos[0] = -1
                            else:
                                balaID = randint(3,5)
                    else:
                        turnos[0] = -1
                else:
                    if jugador.ammo:
                        pressed = pygame.key.get_pressed()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                                return None
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if pygame.mouse.get_pressed()[0]:
                                    print(pygame.mouse.get_pos())
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_SPACE: #aqui debe guardar la potencia
                                    print("cargando potencia. . . ")
                                if event.type==pygame.KEYDOWN:
                                    if event.key==pygame.K_f:
                                        if params.size == 120:
                                            params.size=80
                                        else:
                                            params.size=120
                                if event.key == pygame.K_RETURN: #recien aqui recibe la potencia para disparar
                                    #debe revisar que haya una bala seleccionada o partir de la mas chica
                                    if potencia >0:
                                        if self.listaPlayers[jugador.playerID].inventory[balaID] > 0:
                                            print('disparo') #metodo shoot
                                            wind = randint(-10,10)
                                            bullet = nProyectil.Projectile(self.screen,(int(jugador.getPos()[0]+jugador.xCanon2-(params.WIDTH*0.028)),int(jugador.getPos()[1]+jugador.yCanon2-(params.HEIGHT*0.05))),balaID,potencia,jugador.angulo,self.listaJugadores,self.gravity,wind)
                                            self.terrain.updateImpact(bullet.shoot(surfaces,self.terrain.getDiccionary(),self.info),bullet,self.listaJugadores,self.listaPlayers,jugadoresDerrotados,turnos[0])
                                            self.listaPlayers[jugador.playerID].inventory[balaID] -=1 #bala
                                            self.cantidadbullets -= 1
                                            self.comprobarBalasJugador(self.listaJugadores[turnos[0]])
                                            print("balas totales: " + str(self.cantidadbullets))
                                            self.info.actualizarCantidadBalas(self.listaPlayers[jugador.playerID].inventory[balaID])
                                            playerPhysics.fallTanks(self.screen,self.listaJugadores,self.terrain.getDiccionary(),self.listaPlayers,jugadoresDerrotados,drawFunctions.returnSurface([self.backGround,self.terrain.surfTerrain]),self.gravity)
                                            turnos[0] = -1
                                        else:
                                            print('no quedan')
                                        #cuando dispara se saca el jugador de la lista de turnos
                                
                                if event.key == pygame.K_1: #bala 1
                                    balaID = 5#pequena
                                    self.info.actualizarTipoBala("60")
                                    self.info.actualizarCantidadBalas(self.listaPlayers[jugador.playerID].inventory[balaID])
                                    
                                if event.key == pygame.K_2:
                                    balaID = 4#mediana
                                    self.info.actualizarTipoBala("80")
                                    self.info.actualizarCantidadBalas(self.listaPlayers[jugador.playerID].inventory[balaID])
                                    
                                if event.key == pygame.K_3:
                                    balaID = 3#grande
                                    self.info.actualizarTipoBala("105")
                                    self.info.actualizarCantidadBalas(self.listaPlayers[jugador.playerID].inventory[balaID])
                                
                                if event.key == pygame.K_0:
                                    turnos[0] = -1
                                if event.key == pygame.K_ESCAPE:
                                    print('pausa') #yo (mariano) lo arreglo dsps
                        if pressed[pygame.K_LEFT]:
                            jugador.actualizarAngulo(pygame.K_LEFT)
                            self.info.actualizarAngulo(jugador.angulo)
                        elif pressed[pygame.K_RIGHT]:
                            jugador.actualizarAngulo(pygame.K_RIGHT)
                            self.info.actualizarAngulo(jugador.angulo)
                        if pressed[pygame.K_SPACE]:
                            self.powerBar.cargar(1)
                            potencia = int(self.powerBar.carga)
                        else:
                            self.powerBar.resetear()
                        #print("potencia: " + str(potencia))

                    else:
                        turnos[0] = -1
            else:
                running = False
                break
            clock.tick(60)
            self.actualizarPantallasJuego()
            self.powerBar.dibujar(self.screen)
            pygame.display.update()
        



def testgame():#Logica de mainScreen()
    pygame.init()
    clock = pygame.time.Clock()
    window = pygame.display.set_mode((params.WIDTH, params.HEIGHT))
    playerWon = None
    run = True
    numeroPartidos = 2
    while run:
        partidosActuales = 0
        listaJugadores = []
        ia = True
        resetTanks = functions.loadPlayers(listaJugadores,window,ia)
        while partidosActuales < numeroPartidos:
            mapa = ["imgs/maps/ciudad.png",9.8,2]
            functions.resetTanks(listaJugadores,resetTanks,window)
            functions.resetIventario(listaJugadores)
            game = gameLogic(window,listaJugadores,mapa)
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
testgame()