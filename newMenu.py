import pygame,sys,params
pygame.init()
WIDTH = 1300
HEIGHT = 700
def draw_menu(surfaceMenu,width,height):

    #variables
    small_font1 = pygame.font.Font(None, 50)
    font1 = pygame.font.Font(None, 150) 
    ARENA_COLOR = (255, 204, 153)
    CACTUS_GREEN = (85, 107, 47)
    buttonPlay = pygame.Rect(width*0.25, 305, 650, 75)
    buttonControls = pygame.Rect(width*0.25, 405, 650, 75)
    buttonExit = pygame.Rect(width*0.25, 505, 650, 75)
    
    listaBotones = [buttonPlay,buttonControls,buttonExit]

    #dibuja bg
    background = pygame.image.load(params.BackGroundIMG)
    background = pygame.transform.scale(background, (width,height))
    surfaceMenu.blit(background, (0, 0))
    
    #titulo
    text = font1.render("Canyon-4", True, CACTUS_GREEN) 
    text_rect = text.get_rect(center=(width*0.5, 200))
    surfaceMenu.blit(text, text_rect)

    #botón "Jugar"
    pygame.draw.rect(surfaceMenu, ARENA_COLOR, buttonPlay)
    text = small_font1.render("Presione 'enter' para jugar", True, 'white')
    text_rect = text.get_rect(center=buttonPlay.center)
    surfaceMenu.blit(text, text_rect)

    #botón "controles"
    pygame.draw.rect(surfaceMenu, ARENA_COLOR, buttonControls)
    text = small_font1.render("Presione 'i' para ver las instrucciones", True, 'white')
    text_rect = text.get_rect(center=buttonControls.center)
    surfaceMenu.blit(text, text_rect)

    #botón "Salir"
    pygame.draw.rect(surfaceMenu, ARENA_COLOR, buttonExit)
    text = small_font1.render("Presione 'esc' para salir", True, 'white')
    text_rect = text.get_rect(center=buttonExit.center)
    surfaceMenu.blit(text, text_rect)

    return listaBotones