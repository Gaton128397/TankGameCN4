import pygame
import sys
import button

def run_dificultad():
    pygame.init()

    x = 100
    width, height = 16*x, 9*x
    screen = pygame.display.set_mode((width, height))

    dificultad_background = pygame.image.load('imgs/dificultad.png')  
    dificultad_background = pygame.transform.scale(dificultad_background, (width, height))
    screen.blit(dificultad_background, (0, 0))

    clock = pygame.time.Clock()

    home_button = button.Button((x*0.5 - 10, x*0.5 - 20, 100, 100), (255, 0, 0), 'Home', False)
    confirmar_button = button.Button((width - x*3.5 - 20, height - x*1.25 - 50, x*3, x*0.75), (255, 255, 0), 'Confirmar', False)
    facil_button = button.Button((width // 2 + x*0.5 - 290, height // 2 + 30, 120, 80), (0, 255, 0), 'Fácil', False)
    normal_button = button.Button((width // 2 + x*0.5 - 100, height // 2 + 30, 120, 80), (0, 255, 0), 'Normal', False)
    dificil_button = button.Button((width // 2 + x*0.5 + 85, height // 2 + 30, 120, 80), (0, 255, 0), 'Difícil', False)





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

        # Dibuja un cuadrado alrededor de cada botón
        square_color = (100, 100, 100)  
        for btn in buttons:
            pygame.draw.rect(screen, square_color, btn.rect, 2) 

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_dificultad()
