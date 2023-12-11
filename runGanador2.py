import pygame
import sys
import button,params


def runGanador2(): #es cuando una ronda acaba
    pygame.init()
    clock = pygame.time.Clock()

    
    while True:
        loadScreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for btn in createButtons():
                if btn.check_click(event):
                    if btn.item == 'Home':
                        return 0
                    elif btn.item == 'Settings':
                        return 3
                    elif btn.item == 'Siguiente Ronda':
                        return 'siguiente ronda' #ver esto con gaston
                    elif btn.item == 'Terminar Juego':
                        pygame.quit()
                        sys.exit()

            clock.tick(60)

def createButtons():
    width, height = params.size*16, params.size*9
    home_button = button.Button((params.size*0.4,params.size*0.3, params.size, params.size), (255, 0, 0), 'Home', False)
    settings_button = button.Button((params.size*14.35, params.size*0.25, params.size, params.size), (255, 0, 0), 'Settings', False)
    siguiente_ronda_button = button.Button((params.size*7.25,params.size*7.75,params.size*4.5, params.size*0.75), (0, 255, 0), 'Siguiente Ronda', False)
    terminar_juego_button = button.Button((width - params.size*3.5 + params.size*0.15, height - params.size*1.25, params.size*3, params.size*0.75), (255, 255, 0), 'Terminar Juego', False)

    return [home_button, settings_button, siguiente_ronda_button, terminar_juego_button]

def loadScreen():
    if params.size == 120:
        params.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    else:
        params.screen = pygame.display.set_mode((params.size*16, params.size*9))
    params.screen.blit(pygame.transform.scale(params.bGanador2, (params.size*16, params.size*9)), (0, 0))    
    pygame.display.flip()
# if __name__ == '__main__':
    # runGanador2()