import pygame,sys
#Menu
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Menu:
    def __init__(self,window,WIDTH, HEIGHT):
        self.screen = window
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.background = pygame.image.load("snapshot1/Background.jpg")
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))

        self.ARENA_COLOR = (255, 204, 153)
        self.CACTUS_GREEN = (85, 107, 47)

        self.small_font = pygame.font.Font(None, 50)
        self.font = pygame.font.Font(None, 150)
        
        self.buttonPlay = pygame.Rect(500, 305, 250, 75)
        self.buttonControls = pygame.Rect(500, 405, 250, 75)
        self.buttonExit = pygame.Rect(975, 585, 250, 75)
        
    
    def draw_menu(self):
        self.screen.blit(self.background, (0, 0))


        #titulo
        text = self.font.render("Canyon-4", True, self.CACTUS_GREEN) 
        text_rect = text.get_rect(center=(self.WIDTH//2, 200))
        self.screen.blit(text, text_rect)

        #botón "Jugar"
        pygame.draw.rect(self.screen, self.ARENA_COLOR, self.buttonPlay)
        text = self.small_font.render("Jugar", True, 'white')
        text_rect = text.get_rect(center=self.buttonPlay.center)
        self.screen.blit(text, text_rect)

        #botón "controles"
        pygame.draw.rect(self.screen, self.ARENA_COLOR, self.buttonControls)
        text = self.small_font.render("Controles", True, 'white')
        text_rect = text.get_rect(center=self.buttonControls.center)
        self.screen.blit(text, text_rect)

        #botón "Salir"
        pygame.draw.rect(self.screen, self.ARENA_COLOR, self.buttonExit)
        text = self.small_font.render("Salir", True, 'white')
        text_rect = text.get_rect(center=self.buttonExit.center)
        self.screen.blit(text, text_rect)
        # pygame.display.update()
        
    def delete_menu(self):
        self.buttonPlay = 0#pygame.Rect(500, 305, 250, 75)
        self.buttonControls =0# pygame.Rect(500, 405, 250, 75)
        self.buttonExit = 0#pygame.Rect(975, 585, 250, 75)
        # pygame.display.update()
