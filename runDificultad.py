import pygame
import sys
import button,params

def run_dificultad():
    pygame.init()

    x = 100
    width, height = params.WIDTH, params.HEIGHT
    screen = pygame.display.set_mode((width, height))

    dificultad_background = pygame.image.load('imgs/dificultad.png')  
    dificultad_background = pygame.transform.scale(dificultad_background, (width, height))
    screen.blit(dificultad_background, (0, 0))

    clock = pygame.time.Clock()

    home_button = button.Button((x*0.5 - params.size*0.1, x*0.5 - params.size*0.2, 100, 100), (255, 0, 0), 'Home', False)
    confirmar_button = button.Button((width - x*3.5 - params.size*0.2, height - x*1.25 - params.size*0.5, x*3, x*0.75), (255, 255, 0), 'Confirmar', False)
    facil_button = button.Button((width // 2 + x*0.5 - params.size*2.9, height // 2 + params.size*0.3, 120, 80), (0, 255, 0), 'Fácil', False)
    normal_button = button.Button((width // 2 + x*0.5 - params.size*1, height // 2 + params.size*0.3, 120, 80), (0, 255, 0), 'Normal', False)
    dificil_button = button.Button((width // 2 + x*0.5 + params.size*0.85, height // 2 + params.size*0.3, 120, 80), (0, 255, 0), 'Difícil', False)

    buttons = [home_button, confirmar_button, facil_button, normal_button, dificil_button]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for btn in buttons:
            if btn.check_click(event):
                if btn.item == 'Home':
                    print('Pantalla de inicio')
                elif btn.item == 'Confirmar':
                    print('Cerrar juego')
                    pygame.quit()
                    sys.exit()
                elif btn.item == 'Fácil':
                    print('Fácil')
                elif btn.item == 'Normal':
                    print('Normal')
                elif btn.item == 'Difícil':
                    print('Difícil')

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_dificultad()
