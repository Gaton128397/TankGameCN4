import pygame
import sys
import button,params

class Ganador1:
    def __init__(self):
        self.x = 100
        self.width, self.height = params.WIDTH, params.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.ganador1_background = params.bGganador1
        

        self.clock = pygame.time.Clock()

        self.home_button = button.Button((self.x*0.5 - params.size*0.1, self.x*0.5 - params.size*0.2, params.size, params.size), (255, 0, 0), 'Home', False)
        self.settings_button = button.Button((self.width - self.x*1.5 + params.size*0.15, self.x*0.5 - params.size*0.25, params.size, params.size), (255, 0, 0), 'Settings', False)
        self.iniciar_partida_button = button.Button((self.x*5 - params.size*4.75, self.x*6 + params.size*1.75, self.x*3, self.x*0.75), (0, 255, 0), 'Iniciar Partida', False)
        self.terminar_juego_button = button.Button((self.width - self.x*3.5, self.height - self.x*1.25, self.x*3, self.x*0.75), (255, 255, 0), 'Terminar Juego', False)

        self.buttons = [self.home_button, self.settings_button, self.iniciar_partida_button, self.terminar_juego_button]
    
    def runGanador1(self): #ganador 1 es cuando la partida acaba
        pygame.init()
        self.screen.blit(self.ganador1_background, (0, 0))
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for btn in self.buttons:
                    if btn.check_click(event):
                        if btn.item == 'Home':
                            print('Ir a la pantalla de inicio')
                            return 0
                        elif btn.item == 'Settings':
                            print('Ir a la configuración')
                            return 3
                        elif btn.item == 'Iniciar Partida':
                            print('Iniciar partida') #boton reinciar partida
                            return 'reiniciar partida' #revisar esto con gaston por el flujo
                        elif btn.item == 'Terminar Juego':
                            pygame.quit()
                            sys.exit()
                pygame.display.flip()
                self.clock.tick(60)

