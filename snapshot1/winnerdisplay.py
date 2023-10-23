import pygame,time

class Winner:
    def init(self,screen,width,height):
        self.screen = screen
        self.width = width
        self.height = height
        
        self.ARENA_COLOR = (244, 164, 96)

        self.buttonRePlay = pygame.Rect(550, 520, 275, 75) 

        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)


    def drawWinner(self,winner):
        time.sleep(0.2)
        self.screen.fill('gold')
        textoGanar = self.big_font.render("Gana Jugador "+str(winner), True, 'black')
        self.screen.blit(textoGanar, (self.width//2-200, self.height//2))
        
        # Dibujar el botón "Volver a jugar"
        pygame.draw.rect(self.screen, self.ARENA_COLOR, self.buttonRePlay)  
        text = self.big_font.render("Volver a jugar", True, 'white')
        text_rect = text.get_rect(center=self.buttonRePlay.center)
        self.screen.blit(text, text_rect)