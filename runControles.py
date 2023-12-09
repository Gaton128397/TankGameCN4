import pygame
import sys
import button,params

class Controles():
    def __init__(self):
        self.x = 100
        self.width, self.height = params.WIDTH, params.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.settings_background = params.controlesImg 
        

        self.clock = pygame.time.Clock()

        self.home_button = button.Button((self.x*0.5 - params.size*0.1, self.x*0.5 - params.size*0.2, params.size, params.size), (255, 0, 0), 'Home', False)

        self.buttons = [self.home_button]
    def runControles(self,lastScreen):
        pygame.init()
        self.screen.blit(self.settings_background, (0, 0))
        

        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type==pygame.KEYDOWN: #si a
                    if event.key==pygame.K_ESCAPE:
                        return 6 #volver a pausa 
                for btn in self.buttons:
                    btn.draw(self.screen)
                    if btn.check_click(event):
                        if btn.item == 'Home':
                            return 0              
                pygame.display.flip()
                self.clock.tick(60)
