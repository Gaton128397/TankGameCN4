import pygame
import sys

class Instrucciones:
    def __init__(self,screen,WIDTH,HEIGHT):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.background = pygame.image.load("snapshot1/Background.jpeg")
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
        
        self.ARENA_COLOR = (244, 164, 96) 
        self.CACTUS_GREEN = (85, 107, 47)

        self.buttonVolver = pygame.Rect(550, 520, 200, 50) 

        self.font = pygame.font.Font(None, 36)
        self.big_font = pygame.font.Font(None, 72)

        self.instrucciones = [
        "1. Mueve el cañón del tanque con las teclas de flecha hacia arriba y flecha hacia abajo",
        "2. Manten la barra espaciadora para la potencia del disparo.",
        "3. Cambia con las teclas 1 , 2 y 3 el tipo de bala.",
        "4. Tienes que estar atento a las municiones de cada bala.",
        "5. Debes estar atento a tu vida, si llega a 0 perderas la partida."
        ]

    def draw_instrucciones(self):
        self.screen.blit(self.background, (0, 0)) 

        text = self.big_font.render("INSTRUCCIONES", True, self.CACTUS_GREEN)  
        text_rect = text.get_rect(center=(self.screen.get_width()//2, 100))
        self.screen.blit(text, text_rect)
        
        # Dibujar lista de instrucciones
        for i, instruccion in enumerate(self.instrucciones):
            text = self.font.render(instruccion, True, self.CACTUS_GREEN)  
            text_rect = text.get_rect(center=(self.screen.get_width()//2, 200 + i*50))
            self.screen.blit(text, text_rect)
        
        # Dibujar el botón "Volver"
        pygame.draw.rect(self.screen, self.ARENA_COLOR, self.buttonVolver)  
        text = self.font.render("Volver", True, 'white')
        text_rect = text.get_rect(center=self.buttonVolver.center)
        self.screen.blit(text, text_rect)