import pygame
import sys
import button,params

def run_pausa():
    pygame.init()

    x = 100
    width, height = 16*x, 9*x
    screen = pygame.display.set_mode((width, height))

    pausa_background = pygame.image.load('imgs/pausa.png')  
    pausa_background = pygame.transform.scale(pausa_background, (width, height))
    screen.blit(pausa_background, (0, 0))

    clock = pygame.time.Clock()

    home_button = button.Button((width // 2 - (x*4 + params.size*0.1) // 2, height // 2 - x*0.45 - params.size*1, x*4 + params.size*0.1, x*0.75), (255, 0, 0), 'Home', False)
    settings_button = button.Button((width // 2 - (x*4 + params.size*0.1) // 2, height // 2 - x*0.45 , x*4 + params.size*0.1, x*0.75), (255, 0, 0), 'Settings', False)
    controls_button = button.Button((width // 2 - (x*4 + params.size*0.1) // 2, height // 2 + params.size*1, x*4 + params.size*0.1, x*0.75), (0, 0, 255), 'Controls', False)
    exit_button = button.Button((width // 2 - x*1.5, height - x*1.25, x*3, x*0.75), (255, 255, 0), 'Exit', False)

    buttons = [home_button, settings_button, controls_button, exit_button]

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
                elif btn.item == 'Controls':
                    print('controles')
                elif btn.item == 'Exit':
                    pygame.quit()
                    sys.exit()

        # Dibuja un cuadrado alrededor de cada botón
        square_color = (100, 100, 100)  
        for btn in buttons:
            pygame.draw.rect(screen, square_color, btn.rect, 2) 

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_pausa()
