import pygame
import sys

class Instrucciones:
    def __init__(self,screen,WIDTH,HEIGHT):
        self.screen = screen
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.background = pygame.image.load("snapshot1/Background.jpg")
        self.background = pygame.transform.scale(self.background, (self.WIDTH, self.HEIGHT))
        
        self.ARENA_COLOR = (255, 204, 153) 
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

    text = big_font.render("INSTRUCCIONES", True, CACTUS_GREEN)  
    text_rect = text.get_rect(center=(screen.get_width()//2, 100))
    screen.blit(text, text_rect)
    
    # Dibujar lista de instrucciones
    for i, instruccion in enumerate(instrucciones):
        text = font.render(instruccion, True, CACTUS_GREEN)  
        text_rect = text.get_rect(center=(screen.get_width()//2, 200 + i*50))
        screen.blit(text, text_rect)
    
    # Dibujar el botón "Volver"
    button = pygame.Rect(550, 520, 200, 50) 
    pygame.draw.rect(screen, ARENA_COLOR, button)  
    text = font.render("Volver", True, WHITE)
    text_rect = text.get_rect(center=button.center)
    screen.blit(text, text_rect)

    pygame.display.flip()


mostrar_instrucciones()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:  
            if button.collidepoint(event.pos):  
                print("Botón Volver presionado")  # Aquí puedes agregar la acción que deseas

                # Por ejemplo, puedes agregar aquí la acción de volver a una pantalla anterior.