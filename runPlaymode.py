import pygame
import sys
import button
class Playmode:
    def __init__(self,screen):
        self.x = 100
        self.width, self.height = 16*self.x, 9*self.x
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.play_mode_background = pygame.image.load('imgs/playmode.png')  
        self.play_mode_background = pygame.transform.scale(self.play_mode_background, (self.width, self.height))
        

        self.clock = pygame.time.Clock()

        self.friends_button = button.Button((self.x*2 + 100, self.height // 2 - self.x*0.45, self.x*3, self.x*0.75), (0, 255, 0), 'Amigos', False)
        self.cpu_button = button.Button((self.x*10 + 30, self.height // 2 - self.x*0.45, self.x*3, self.x*0.75), (0, 255, 0), 'CPU', False)
        self.confirm_button = button.Button((self.x*5 + 150, self.x*6 + 125, self.x*3, self.x*0.75), (0, 0, 255), 'Confirmar', False)


        self.buttons = [self.friends_button, self.cpu_button, self.confirm_button]
        self.modo = None
    def runPlaymode(self):
        pygame.init()
        self.screen.blit(self.play_mode_background, (0, 0))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                for btn in self.buttons:
                    if btn.check_click(event):
                        if btn.item == 'Amigos':
                            self.modo = 'Amigos'
                        elif btn.item == 'CPU':
                            self.modo = 'CPU'
                        elif btn.item == 'Confirmar':
                            if self.modo == 'Amigos':
                                print(self.modo)
                                return 2
                            elif self.modo == 'CPU':
                                print(self.modo)
                                return 10 #pantalla dificultad cpu
                pygame.display.flip()
                self.clock.tick(60)
