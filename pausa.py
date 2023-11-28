import pygame,time
def drawPausa(pause,width,height):
    time.sleep(0.2)
    ARENA_COLOR = (244, 164, 96)
    buttonVolver = pygame.Rect(width*0.85, height*0.9, 80, 40) 

    font = pygame.font.Font(None, 36)
    big_font = pygame.font.Font(None, 72)
    pause.fill((228,249,124))

    textoEnd = big_font.render("PAUSADO", True, 'black')
    text_rectScreen = (width*0.6, height*0.5)
    pause.blit(textoEnd,text_rectScreen)
    
    
    # Dibujar el botón "Volver a jugar"

    # button = pygame.Rect(width*0.25, height*0.9, 650, 50) 
    # pygame.draw.rect(pause, ARENA_COLOR, button)  
    textVolver = font.render("'esc' para volver", True, 'black')
    textReiniciar = font.render("'r' para reiniciar", True, 'black')
    textSalir = font.render("'q' para salir", True, 'black')
    # text_rect = text.get_rect(center=button.center)
    pause.blit(textVolver, (width*0.7, height*0.9))
    pause.blit(textReiniciar, (width*0.7, height*1.1))
    pause.blit(textSalir, (width*0.7, height*1.3))
    return buttonVolver
