import pygame
import sys
import button
class Pausa:
    def __init__(self,screen):
        self.x = 100
        self.width, self.height = 16*self.x, 9*self.x
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.pausa_background = pygame.image.load('imgs/pausa.png')  
        self.pausa_background = pygame.transform.scale(self.pausa_background, (self.width, self.height))
        

        self.clock = pygame.time.Clock()

        self.home_button = button.Button((self.width // 2 - (self.x*4 + 10) // 2, self.height // 2 - self.x*0.45 - 100, self.x*4 + 10, self.x*0.75), (255, 0, 0), 'Home', False)
        self.settings_button = button.Button((self.width // 2 - (self.x*4 + 10) // 2, self.height // 2 - self.x*0.45 , self.x*4 + 10, self.x*0.75), (255, 0, 0), 'Settings', False)
        self.controls_button = button.Button((self.width // 2 - (self.x*4 + 10) // 2, self.height // 2 + 100, self.x*4 + 10, self.x*0.75), (0, 0, 255), 'Controls', False)
        self.exit_button = button.Button((self.width // 2 - self.x*1.5, self.height - self.x*1.25, self.x*3, self.x*0.75), (255, 255, 0), 'Eself.xit', False)

        self.buttons = [self.home_button, self.settings_button, self.controls_button, self.exit_button]
    def runPausa(self,):
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
                        return 7
                for btn in self.buttons:
                    if btn.check_click(event):
                        if btn.item == 'Home':
                            return 0
                        elif btn.item == 'Settings':
                            return 4
                        elif btn.item == 'Controls':
                            print('nothing yet')
                            return 3
                        elif btn.item == 'Exit':
                            pygame.quit()
                            running = False
                            sys.exit()
            
                pygame.display.flip()
                self.clock.tick(60)
        return 4 #pantalla de juego

