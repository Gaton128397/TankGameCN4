import pygame
import sys
import button,params

def run_ganador1():
    pygame.init()

    x = 100
    width, height = 16*x, 9*x
    screen = pygame.display.set_mode((width, height))

    ganador1_background = pygame.image.load('imgs/ganador2.png')  
    ganador1_background = pygame.transform.scale(ganador1_background, (width, height))
    screen.blit(ganador1_background, (0, 0))

    clock = pygame.time.Clock()

    home_button = button.Button((x*0.5 - params.size*0.1, x*0.5 - params.size*0.20, 100, 100), (255, 0, 0), 'Home', False)
    settings_button = button.Button((width - x*1.5 + params.size*0.15, x*0.5 - params.size*0.25, 100, 100), (255, 0, 0), 'Settings', False)
    siguiente_ronda_button = button.Button((width // 2 - x*1.5 - params.size*0.75 , x*6 + params.size*1.75, x*3 + params.size*1.5, x*0.75), (0, 255, 0), 'Siguiente Ronda', False)
    terminar_juego_button = button.Button((width - x*3.5 + params.size*0.15, height - x*1.25, x*3, x*0.75), (255, 255, 0), 'Terminar Juego', False)

    buttons = [home_button, settings_button, siguiente_ronda_button, terminar_juego_button]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for btn in buttons:
            if btn.check_click(event):
                if btn.item == 'Home':
                    print('pantalla de inicio')
                elif btn.item == 'Settings':
                    print('configuración')
                elif btn.item == 'Siguiente Ronda':
                    print('siguiente ronda')
                elif btn.item == 'Terminar Juego':
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_ganador1()
