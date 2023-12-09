import pygame
import sys
import button,params

class Settings():
    def __init__(self):
        self.x = 100
        self.width, self.height = params.WIDTH, params.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.settings_background = params.settingsPausa

        self.clock = pygame.time.Clock()

        self.home_button = button.Button((self.x*0.5 - params.size*0.1, self.x*0.5 - params.size*0.2, params.size, params.size), (255, 0, 0), 'Home', False)
        self.confirmar_button = button.Button((self.width - self.x*1.5 - params.size*2.5, self.x*0.5 + params.size*6.5, params.size*3, params.size), (255, 0, 0), 'Settings', False)

        self.buttons = [self.home_button, self.confirmar_button]
    def runSettings(self):
        pygame.init()

        

        while True:
            
            self.screen.blit(self.settings_background, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for btn in self.buttons:
                if btn.check_click(event):
                    if btn.item == 'Home':
                        print('boton home')
                        pygame.quit()
                        sys.exit()
                    elif btn.item == 'Settings':
                        print('confirmar')
                        pygame.quit()
                        sys.exit()                    
                        
            pygame.display.flip()
            self.clock.tick(60)

# if __name__ == "__main__":
#     run_settings()
