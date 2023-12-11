import pygame,sys,button,params,random,createMap

class Maps:
    def __init__(self):
        self.x = params.size
        self.width, self.height = 16*self.x, 9*self.x
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.maps_background = params.bgMapas
        

        self.clock = pygame.time.Clock()

        self.home_button = button.Button((self.x*0.5 - self.x*0.1, self.x*0.5 - params.size*0.2, 100, 100), (255, 0, 0), 'Home', False)
        self.settings_button = button.Button((self.width - self.x*1.5 + params.size*0.15, self.x*0.5 - params.size*0.25, 100, 100), (255, 0, 0), 'Settings', False)
        self.confirmar_button = button.Button((self.width - params.size*3, self.height - params.size*1, 250, 80), (0, 255, 0), 'Confirmar', False)



        self.random_map_button = button.Button((self.width // 2 - params.size*6.15, self.height // 2 - params.size*1.85, params.size*3, params.size*1.75), (0, 255, 0), 'Random Map', False)
        self.selva_button = button.Button((self.width // 2 - params.size*2.35, self.height // 2 - params.size*1.85, params.size*3, params.size*1.75), (0, 255, 0), 'Selva', False)
        self.galaxy_button = button.Button((self.width // 2 + params.size*1.55, self.height // 2 - params.size*1.85, params.size*3, params.size*1.75), (0, 255, 0), 'Galaxy', False)

        self.nieve_button = button.Button((self.width // 2 - params.size*6.15, self.height // 2 + params.size*1.25, params.size*3, params.size*1.75), (0, 255, 0), 'Nieve', False)
        self.desierto_button = button.Button((self.width // 2 - params.size*2.4, self.height // 2 + params.size*1.25, params.size*3, params.size*1.75), (0, 255, 0), 'Desierto', False)
        self.ciudad_button = button.Button((self.width // 2 + params.size*1.6, self.height // 2 + params.size*1.25, params.size*3, params.size*1.75), (0, 255, 0), 'Ciudad', False)

        self.buttons = [self.home_button, self.settings_button, self.confirmar_button,
                self.random_map_button, self.selva_button, self.galaxy_button,
                self.nieve_button, self.desierto_button, self.ciudad_button]
        self.selectedMap = 0

        #MAPAS
        self.desierto = createMap.Map(params.mapaDesert, 9.8, 2, 'yellow') #gravedad = 0 y viento = 0
        self.selva = createMap.Map(params.mapaSelva, 9.8, 4, 'green')
        self.nieve = createMap.Map(params.mapaSnow, 9.8, 8, 'white')
        self.galaxia = createMap.Map(params.mapaGalaxia, 5.2, 0, 'purple')
        self.ciudad = createMap.Map(params.mapaCiudad, 9.8, 6, 'grey')
        self.mapas = [self.desierto, self.selva, self.nieve, self.galaxia, self.ciudad]
    def runMaps(self):
        pygame.init()
        self.screen.blit(self.maps_background, (0, 0))
        

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for btn in self.buttons:
                    if btn.check_click(event):
                        if btn.item == 'Home':
                            return 0
                        elif btn.item == 'Settings':
                            return 3
                        elif btn.item == 'Confirmar':
                            if self.selectedMap == 'Random Map':
                                return [5,self.mapas[random.randint(0,4)]] #mapa al azar
                            elif self.selectedMap == 'Desierto':
                                return [5,self.desierto]
                            elif self.selectedMap == 'Selva':
                                return [5,self.selva]
                            elif self.selectedMap == 'Nieve':
                                return [5,self.nieve]
                            elif self.selectedMap == 'Galaxy':
                                return [5,self.galaxia]
                            elif self.selectedMap == 'Ciudad':
                                return [5,self.ciudad]
                        else:
                            print(btn.item)
                            self.selectedMap = btn.item
            pygame.display.flip()
            self.clock.tick(60)

