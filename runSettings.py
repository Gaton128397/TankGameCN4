import pygame,sys,button,params
import pygame_widgets
from pygame_widgets.slider import Slider
from pygame_widgets.textbox import TextBox
class settings:
    def __init__(self,screen):
        self.x = params.size
        self.width, self.height = params.WIDTH, params.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.settings_background = pygame.image.load('imgs/varios/settings.png')  
        self.settings_background = pygame.transform.scale(self.settings_background, (self.width, self.height))
        

        self.clock = pygame.time.Clock()

        self.home_button = button.Button((params.size*0.4,params.size*0.3,params.size,params.size*0.8), (255, 0, 0), 'Home', False)
        self.confirmar_button = button.Button((self.width - self.x*1.5 - params.size*2.5, self.x*0.5 - params.size*0.25, params.size*3, params.size), (255, 0, 0), 'Confirmar', False)
        self.mas_player_button = button.Button((self.width // 2 + params.size*5.1, self.height // 2 - params.size*1.2, params.size, params.size*0.75), (0, 255, 0), 'MasPlayer', False)
        self.menos_player_button = button.Button((self.width // 2 + params.size*2.1, self.height // 2 - params.size*1.2, params.size, params.size*0.75), (0, 255, 0), 'MenosPlayer', False)
        self.mas_ronda_button = button.Button((self.width // 2 + params.size*5.1, self.height // 2 + params.size*2.75, params.size, params.size*0.75), (0, 255, 0), 'MasRonda', False)
        self.menos_ronda_button = button.Button((self.width // 2 + params.size*2.1, self.height // 2 + params.size*2.75, params.size, params.size*0.75), (0, 255, 0), 'MenosRonda', False)
        
        self.Resolucion = Slider(self.screen, int(self.width*0.08),int(self.height*0.38), int(self.width*0.14), int(self.height*0.03), min=0, max=99, step=1)
        self.VolumeGame = Slider(self.screen, int(self.width*0.08),int(self.height*0.62), int(self.width*0.14), int(self.height*0.03), min=0, max=99, step=1)
        self.VolumeMusic = Slider(self.screen, int(self.width*0.08),int(self.height*0.92), int(self.width*0.14), int(self.height*0.03), min=0, max=99, step=1)
        
        self.outputResolucion = TextBox(self.screen, int(self.width*0.25), int(self.height*0.37), int(params.WIDTH/40), int(params.WIDTH/40), fontSize=int(params.size*0.3))
        self.outputResolucion.disable()
        self.outputVolumeGame = TextBox(self.screen, int(self.width*0.25), int(self.height*0.61), int(params.WIDTH/40), int(params.WIDTH/40), fontSize=int(params.size*0.3))
        self.outputVolumeGame.disable()
        self.outputVolumeMusic = TextBox(self.screen, int(self.width*0.25), int(self.height*0.91), int(params.WIDTH/40), int(params.WIDTH/40), fontSize=int(params.size*0.3))
        self.outputVolumeMusic.disable()

        self.CantidadJugadores = TextBox(self.screen, int(self.width*0.735), int(self.height*0.38), int(params.WIDTH/27), int(params.WIDTH/40), fontSize=int(params.size*0.3))
        self.CantidadJugadores.disable()
        self.CantidadRondas = TextBox(self.screen, int(self.width*0.735), int(self.height*0.83), int(params.WIDTH/27), int(params.WIDTH/40), fontSize=int(params.size*0.3))
        self.CantidadRondas.disable()
        
        self.buttons = [self.home_button, self.confirmar_button, self.mas_player_button, self.menos_player_button, self.mas_ronda_button, self.menos_ronda_button]
        self.jugadores = 2
        self.rondas = 1
    def runSettings(self):
        pygame.init()
        
        
        self.screen.blit(self.settings_background, (0, 0))
        
        running = True
        while True:
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for btn in self.buttons:
                    # btn.draw(self.screen) #ver posiciones de los botones
                    if btn.check_click(event):
                        if btn.item == 'Home':
                            print('boton home')
                            return 0
                        elif btn.item == 'Confirmar':
                            return 2
                            # print('boton config')
                            # pygame.quit()
                            # sys.exit()
                        elif btn.item == 'MasPlayer':
                            if self.jugadores < 6 and self.jugadores >= 0:
                                self.jugadores += 1

                        elif btn.item == 'MenosPlayer':
                            if self.jugadores > 2 and self.jugadores <= 6:
                                self.jugadores -= 1
                        elif btn.item == 'MasRonda':
                            if self.rondas < 5 and self.rondas >= 0:
                                self.rondas += 1

                        elif btn.item == 'MenosRonda':
                            if self.rondas > 1 and self.rondas <= 5:
                                self.rondas -= 1
                        
            self.outputResolucion.setText(self.Resolucion.getValue())
            self.outputVolumeGame.setText(self.VolumeGame.getValue())
            self.outputVolumeMusic.setText(self.VolumeMusic.getValue())
            self.CantidadJugadores.setText(self.jugadores)
            self.CantidadRondas.setText(self.rondas)
            pygame.draw.rect(self.screen, (255, 255, 255), (int(self.width*0.068),int(self.height*0.37), int(self.width*0.17), int(self.height*0.05)))
            pygame.draw.rect(self.screen, (255, 255, 255), (int(self.width*0.068),int(self.height*0.61), int(self.width*0.17), int(self.height*0.05)))
            pygame.draw.rect(self.screen, (255, 255, 255), (int(self.width*0.068),int(self.height*0.91), int(self.width*0.17), int(self.height*0.05)))
            pygame_widgets.update(events)
            pygame.display.flip()
            self.clock.tick(60)

