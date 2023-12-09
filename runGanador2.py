import pygame
import sys
import button,params
class Ganador2:
    def __init__(self):
        self.x = 100
        self.width, self.height = params.WIDTH, params.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.ganador1_background = params.bGanador2


        self.clock = pygame.time.Clock()

        self.home_button = button.Button((self.x*0.5 - params.size*0.1, self.x*0.5 - params.size*0.2, params.size, params.size), (255, 0, 0), 'Home', False)
        self.settings_button = button.Button((self.width - self.x*1.5 +params.size*0.015, self.x*0.5 - 25, params.size, params.size), (255, 0, 0), 'Settings', False)
        self.siguiente_ronda_button = button.Button((self.width // 2 - self.x*1.5 - params.size*0.75, self.x*6 + params.size*1.75, self.x*3 + params.size*1.5, self.x*0.75), (0, 255, 0), 'Siguiente Ronda', False)
        self.terminar_juego_button = button.Button((self.width - self.x*3.5 + params.size*0.15, self.height - self.x*1.25, self.x*3, self.x*0.75), (255, 255, 0), 'Terminar Juego', False)

        self.buttons = [self.home_button, self.settings_button, self.siguiente_ronda_button, self.terminar_juego_button]

    def runGanador2(self): #es cuando una ronda acaba
        pygame.init()
        self.screen.blit(self.ganador2_background, (0, 0))
        
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
                        elif btn.item == 'Siguiente Ronda':
                            return 'siguiente ronda' #ver esto con gaston
                        elif btn.item == 'Terminar Juego':
                            pygame.quit()
                            sys.exit()
                pygame.display.flip()
                self.clock.tick(60)

