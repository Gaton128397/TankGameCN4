import pygame,sys#,mainScreen

pygame.init()

WIDTH,HEIGHT = 1300,700
screen = pygame.display.set_mode((WIDTH, HEIGHT))


#Menu
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Menu:
    def __init__(self,window,WIDTH, HEIGHT):
        self.screen = window
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT  
        self.background = pygame.image.load("Background.jpeg")
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
        self.ARENA_COLOR = (244, 164, 96) 
        self.CACTUS_GREEN = (85, 107, 47)
        
        self.buttonPlay = pygame.Rect(475, 305, 350, 150)
        self.buttonExit = pygame.Rect(475, 485, 350, 150)
    def draw_menu(self):
        
        
        self.screen.blit(self.background, (0, 0))

        font = pygame.font.Font(None,150)
        text = font.render("Canyon-4", True, self.CACTUS_GREEN) 
        text_rect = text.get_rect(center=(self.WIDTH//2, 200))
        self.screen.blit(text, text_rect)

        #botón "Jugar"
        pygame.draw.rect(self.screen, self.ARENA_COLOR, self.buttonPlay)
        text = font.render("Jugar", True, 'white')
        text_rect = text.get_rect(center=self.buttonPlay.center)
        self.screen.blit(text, text_rect)

        #botón "Salir"
        pygame.draw.rect(self.screen, self.ARENA_COLOR, self.buttonExit)
        text = font.render("Salir", True, 'white')
        text_rect = text.get_rect(center=self.buttonExit.center)
        self.screen.blit(text, text_rect)
        
        


#Codigo para saber si funciona el boton jugar
def draw_red_screen():
    screen.fill('red')
    pygame.display.flip()

def main():
    menu1 = Menu(WIDTH,HEIGHT)
    # menu1.draw_menu()
    # menu1.getButton()
    while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if menu1.buttonPlay.collidepoint(event.pos):
                        draw_red_screen()
                        #mainScreen.game()

                    elif menu1.buttonExit.collidepoint(event.pos):
                        pygame.quit()
                        sys.exit()
            menu1.draw_menu()


if __name__ == "__main__":
    main()
