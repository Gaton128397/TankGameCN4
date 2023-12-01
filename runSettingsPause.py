import pygame
import sys
import button,params

def run_settings():
    pygame.init()

    x = 100
    width, height = params.WIDTH, params.HEIGHT
    screen = pygame.display.set_mode((width, height))

    settings_background = pygame.image.load('imgs/settingspause.png')  
    settings_background = pygame.transform.scale(settings_background, (width, height))
    screen.blit(settings_background, (0, 0))

    clock = pygame.time.Clock()

    home_button = button.Button((x*0.5 - params.size*0.1, x*0.5 - params.size*0.2, 100, 100), (255, 0, 0), 'Home', False)
    confirmar_button = button.Button((width - x*1.5 - params.size*2.5, x*0.5 + params.size*6.5, 300, 100), (255, 0, 0), 'Settings', False)

    buttons = [home_button, confirmar_button]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for btn in buttons:
            if btn.check_click(event):
                if btn.item == 'Home':
                    print('boton home')
                    pygame.quit()
                    sys.exit()
                elif btn.item == 'Settings':
                    print('confirmar')
                    pygame.quit()
                    sys.exit()                    

        # Dibuja un cuadrado alrededor de cada botón
        square_color = (100, 100, 100)  
        for btn in buttons:
            pygame.draw.rect(screen, square_color, btn.rect, 2) 

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_settings()
