import pygame,sys,button,params
class settings:
    def __init__(self,screen):
        self.x = params.size
        self.width, self.height = 16*self.x, 9*self.x
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.settings_background = pygame.image.load('imgs/settings.png')  
        self.settings_background = pygame.transform.scale(self.settings_background, (self.width, self.height))
        

        self.clock = pygame.time.Clock()

        self.home_button = button.Button((self.x*0.5 - 10, self.x*0.5 - 20, 100, 100), (255, 0, 0), 'Home', False)
        self.settings_button = button.Button((self.width - self.x*1.5 +15, self.x*0.5 - 25, 100, 100), (255, 0, 0), 'Settings', False)
        self.mas_player_button = button.Button((self.width // 2 + 510, self.height // 2 - 120, 100, 75), (0, 255, 0), 'MasPlayer', False)
        self.menos_player_button = button.Button((self.width // 2 + 210, self.height // 2 - 120, 100, 75), (0, 255, 0), 'MenosPlayer', False)

        self.mas_ronda_button = button.Button((self.width // 2 + 510, self.height // 2 + 275, 100, 75), (0, 255, 0), 'MasRonda', False)
        self.menos_ronda_button = button.Button((self.width // 2 + 210, self.height // 2 + 275, 100, 75), (0, 255, 0), 'MenosRonda', False)


        self.buttons = [self.home_button, self.settings_button, self.mas_player_button, self.menos_player_button, self.mas_ronda_button, self.menos_ronda_button]
        self.jugadores = 2
        self.rondas = 1
    def runSettings(self):
        pygame.init()
        self.screen.blit(self.settings_background, (0, 0))
        
        running = True
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for btn in self.buttons:
                    if btn.check_click(event):
                        if btn.item == 'Home':
                            return 0
                            # sys.exit()
                            
                            
                        elif btn.item == 'Settings':
                            running = False#deberia continuar a la pantalla y no ser arriba
                        elif btn.item == 'MasPlayer':
                            self.jugadores += 1
                            
                        elif btn.item == 'MenosPlayer':
                            self.jugadores -= 1
                        elif btn.item == 'MasRonda':
                            self.rondas += 1
                        elif btn.item == 'MenosRonda':
                            self.rondas -= 1
                pygame.display.flip()
            self.clock.tick(60)
        return [4,self.jugadores,self.rondas]
