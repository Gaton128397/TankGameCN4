import pygame, params

def backgroundDraw(screen,ruta):
    WIDTH = params.size*16
    HEIGHT = params.size*9
    print(ruta)
    backGr = pygame.image.load(ruta)
    # print(backGr)
    backGr = pygame.transform.scale(backGr,(WIDTH,HEIGHT))
    screen.blit(backGr,(0,0))
    
def cargarImagen(surf, imagen, proporcionX, proporcionY, posicion):
    imagen_cargada = pygame.image.load(imagen)
    imagen_escalada = pygame.transform.scale(imagen_cargada, (surf.get_width()*proporcionX, surf.get_height()*proporcionY))
    surf.blit(imagen_escalada, (int(surf.get_width() *posicion[0]),int(surf.get_height() *posicion[1])))
        
        
def returnSurface(matriz):
    WIDTH = params.size*16
    HEIGHT = params.size*9
    surface = pygame.Surface((WIDTH, HEIGHT))
    for i in range(len(matriz)):
        if i < len(matriz) - 1:
            surface.blit(matriz[i],(0,0))
        else:
            surface.blit(matriz[i],(0,0))
    
    return surface

def blitIndicador(screen,indicador,tLetra):
    screen.fill((255,255,255))
    texto = str(indicador)
    fuente = pygame.font.Font(None, int(screen.get_width() *tLetra))
    superficie_texto = fuente.render(texto, True, (0, 0, 0))
    screen.blit(superficie_texto, (int(screen.get_width() *0.2), int(screen.get_height() *0.07)))