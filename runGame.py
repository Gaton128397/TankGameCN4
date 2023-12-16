from random import randint
import pygame,nTank,nTerrain,sys, params, drawFunctions, player, random, playerPhysics, ninfoBlock, functions, nProyectil, scoreBoard, npowerBar

class gameLogic:
    
    def __init__(self, windowGame,playerList, mapa):
        self.WIDTH = params.size*16
        self.HEIGHT = params.size*9
        self.screen = windowGame
        #WIDTH = params.size*16
        #HEIGHT = params.size*9
        #variables de entorno
        self.mapa = mapa
        self.gravity = self.mapa.getMap()[1]
        self.color = self.mapa.getMap()[2]
        
        #background
        self.backGround = pygame.Surface((self.WIDTH,self.HEIGHT))
        self.mapaImg = pygame.transform.scale(self.mapa.getMap()[0],(self.WIDTH,self.HEIGHT))

        # drawFunctions.backgroundDraw(self.backGround,self.mapaIMG)
        self.backGround.blit(self.mapa.getMap()[0],(0,0))
        print('a')
        self.screen.blit(self.backGround,(0,0))
        
        #Terreno
        self.terrain = nTerrain.TerrenoVariado(self.color)
        
        #terreno
        self.screen.blit(self.terrain.surfTerrain,(0,0))
        
        #players
        self.listaPlayers = playerList
        self.listaJugadores = []
        self.setPlayers()
        
        #infoBlock
        self.info = ninfoBlock.infoBlock(0.25)
        self.cantidadbullets = self.cantidadBalas()
        
        #estela de disparo
        self.estelaSurface = pygame.Surface((self.WIDTH,self.HEIGHT))
        self.estelaAlpha = (255,255,255)
        self.estelaSurface.fill(self.estelaAlpha)
        self.estelaSurface.set_alpha()
        self.estelaSurface.set_colorkey(self.estelaAlpha)
        
        #powerBar
        self.powerBar = npowerBar.BarraDeCarga(0.2)
        
        #surface del viento
        self.surfaceWind = pygame.Surface((self.WIDTH*0.1,self.HEIGHT*0.04))
        self.windAlpha = (255,255,255)
        self.surfaceWind.fill(self.windAlpha)
        self.surfaceWind.set_alpha()
        self.surfaceWind.set_colorkey(self.windAlpha)
        drawFunctions.cargarImagen(self.surfaceWind,"items/wind.png",0.3,1,(0,0))
        
        
        #otros
        self.coloresJuagadores = []
        self.getColoresPlayers()
        
    def actualizarViento(self,wind):
        pygame.draw.rect(self.surfaceWind, (255,255,255), (self.surfaceWind.get_width()*0.4,0,self.surfaceWind.get_width()*0.5,self.surfaceWind.get_height()))
        wind = str(wind)
        wind = wind + " m/s"
        fuente = pygame.font.Font(None, int(self.surfaceWind.get_width() *0.2))
        superficie_texto = fuente.render(wind, True, (0, 0, 0))
        self.surfaceWind.blit(superficie_texto, (int(self.surfaceWind.get_width() *0.4), int(self.surfaceWind.get_height() *0.18)))
        
    def setPlayers(self):
        splitPos = self.WIDTH//(params.playersNumber*2)
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
        self.screen.blit(self.estelaSurface,(0,0))
        self.screen.blit(self.info.bloque, (self.WIDTH*0.68, 0))
        self.screen.blit(self.surfaceWind,(self.WIDTH*0,self.HEIGHT*0.1))
        self.updPlayers()

    def actualizarInfo(self,turno,balaID):
        self.info.actualizarAngulo(self.listaJugadores[turno].angulo)
        self.info.actualizarDistancia(self.listaJugadores[turno].distancia)
        self.info.actualizarTanque(self.listaJugadores[turno].color)
        #self.info.actualizarEscudo(self.listaPlayers[player.playerID].inventory[0])
        #self.info.actualizarDmg(player.damage)
        #self.info.actualizarBotellas(player.inventory[0])
        
        if balaID == 5: #bala 1
            self.info.actualizarTipoBala("60")
            self.info.actualizarCantidadBalas(self.listaPlayers[self.listaJugadores[turno].playerID].inventory[balaID])    
        elif balaID == 4:
            balaID = 4#mediana
            self.info.actualizarTipoBala("80")
            self.info.actualizarCantidadBalas(self.listaPlayers[self.listaJugadores[turno].playerID].inventory[balaID])    
        elif balaID == 3:
            balaID = 3#grande
            self.info.actualizarTipoBala("105")
            self.info.actualizarCantidadBalas(self.listaPlayers[self.listaJugadores[turno].playerID].inventory[balaID])
            
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
            #print("jugador gano")
            #mostrar pantalla de que el jugador gano
            #summary = scoreBoard.scoreBoard(self.listaPlayers,self.screen, self.coloresJuagadores,"imgs/pantallas/scorePartida.png",False)
            #summary.sb_run()
            #summary = None
            return False
        elif self.cantidadbullets <= 0:
            #print("jugadores sin balas")
            #summary = scoreBoard.scoreBoard(self.listaPlayers,self.screen, self.coloresJuagadores,"imgs/pantallas/scorePartida.png",False)
            #summary.sb_run()
            #summary = None
            
            #mostrar pantalla de que se los jugadores se quedaron sin balas
            return False
        elif jugadoresDerrotados:
            for i in range(len(jugadoresDerrotados)):
                indice = self.getTankIndex(jugadoresDerrotados[i])
                if indice in listaDeTurnos:
                    listaDeTurnos.remove(indice)
                del self.listaJugadores[indice]
            self.definirTurnos(listaDeTurnos)
            cambioDeTurno = random.choice(listaDeTurnos)
            while cambioDeTurno == turnos[1] and len(listaDeTurnos) > 1:
                cambioDeTurno = random.choice(listaDeTurnos)
            turnos[0] = random.choice(listaDeTurnos)
            turnos[1] = turnos[0]
            self.listaJugadores[turnos[0]].turnoTanque(True)
            listaDeTurnos.remove(turnos[0])
            self.cantidadbullets = self.cantidadBalas()
            self.actualizarInfo(turnos[0],balaID)
            jugadoresDerrotados.clear()
            return True
        elif (not listaDeTurnos) and (turnos[0] != turnos[1]):
            #print("no hay turnos")
            self.definirTurnos(listaDeTurnos)
            cambioDeTurno = random.choice(listaDeTurnos)
            while cambioDeTurno == turnos[1]:
                cambioDeTurno = random.choice(listaDeTurnos)
            turnos[0] = cambioDeTurno
            turnos[1] = turnos[0]
            self.listaJugadores[turnos[0]].turnoTanque(True)
            self.actualizarInfo(turnos[0],balaID)
            listaDeTurnos.remove(turnos[0])
            return True
        elif turnos[0] != turnos[1]:
            #print("\n--------------turno antes de cambiar----------------")
            #print("turno actual: ",turnos[0])
            #print("turno anterior: ",turnos[1])
            #print("Lista de turnos"+str(listaDeTurnos))
            turnos[0] = random.choice(listaDeTurnos)
            turnos[1] = turnos[0]
            self.listaJugadores[turnos[0]].turnoTanque(True)
            self.actualizarInfo(turnos[0],balaID)
            listaDeTurnos.remove(turnos[0])
            #print("\n--------------turno cambiado----------------")
            #print("turno actual: ",turnos[0])
            #print("turno anterior: ",turnos[1])
            #print("Lista de turnos"+str(listaDeTurnos))
            return True
        else:
            return True


    def definirTurnos(self,listaTurnos):
        listaTurnos.clear()
        for i in range(len(self.listaJugadores)):
            listaTurnos.append(i)
        
    def tankPos(self):
        return 0
        
    def pauseScreen(self):
        pass
        #print("pause state")
    
    def loadingScreen():
        pass
        #print("loading")
    
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
        
    def run(self,clock):
        running = True
        #print(self.listaJugadores[0].getPos())
        playerPhysics.playerSpawn(self.screen,self.listaJugadores,self.terrain,drawFunctions.returnSurface([self.backGround,self.terrain.surfTerrain]),self.gravity)
        surfaces = [self.backGround,self.terrain.surfTerrain,self.info.bloque,self.estelaSurface,self.powerBar.poweBarSurface,self.surfaceWind]
        listaTurnos = []
        jugadoresDerrotados = []
        self.definirTurnos(listaTurnos)
        turnos = [0,0]
        listaTurnos.remove(0)
        potencia = 0
        jugador = 'a'
        balaID = 3 #3,4,5 son las IDs
        self.actualizarInfo(turnos[0],balaID)
        self.listaJugadores[turnos[0]].turnoTanque(True)
        chooseWind = True
        wind = randint(-10,10)
        self.actualizarViento(wind)
        anguloIA = -1
        while running:
            
            if self.checkearTurno(listaTurnos,turnos,jugadoresDerrotados,balaID):
                
                jugador = self.listaJugadores[turnos[0]]
                
                if not chooseWind:
                    chooseWind = True
                    wind = randint(-10,10)
                    self.actualizarViento(wind)
                    
                if self.listaPlayers[jugador.playerID].ia:
                    if jugador.ammo:
                        if anguloIA == -1:
                            anguloIA = randint(0,180)
                        if jugador.angulo > anguloIA:
                            jugador.actualizarAnguloIA(-1)
                            self.info.actualizarAngulo(jugador.angulo)
                        elif jugador.angulo < anguloIA:
                            jugador.actualizarAnguloIA(1)
                            self.info.actualizarAngulo(jugador.angulo)
                        elif jugador.angulo == anguloIA:
                            if self.listaPlayers[jugador.playerID].inventory[balaID] > 0:
                                self.estelaSurface.fill(self.estelaAlpha)
                                potenciaIA = random.randint(50,150)
                                bullet = nProyectil.Projectile(self.screen,(int(jugador.getPos()[0]+jugador.xCanon2-(self.WIDTH*0.028)),int(jugador.getPos()[1]+jugador.yCanon2-(self.HEIGHT*0.05))),balaID,potenciaIA,jugador.angulo,self.listaJugadores,self.gravity,wind)
                                self.terrain.updateImpact(bullet.shoot(surfaces,self.terrain.getDiccionary(), self.info,turnos[0]),bullet,self.listaJugadores,self.listaPlayers,jugadoresDerrotados,turnos[0])
                                self.listaPlayers[jugador.playerID].inventory[balaID] -=1
                                self.cantidadbullets -= 1
                                self.comprobarBalasJugador(self.listaJugadores[turnos[0]])
                                self.info.actualizarCantidadBalas(self.listaPlayers[jugador.playerID].inventory[balaID])
                                playerPhysics.fallTanks(self.screen,self.listaJugadores,self.terrain.getDiccionary(),self.listaPlayers,jugadoresDerrotados,drawFunctions.returnSurface([self.backGround,self.terrain.surfTerrain]),self.gravity)
                                anguloIA = -1
                                self.listaJugadores[turnos[0]].turnoTanque(False)
                                turnos[0] = -1
                                chooseWind = False
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
                                    pass
                                    #print(pygame.mouse.get_pos())
                            if event.type == pygame.KEYDOWN:
                                if event.key == pygame.K_RETURN: #r
                                    #debe revisar que haya una bala seleccionada o partir de la mas chica
                                    if potencia >0:
                                        if self.listaPlayers[jugador.playerID].inventory[balaID] > 0:
                                            self.estelaSurface.fill(self.estelaAlpha)
                                            bullet = nProyectil.Projectile(self.screen,(int(jugador.getPos()[0]+jugador.xCanon2-(self.WIDTH*0.028)),int(jugador.getPos()[1]+jugador.yCanon2-(self.HEIGHT*0.05))),balaID,potencia,jugador.angulo,self.listaJugadores,self.gravity,wind)
                                            self.terrain.updateImpact(bullet.shoot(surfaces,self.terrain.getDiccionary(),self.info,turnos[0]),bullet,self.listaJugadores,self.listaPlayers,jugadoresDerrotados,turnos[0])
                                            self.listaPlayers[jugador.playerID].inventory[balaID] -=1 #bala
                                            self.cantidadbullets -= 1
                                            self.comprobarBalasJugador(self.listaJugadores[turnos[0]])
                                            self.info.actualizarCantidadBalas(self.listaPlayers[jugador.playerID].inventory[balaID])
                                            playerPhysics.fallTanks(self.screen,self.listaJugadores,self.terrain.getDiccionary(),self.listaPlayers,jugadoresDerrotados,drawFunctions.returnSurface([self.backGround,self.terrain.surfTerrain]),self.gravity)
                                            self.listaJugadores[turnos[0]].turnoTanque(False)
                                            turnos[0] = -1
                                            chooseWind = False
                                        else:
                                            pass
                                            #print('no quedan')
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
                                    pass
                                    #print('pausa') #yo (mariano) lo arreglo dsps
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
                        ##print("potencia: " + str(potencia))
                    else:
                        turnos[0] = -1
            else:
                running = False
            if running != False:
                clock.tick(60)
                self.actualizarPantallasJuego()
                self.powerBar.dibujar(self.screen)
                pygame.display.update()
        



def testgame():#Logica de mainScreen()
    pygame.init()
    clock = pygame.time.Clock()
    WIDTH = params.size*16
    HEIGHT = params.size*9
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    run = True
    numeroPartidos = 3
    pantallaActual = 0
    while run:
        if pantallaActual == 0:
            partidosActuales = 0
            listaJugadores = []
            ia = False
            resetTanks = functions.loadPlayers(listaJugadores,window,ia)
            while partidosActuales < numeroPartidos:
                mapa = ["Mapas/galaxia.png",9.8]
                functions.resetTanks(listaJugadores,resetTanks,window)
                functions.anhadirDiezmo(listaJugadores)
                #tienda 
                game = gameLogic(window,listaJugadores,mapa)
                game.run(clock)
                partidosActuales += 1
        #print("pantaalla actual: "+str(pantallaActual))
        ##print("not reach")
        clock.tick(60)
        pygame.display.update()
#testgame()
