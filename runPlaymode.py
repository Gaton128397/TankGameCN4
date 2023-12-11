import pygame
import sys
import button,params
class Playmode:
    def __init__(self):
        self.x = params.size
        self.width, self.height = params.WIDTH, params.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.play_mode_background = params.playModeImg

        self.clock = pygame.time.Clock()

        self.friends_button = button.Button((self.x*2 + params.size, self.height // 2 - self.x*0.45, self.x*3, self.x*0.75), (0, 255, 0), 'Amigos', False)
        self.cpu_button = button.Button((self.x*10 + params.size*0.3, self.height // 2 - self.x*0.45, self.x*3, self.x*0.75), (0, 255, 0), 'CPU', False)
        self.confirm_button = button.Button((self.x*5 + params.size*1.5, self.x*6 + 125, self.x*3, self.x*0.75), (0, 0, 255), 'Confirmar', False)

        self.buttons = [self.friends_button, self.cpu_button, self.confirm_button]
        self.modo = None
    def runPlaymode(self):
        pygame.init()
        self.screen.blit(self.play_mode_background, (0, 0))

        while True:
            self.confirm_button.draw(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for btn in self.buttons:
                    if btn.check_click(event):
                        if btn.item == 'Amigos':
                            print('boton amigos')
                            self.modo = 'Amigos'
                        elif btn.item == 'CPU':
                            print('boton cpu')
                            self.modo = 'CPU'
                        elif btn.item == 'Confirmar':
                            print('boton confirmar')
                            if self.modo == 'Amigos':
                                # print(self.modo)
                                return[4,0]
                            elif self.modo == 'CPU':
                                # print(self.modo)
                                return[4,1]
                            
                            #pantalla dificultad cpu
                pygame.display.flip()
                self.clock.tick(60)