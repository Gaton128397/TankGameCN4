import pygame
import sys
import button

def run_settings():
    pygame.init()

    x = 100
    width, height = 16*x, 9*x
    screen = pygame.display.set_mode((width, height))

    settings_background = pygame.image.load('settings.png')  
    settings_background = pygame.transform.scale(settings_background, (width, height))
    screen.blit(settings_background, (0, 0))

    clock = pygame.time.Clock()

    home_button = button.Button((x*0.5 - 10, x*0.5 - 20, 100, 100), (255, 0, 0), 'Home', False)
    settings_button = button.Button((width - x*1.5 +15, x*0.5 - 25, 100, 100), (255, 0, 0), 'Settings', False)
    mas_player_button = button.Button((width // 2 + 510, height // 2 - 120, 100, 75), (0, 255, 0), 'MasPlayer', False)
    menos_player_button = button.Button((width // 2 + 210, height // 2 - 120, 100, 75), (0, 255, 0), 'MenosPlayer', False)

    mas_ronda_button = button.Button((width // 2 + 510, height // 2 + 275, 100, 75), (0, 255, 0), 'MasRonda', False)
    menos_ronda_button = button.Button((width // 2 + 210, height // 2 + 275, 100, 75), (0, 255, 0), 'MenosRonda', False)


    buttons = [home_button, settings_button, mas_player_button, menos_player_button, mas_ronda_button, menos_ronda_button]

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
                    print('boton config')
                    pygame.quit()
                    sys.exit()
                elif btn.item == 'MasPlayer':
                    print('Aumentar cantidad de jugadores')
                elif btn.item == 'MenosPlayer':
                    print('Reducir de selección de jugadores')
                elif btn.item == 'MasRonda':
                    print('Aumentar número de rondas')
                elif btn.item == 'MenosRonda':
                    print('Reducir número de rondas')
                    

        # Dibuja un cuadrado alrededor de cada botón
        square_color = (100, 100, 100)  
        for btn in buttons:
            pygame.draw.rect(screen, square_color, btn.rect, 2) 

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_settings()
