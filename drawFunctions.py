import pygame, params
def backgroundDraw(screen):
    backGr = params.mapaDesert
    backGr = pygame.transform.scale(backGr,(params.WIDTH,params.HEIGHT))
    screen.blit(backGr,(0,0))
    
def cargarImagen(surf, imagen, proporcionX, proporcionY, posicion):
    imagen_cargada = imagen
    imagen_escalada = pygame.transform.scale(imagen_cargada, (surf.get_width()*proporcionX, surf.get_height()*proporcionY))
    surf.blit(imagen_escalada, (int(surf.get_width() *posicion[0]),int(surf.get_height() *posicion[1])))
        
        
def returnSurface(matriz):
    surface = pygame.Surface((params.WIDTH, params.HEIGHT))
    for i in range(len(matriz)):
        if i < len(matriz) - 1:
            surface.blit(matriz[i],(0,0))
        else:
            surface.blit(matriz[i],(0,0))
    
    return surface