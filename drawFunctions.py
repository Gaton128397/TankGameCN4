import pygame, params
def backgroundDraw(screen):
    backGr = pygame.image.load(params.BackGroundIMG)
    backGr = pygame.transform.scale(backGr,(params.WIDTH,params.HEIGHT))
    screen.blit(backGr,(0,0))
    
def cargarImagen(surf, imagen, proporcionX, proporcionY, posicion):
        imagen_cargada = pygame.image.load(imagen)
        imagen_escalada = pygame.transform.scale(imagen_cargada, (surf.get_width()*proporcionX, surf.get_height()*proporcionY))
        surf.blit(imagen_escalada, (int(surf.get_width() *posicion[0]),int(surf.get_height() *posicion[1])))