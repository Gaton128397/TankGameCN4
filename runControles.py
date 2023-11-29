import pygame
import sys
import button

def run_settings():
    pygame.init()

    x = 100
    width, height = 16*x, 9*x
    screen = pygame.display.set_mode((width, height))

    settings_background = pygame.image.load('imgs/controles.png')  
    settings_background = pygame.transform.scale(settings_background, (width, height))
    screen.blit(settings_background, (0, 0))

    clock = pygame.time.Clock()

    home_button = button.Button((x*0.5 - 10, x*0.5 - 20, 100, 100), (255, 0, 0), 'Home', False)

    buttons = [home_button]

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

        # Dibuja un cuadrado alrededor de cada botón
        square_color = (100, 100, 100)  
        for btn in buttons:
            pygame.draw.rect(screen, square_color, btn.rect, 2) 

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_settings()
