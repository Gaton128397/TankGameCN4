import pygame,sys
pygame.init()
WIDTH = 1300
HEIGHT = 700
def draw_menu(surfaceMenu,width,height):

    #variables
    small_font1 = pygame.font.Font(None, 50)
    font1 = pygame.font.Font(None, 150) 
    ARENA_COLOR = (255, 204, 153)
    CACTUS_GREEN = (85, 107, 47)
    buttonPlay = pygame.Rect(500, 305, 250, 75)
    buttonControls = pygame.Rect(500, 405, 250, 75)
    buttonExit = pygame.Rect(975, 585, 250, 75)
    
    listaBotones = [buttonPlay,buttonControls,buttonExit]

    #dibuja bg
    background = pygame.image.load("Background.jpg")
    background = pygame.transform.scale(background, (width,height))
    surfaceMenu.blit(background, (0, 0))
    
    #titulo
    text = font1.render("Canyon-4", True, CACTUS_GREEN) 
    text_rect = text.get_rect(center=(width//2, 200))
    surfaceMenu.blit(text, text_rect)

    #botón "Jugar"
    pygame.draw.rect(surfaceMenu, ARENA_COLOR, buttonPlay)
    text = small_font1.render("Jugar", True, 'white')
    text_rect = text.get_rect(center=buttonPlay.center)
    surfaceMenu.blit(text, text_rect)

    #botón "controles"
    pygame.draw.rect(surfaceMenu, ARENA_COLOR, buttonControls)
    text = small_font1.render("Controles", True, 'white')
    text_rect = text.get_rect(center=buttonControls.center)
    surfaceMenu.blit(text, text_rect)

    #botón "Salir"
    pygame.draw.rect(surfaceMenu, ARENA_COLOR, buttonExit)
    text = small_font1.render("Salir", True, 'white')
    text_rect = text.get_rect(center=buttonExit.center)
    surfaceMenu.blit(text, text_rect)

    return listaBotones