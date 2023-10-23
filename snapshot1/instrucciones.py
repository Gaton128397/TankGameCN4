import pygame
import sys


def draw_instrucciones(surfaceInstrucciones,width,heihgt):
    background = pygame.image.load("snapshot1/Background.jpg")
    background = pygame.transform.scale(background, (width, heihgt))

    ARENA_COLOR = (255, 204, 153) 
    CACTUS_GREEN = (85, 107, 47)

    buttonVolver = pygame.Rect(550, 520, 200, 50) 

    font = pygame.font.Font(None, 36)
    big_font = pygame.font.Font(None, 72)

    instrucciones = [
    "1. Mueve el cañón del tanque con las teclas de flecha hacia arriba y flecha hacia abajo",
    "2. Manten la barra espaciadora para la potencia del disparo.",
    "3. Cambia con las teclas 1 , 2 y 3 el tipo de bala.",
    "4. Tienes que estar atento a las municiones de cada bala.",
    "5. Debes estar atento a tu vida, si llega a 0 perderas la partida."
    ]
    surfaceInstrucciones.blit(background, (0, 0)) 

    text = font.render("INSTRUCCIONES", True, CACTUS_GREEN)  
    text_rect = text.get_rect(center=(width//2, 100))
    surfaceInstrucciones.blit(text, text_rect)
    
    # Dibujar lista de instrucciones
    for i, instruccion in enumerate(instrucciones):
        text = font.render(instruccion, True, CACTUS_GREEN)  
        text_rect = text.get_rect(center=(width//2, 200 + i*50))
        surfaceInstrucciones.blit(text, text_rect)
    
    # Dibujar el botón "Volver"
    button = pygame.Rect(550, 520, 200, 50) 
    pygame.draw.rect(surfaceInstrucciones, ARENA_COLOR, button)  
    text = font.render("Volver", True, 'white')
    text_rect = text.get_rect(center=button.center)
    surfaceInstrucciones.blit(text, text_rect)
    return buttonVolver
    # pygame.display.update()
