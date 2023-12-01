import pygame
import sys
import button

def run_maps():
    pygame.init()

    x = 100
    width, height = 16*x, 9*x
    screen = pygame.display.set_mode((width, height))

    maps_background = pygame.image.load('imgs/mapas.png')  
    maps_background = pygame.transform.scale(maps_background, (width, height))
    screen.blit(maps_background, (0, 0))

    clock = pygame.time.Clock()

    home_button = button.Button((x*0.5 - 10, x*0.5 - 20, 100, 100), (255, 0, 0), 'Home', False)
    settings_button = button.Button((width - x*1.5 + 15, x*0.5 - 25, 100, 100), (255, 0, 0), 'Settings', False)
    confirmar_button = button.Button((width // 2 - 150, height // 2 - 50, 300, 100), (0, 255, 0), 'Confirmar', False)

    random_map_button = button.Button((width // 2 - 100, height // 2 - 200, 200, 200), (0, 255, 0), 'Random Map', False)
    selva_button = button.Button((width // 2 - 300, height // 2 - 100, 200, 200), (0, 255, 0), 'Selva', False)
    galaxy_button = button.Button((width // 2 - 100, height // 2 - 100, 200, 200), (0, 255, 0), 'Galaxy', False)
    nieve_button = button.Button((width // 2 + 100, height // 2 - 100, 200, 200), (0, 255, 0), 'Nieve', False)
    desierto_button = button.Button((width // 2 - 300, height // 2 + 100, 200, 200), (0, 255, 0), 'Desierto', False)
    ciudad_button = button.Button((width // 2 - 100, height // 2 + 100, 200, 200), (0, 255, 0), 'Ciudad', False)

    buttons = [home_button, settings_button, confirmar_button,
               random_map_button, selva_button, galaxy_button,
               nieve_button, desierto_button, ciudad_button]

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
                    elif btn.item == 'Confirmar':
                        print('Confirmar')
                    else:
                        print(f'Seleccionado: Mapa {btn.item}')

        # Dibuja un cuadrado alrededor de cada botón
        square_color = (100, 100, 100)  
        for btn in buttons:
            pygame.draw.rect(screen, square_color, btn.rect, 2) 

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_maps()
