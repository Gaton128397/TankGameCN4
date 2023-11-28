import pygame
import sys
import button

def run_ganador1():
    pygame.init()

    x = 100
    width, height = 16*x, 9*x
    screen = pygame.display.set_mode((width, height))

    ganador1_background = pygame.image.load('ganador2.png')  
    ganador1_background = pygame.transform.scale(ganador1_background, (width, height))
    screen.blit(ganador1_background, (0, 0))

    clock = pygame.time.Clock()

    home_button = button.Button((x*0.5 - 10, x*0.5 - 20, 100, 100), (255, 0, 0), 'Home', False)
    settings_button = button.Button((width - x*1.5 +15, x*0.5 - 25, 100, 100), (255, 0, 0), 'Settings', False)
    siguiente_ronda_button = button.Button((width // 2 - x*1.5 - 75, x*6 + 175, x*3 + 150, x*0.75), (0, 255, 0), 'Siguiente Ronda', False)
    terminar_juego_button = button.Button((width - x*3.5 + 15, height - x*1.25, x*3, x*0.75), (255, 255, 0), 'Terminar Juego', False)

    buttons = [home_button, settings_button, siguiente_ronda_button, terminar_juego_button]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for btn in buttons:
            if btn.check_click(event):
                if btn.item == 'Home':
                    print('Ir a la pantalla de inicio')
                elif btn.item == 'Settings':
                    print('Ir a la configuración')
                elif btn.item == 'Siguiente Ronda':
                    print('Ir a la siguiente ronda')
                elif btn.item == 'Terminar Juego':
                    pygame.quit()
                    sys.exit()

        # Dibuja un cuadrado alrededor de cada botón
        square_color = (100, 100, 100)  
        for btn in buttons:
            pygame.draw.rect(screen, square_color, btn.rect, 2) 

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_ganador1()
