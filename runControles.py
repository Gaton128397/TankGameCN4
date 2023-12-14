import pygame
import sys
import button,params


def runControles():
    pygame.init()
    clock = pygame.time.Clock()
    while True:
        loadScreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    return 6 #volver a pausa 
            for btn in buttons():
                if btn.check_click(event):
                    if btn.item == 'Home':
                        return 0              
            pygame.display.flip()
            clock.tick(60)
def buttons():
    home_button = button.Button((params.size*0.3, params.size*0.1, params.size, params.size), (255, 0, 0), 'Home', False)
    return [home_button]

def loadScreen():
    screen = pygame.display.set_mode((params.size*16, params.size*9))
    screen.blit(pygame.transform.scale(params.controlesImg, (params.size*16,params.size*9)), (0, 0))
    pygame.display.flip()

    
if __name__ == '__main__':
    runControles()