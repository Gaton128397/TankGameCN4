import pygame
import sys
import button

def run_play_mode():
    pygame.init()

    x = 100
    width, height = 16*x, 9*x
    screen = pygame.display.set_mode((width, height))

    play_mode_background = pygame.image.load('playmode.png')  
    play_mode_background = pygame.transform.scale(play_mode_background, (width, height))
    screen.blit(play_mode_background, (0, 0))

    clock = pygame.time.Clock()

    friends_button = button.Button((x*2 + 100, height // 2 - x*0.45, x*3, x*0.75), (0, 255, 0), 'Amigos', False)
    cpu_button = button.Button((x*10 + 30, height // 2 - x*0.45, x*3, x*0.75), (0, 255, 0), 'CPU', False)
    confirm_button = button.Button((x*5 + 150, x*6 + 125, x*3, x*0.75), (0, 0, 255), 'Confirmar', False)


    buttons = [friends_button, cpu_button, confirm_button]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        for btn in buttons:
            if btn.check_click(event):
                if btn.item == 'Amigos':
                    print('Modo amigos')
                elif btn.item == 'CPU':
                    print('Modo CPU')
                elif btn.item == 'Confirmar':
                    print('Confirmar')
                    pygame.quit()
                    sys.exit()

        # Dibuja un cuadrado alrededor de cada botón
        square_color = (100, 100, 100)  
        for btn in buttons:
            pygame.draw.rect(screen, square_color, btn.rect, 2)  

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    run_play_mode()
