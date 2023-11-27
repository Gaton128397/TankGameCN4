import pygame,time
def drawEnd(endSurface,width,height,event):
    time.sleep(0.2)
    ARENA_COLOR = (244, 164, 96)

    buttonRePlay = pygame.Rect(550, 520, 200, 50) 

    font = pygame.font.Font(None, 36)
    big_font = pygame.font.Font(None, 72)
    endSurface.fill('gold')
    if event == 0:
        textoEnd = big_font.render("Time over", True, 'black')
        endSurface.blit(textoEnd, (width//2-120, height//2))
    else:
        textoEnd = big_font.render("Gana Jugador "+str(event), True, 'black')
        endSurface.blit(textoEnd, (width//2-200, height//2))
    
    # Dibujar el botón "Volver a jugar"
    pygame.draw.rect(endSurface, ARENA_COLOR, buttonRePlay)  
    text = font.render("Volver a jugar", True, 'white')
    text_rect = text.get_rect(center=buttonRePlay.center)
    endSurface.blit(text, text_rect)
    return buttonRePlay
