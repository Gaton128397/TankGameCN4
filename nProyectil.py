import math,pygame,params, drawFunctions, nTerrain, nTank, random, playerPhysics, ninfoBlock, functions

def cargarProyectil(surf, imagen, proporcionX, proporcionY, posicion):
    imagen_cargada = pygame.image.load(imagen)
    imagen_escalada = pygame.transform.scale(imagen_cargada, (surf.get_width()*proporcionX, surf.get_height()*proporcionY))
    surf.blit(imagen_escalada, (posicion))
class Projectile():
    def __init__(self,window,position, typeBullet,power, theta,listaJugador,gravity,wind):
        self.WIDTH = params.size*16
        self.HEIGHT = params.size*9
        #pantalla donde se ejecutara la visual del proyectil
        self.window = window
        
        #almacena los jugadores que estan en la partida
        self.listaJugador = listaJugador
        
        #tipo de proyectil que se va a disparar
        self.typeBullet = typeBullet
        
        #superficie del proyectil
        self.surf = pygame.Surface((self.WIDTH*0.05,self.HEIGHT*0.07))
        
        #clave de color para el proyectil
        self.alphaColor = (255,0,255)
        self.surf.fill(self.alphaColor)
        self.surf.set_alpha()
        self.surf.set_colorkey(self.alphaColor)
        
        #potencia del disparo

        
        #radio de explosion del proyectil
        self.blastRadius = 0
        
        #daño que hace el proyectil
        self.DMG = 0
        
        #gravedad del proyectil
        self.g = gravity
        
        #intensidad del viento
        self.wind = wind
        
        #posiciones del proyectil
        self.xPositions = []
        self.yPositions = []
        
        #tipo de proyectil 1
        if self.typeBullet == 3: #105mm
            cargarProyectil(self.surf,"items/105mmStone.png",1,1,(0,0))
            pygame.draw.circle(self.surf, (0,0,0), (int(self.surf.get_width()/2),int(self.surf.get_height()/2)), 2)
            self.blastRadius = int(self.WIDTH*0.07)
            self.DMG = 50
            
        #tipo de proyectil 2
        elif self.typeBullet == 4: #80mm
            cargarProyectil(self.surf,"items/60mmStone.png",1,1,(0,0))
            pygame.draw.circle(self.surf, (0,0,0), (int(self.surf.get_width()/2),int(self.surf.get_height()/2)), 2)
            self.blastRadius = int(self.WIDTH*0.05)
            self.DMG = 40
            
        #tipo de proyectil 3
        elif self.typeBullet == 5: #60mm
            cargarProyectil(self.surf,"items/80mmStone.png",0.6,0.6,(0,0))
            pygame.draw.circle(self.surf, (0,0,0), (int(self.surf.get_width()/2),int(self.surf.get_height()/2)), 2)
            self.blastRadius = int(self.WIDTH*0.03)
            self.DMG = 30
            
        self.yMaxHeight = position[1]
        self.pos = []
        self.pos.append(position[0])
        self.pos.append(self.HEIGHT-position[1])
        functions.draw_trajectory(power, theta, self.g, self.xPositions,self.yPositions, self.pos, self.wind)
        
    def shoot(self,listaDeSurface,puntosTerreno,infoBlock,turno):
        puntox = int(self.surf.get_width()/2)
        puntoy = int(self.surf.get_height()/2)
        shoot = True
        clock = pygame.time.Clock()
        contador = 0
        maxHeight = self.HEIGHT
        while shoot:
            clock.tick(200)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    shoot = False
            xIni = self.xPositions.pop(0) 
            yIni = (self.HEIGHT-self.yPositions.pop(0)) 
            x = xIni + puntox
            y = yIni + puntoy
            if contador == 5:
                pygame.draw.circle(listaDeSurface[3], (0,0,0), (int(x),int(y)), int(self.HEIGHT*0.006))
                contador = 0
            self.window.blit(listaDeSurface[0],(0,0))
            self.window.blit(listaDeSurface[1],(0,0))
            self.window.blit(listaDeSurface[3],(0,0))
            self.window.blit(listaDeSurface[4],(0,0))
            self.window.blit(listaDeSurface[5],(self.WIDTH*0,self.HEIGHT*0.1))
            distancia = functions.calcular_distancia((x,y),(self.pos[0]+puntox,self.pos[1]+puntoy))
            infoBlock.actualizarDistancia(int(distancia))
            self.listaJugador[turno].distancia = int(distancia)
            self.window.blit(self.surf,(xIni,yIni))
            self.window.blit(infoBlock.bloque,(self.WIDTH*0.68,0))
            if maxHeight > y:
                maxHeight = y
                self.actualizarMaxHeight(listaDeSurface[3],int(maxHeight))
            for i in range(len(self.listaJugador)):
                self.window.blit(self.listaJugador[i].surfaceTank,self.listaJugador[i].getPos())
            if (int(x),int(y)) in puntosTerreno:
                return (int(x),int(y))
            else:
                for i in range(len(self.listaJugador)):
                    if (int(x),int(y)) in self.listaJugador[i].hitBox:
                        return (int(x),int(y))
            if x > self.WIDTH or x < 0 or y > self.HEIGHT:
                return (int(x),int(y))
            
            contador += 1
            pygame.display.update()
    def actualizarMaxHeight(self,surface, texto):
        texto = self.yMaxHeight - texto
        texto = str(texto)
        pygame.draw.rect(surface, (255,255,255), pygame.Rect(int(surface.get_width() *0), int(surface.get_height() *0.05), int(surface.get_width() *0.2), int(surface.get_height() *0.07)))
        texto = "Max height: "+ texto + "m"
        fuente = pygame.font.Font(None, int(surface.get_width() *0.02))
        superficie_texto = fuente.render(texto, True, (0, 0, 0))
        surface.blit(superficie_texto, (int(surface.get_width() *0), int(surface.get_height() *0.07)))