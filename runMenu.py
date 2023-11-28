import pygame
import sys
import button

def run_menu():
    pygame.init()

    x = 100
    width, height = 16*x, 9*x
    screen = pygame.display.set_mode((width, height))

    menu_background = pygame.image.load('imgs/Menu.png')  
    menu_background = pygame.transform.scale(menu_background, (width, height))
    screen.blit(menu_background, (0, 0))

    clock = pygame.time.Clock()

    play_button = button.Button((x*2, height // 2 - x*0.45, x*4, x*0.75 + 20), (0, 255, 0), 'Play', False)
    settings_button = button.Button((x, height - x*1.25, x*4 + 10, x*0.75), (255, 0, 0), 'Settings', False)
    controls_button = button.Button((x*5 + 75, x*6 + 175, x*3, x*0.75), (0, 0, 255), 'Controls', False)
    exit_button = button.Button((width - x*3.5, height - x*1.25, x*3, x*0.75), (255, 255, 0), 'Exit', False)

    buttons = [play_button, settings_button, controls_button, exit_button]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for btn in buttons:
            if btn.check_click(event):
                if btn.item == 'Play':
                    print('jugar')
                elif btn.item == 'Settings':
                    print('opciones')
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
    run_menu()

