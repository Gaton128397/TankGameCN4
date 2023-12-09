import pygame
import sys
import button,params

class Difficulty:
    def __init__(self):
        self.x = 100
        self.width, self.height = params.WIDTH, params.HEIGHT
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.dificultad_background = params.difficulty
        

        self.clock = pygame.time.Clock()

        self.home_button = button.Button((self.x*0.5 - params.size*0.1, self.x*0.5 - params.size*0.2, params.size*0.1, params.size*0.1), (255, 0, 0), 'Home', False)
        self.confirmar_button = button.Button((self.width - self.x*3.5 - params.size*0.2, self.height - self.x*1.25 - params.size*0.5, self.x*3, self.x*0.75), (255, 255, 0), 'Confirmar', False)
        self.facil_button = button.Button((self.width // 2 + self.x*0.5 - params.size*2.9, self.height // 2 + params.size*0.3, params.size*0.12, params.size*0.8), (0, 255, 0), 'Fácil', False)
        self.normal_button = button.Button((self.width // 2 + self.x*0.5 - params.size*1, self.height // 2 + params.size*0.3, params.size*0.12, params.size*0.8), (0, 255, 0), 'Normal', False)
        self.dificil_button = button.Button((self.width // 2 + self.x*0.5 + params.size*0.85, self.height // 2 + params.size*0.3, params.size*0.12, params.size*0.8), (0, 255, 0), 'Difícil', False)

        self.buttons = [self.home_button, self.confirmar_button, self.facil_button, self.normal_button, self.dificil_button]
        self.dificulty = 0
    def runDificultad(self):
        pygame.init()
        self.screen.blit(self.dificultad_background, (0, 0))
        
        while True:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for btn in self.buttons:
                if btn.check_click(event):
                    if btn.item == 'Home':
                        return 0
                    elif btn.item == 'Confirmar':
                        return [2,self.dificulty]
                        pygame.quit()
                        sys.exit()
                    elif btn.item == 'Fácil':
                        self.dificulty = 0
                    elif btn.item == 'Normal':
                        self.dificulty = 1
                    elif btn.item == 'Difícil':
                        self.dificulty = 2

            pygame.display.flip()
            self.clock.tick(60)

# if __name__ == "__main__":
# run_dificultad()
