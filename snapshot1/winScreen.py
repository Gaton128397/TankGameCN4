import pygame,time

class Winner:
    def __init__(self,screen,width,height):
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)
    def drawWinner(self,winner):
        time.sleep(0.2)
        self.screen.fill('gold')
        textoGanar = self.big_font.render("Gana Jugador "+str(winner), True, 'black')
        self.screen.blit(textoGanar, (self.width//2-200, self.height//2))
