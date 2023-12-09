import pygame,sys,button,params
from pygame_widgets.slider import Slider

class settings:
    def __init__(self):
        self.x = params.size
        self.width, self.height = params.WIDTH, params.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.settings_background = params.settingsPausa
        

        self.clock = pygame.time.Clock()

        self.home_button = button.Button((self.x*0.5 - params.size*0.1, self.x*0.5 - params.size*0.2, params.size, params.size), (255, 0, 0), 'Home', False)
        self.confirmar_button = button.Button((self.width - self.x*1.5 - params.size*2.5, self.x*0.5 - params.size*0.25, 300, 100), (255, 0, 0), 'Settings', False)

        self.buttons = [self.home_button, self.confirmar_button, self.mas_player_button, self.menos_player_button, self.mas_ronda_button, self.menos_ronda_button]
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
                        pygame.quit()
                        sys.exit()
                    elif btn.item == 'Settings':
                        return 7
                        pygame.quit()
                        sys.exit()
            pygame.display.flip()
            self.clock.tick(60)

