import pygame
import sys
import button,params
class Pausa:
    def __init__(self):
        self.x = 100
        self.width, self.height = params.WIDTH, params.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.pausa_background = params.pausaImg
        

        self.clock = pygame.time.Clock()

        self.home_button = button.Button((self.width // 2 - (self.x*4 + params.size*0.1) // 2, self.height // 2 - self.x*0.45 - params.size, self.x*4 + params.size*0.1, self.x*0.75), (255, 0, 0), 'Home', False)
        self.settings_button = button.Button((self.width // 2 - (self.x*4 + params.size*0.1) // 2, self.height // 2 - self.x*0.45 , self.x*4 + params.size*0.1, self.x*0.75), (255, 0, 0), 'Settings', False)
        self.controls_button = button.Button((self.width // 2 - (self.x*4 + params.size*0.1) // 2, self.height // 2 + params.size, self.x*4 + params.size*0.1, self.x*0.75), (0, 0, 255), 'Controls', False)
        self.exit_button = button.Button((self.width // 2 - self.x*1.5, self.height - self.x*1.25, self.x*3, self.x*0.75), (255, 255, 0), 'Exit', False)

        self.buttons = [self.home_button, self.settings_button, self.controls_button, self.exit_button]
        
    def runPausa(self,lastScreen): #lastScreen es la pantalla que se estaba ejecutando antes de pausa
        pygame.init()
        self.screen.blit(self.pausa_background, (0, 0))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_ESCAPE:
                        return 5 #regresa a la pantalla que se estaba ejecutando antes de pausa
                for btn in self.buttons:
                    if btn.check_click(event):
                        if btn.item == 'Home':
                            return 0
                        elif btn.item == 'Settings':
                            return 3
                        elif btn.item == 'Controls':
                            return 7
                        elif btn.item == 'Exit':
                            pygame.quit()
                            running = False
                            sys.exit()
            
                pygame.display.flip()
                self.clock.tick(60)

