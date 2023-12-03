import pygame
import sys
import button,params

def run_maps():
    pygame.init()

    x = 100
    width, height = 16*x, 9*x
    screen = pygame.display.set_mode((width, height))

    maps_background = params.bgMapas
    screen.blit(maps_background, (0, 0))

    clock = pygame.time.Clock()

    home_button = button.Button((x*0.5 - 10, x*0.5 - params.size*0.2, 100, 100), (255, 0, 0), 'Home', False)
    settings_button = button.Button((width - x*1.5 + params.size*0.15, x*0.5 - params.size*0.25, 100, 100), (255, 0, 0), 'Settings', False)
    confirmar_button = button.Button((width - params.size*3, height - params.size*1, 250, 80), (0, 255, 0), 'Confirmar', False)



    random_map_button = button.Button((width // 2 - params.size*6.15, height // 2 - params.size*1.85, 300, 175), (0, 255, 0), 'Random Map', False)
    selva_button = button.Button((width // 2 - params.size*2.35, height // 2 - params.size*1.85, 300, 175), (0, 255, 0), 'Selva', False)
    galaxy_button = button.Button((width // 2 + params.size*1.55, height // 2 - params.size*1.85, 300, 175), (0, 255, 0), 'Galaxy', False)

    nieve_button = button.Button((width // 2 - params.size*6.15, height // 2 + params.size*1.25, 300, 175), (0, 255, 0), 'Nieve', False)
    desierto_button = button.Button((width // 2 - params.size*2.4, height // 2 + params.size*1.25, 300, 175), (0, 255, 0), 'Desierto', False)
    ciudad_button = button.Button((width // 2 + params.size*1.6, height // 2 + params.size*1.25, 300, 175), (0, 255, 0), 'Ciudad', False)

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

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_maps()
