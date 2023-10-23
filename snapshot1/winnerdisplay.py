import pygame,time
def drawWinner(winnerSurface,width,height,winner):
    time.sleep(0.2)
    ARENA_COLOR = (244, 164, 96)

    buttonRePlay = pygame.Rect(550, 520, 200, 50) 

    font = pygame.font.Font(None, 36)
    big_font = pygame.font.Font(None, 72)
    winnerSurface.fill('gold')
    textoGanar = big_font.render("Gana Jugador "+str(winner), True, 'black')
    winnerSurface.blit(textoGanar, (width//2-200, height//2))
    
    # Dibujar el botón "Volver a jugar"
    pygame.draw.rect(winnerSurface, ARENA_COLOR, buttonRePlay)  
    text = font.render("Volver a jugar", True, 'white')
    text_rect = text.get_rect(center=buttonRePlay.center)
    winnerSurface   .blit(text, text_rect)