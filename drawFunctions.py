import pygame, params
def backgroundDraw(screen):
    backGr = pygame.image.load(params.BackGroundIMG)
    backGr = pygame.transform.scale(backGr,(params.WIDTH,params.HEIGHT))
    screen.blit(backGr,(0,0))