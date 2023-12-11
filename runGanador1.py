import pygame,sys,button,params


def runGanador1(): #ganador 1 es cuando la partida acaba
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
                        print('Ir a la pantalla de inicio')
                        # return 0
                    elif btn.item == 'Settings':
                        print('Ir a la configuración')
                        # return 3
                    elif btn.item == 'Iniciar Partida':
                        print('Iniciar partida') #boton reinciar partida
                        # return 'reiniciar partida' #revisar esto con gaston por el flujo
                    elif btn.item == 'Terminar Juego':
                        print('Terminar juego')
                        pygame.quit()
                        sys.exit()
            clock.tick(60)

def createButtons():
    home_button = button.Button((params.size*0.4, params.size*0.3, params.size, params.size), (255, 0, 0), 'Home', False)
    settings_button = button.Button((params.size*14.35,params.size*0.25, params.size, params.size), (255, 0, 0), 'Settings', False)
    iniciar_partida_button = button.Button((params.size*0.25,params.size*7.75, params.size*3, params.size*0.75), (0, 255, 0), 'Iniciar Partida', False)
    terminar_juego_button = button.Button((params.size*12.5,params.size*7.75, params.size*3, params.size*0.75), (255, 255, 0), 'Terminar Juego', False)
    return [home_button, settings_button,iniciar_partida_button, terminar_juego_button]

def loadScreen():
    if params.size == 120:
        screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((params.size*16, params.size*9))
    screen.blit(pygame.transform.scale(params.bGganador1, (params.size*16, params.size*9)), (0, 0))    
    pygame.display.flip()

# if __name__ == '__main__':
#     runGanador1()