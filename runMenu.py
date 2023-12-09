import pygame,sys,button,params

class Menu:
    def __init__(self):
        self.x = params.size
        self.width, self.height = params.WIDTH, params.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.menu_background = params.menuImg        

        self.clock = pygame.time.Clock()

        self.play_button = button.Button((self.x*2, self.height // 2 - self.x*0.45, self.x*4, self.x*0.75 + params.size*0.2), (0, 255, 0), 'Play', False)
        self.settings_button = button.Button((self.x, self.height - self.x*1.25, self.x*4 + params.size*0.1, self.x*0.75), (255, 0, 0), 'Settings', False)
        self.controls_button = button.Button((self.x*5 + params.size*0.75, self.x*6 + params.size*1.75, self.x*3, self.x*0.75), (0, 0, 255), 'Controls', False)
        self.exit_button = button.Button((self.width - self.x*3.5, self.height - self.x*1.25, self.x*3, self.x*0.75), (255, 255, 0), 'Exit', False)

        self.buttons = [self.play_button, self.settings_button, self.controls_button, self.exit_button]
        
    def runMenu(self):
        pygame.init()
        self.screen.blit(self.menu_background, (0, 0))
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for btn in self.buttons:
                    if btn.check_click(event):
                        if btn.item == 'Play': #start choosing who to play against
                            return 1
                        elif btn.item == 'Settings':
                            return 3
                        elif btn.item == 'Controls':
                            return 7
                        elif btn.item == 'Exit':
                            pygame.quit()
                            running =  False
                            sys.exit()
                            
                
                pygame.display.flip()
            self.clock.tick(60)
            # return False #salir

