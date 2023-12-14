import pygame,sys, button,params

def runPlaymode():
    pygame.init()
    clock = pygame.time.Clock()
    modo = 0

    while True:
        loadScreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for btn in buttons():
                if btn.check_click(event):
                    if btn.item == 'Amigos':
                        print('boton amigos')
                        modo = 'Amigos'
                    elif btn.item == 'CPU':
                        print('boton cpu')
                        modo = 'CPU'
                    elif btn.item == 'Confirmar':
                        print('boton confirmar')
                        print(modo)
                        return modo
            pygame.display.flip()
            clock.tick(60)

def buttons():
    x,width,height = params.size,params.size*16,params.size*9 

    friends_button = button.Button((x*2 + params.size, height // 2 - x*0.45, x*3, x*0.75), (0, 255, 0), 'Amigos', False)
    cpu_button = button.Button((x*10 + params.size*0.3, height // 2 - x*0.45, x*3, x*0.75), (0, 255, 0), 'CPU', False)
    confirm_button = button.Button((x*5 + params.size*1.5, x*6 + 125, x*3, x*0.75), (0, 0, 255), 'Confirmar', False)

    buttons = [friends_button, cpu_button, confirm_button]
    return buttons

def loadScreen():
    params.screen.blit(pygame.transform.scale(params.playModeImg, (params.size*16,params.size*9)), (0, 0))


#if __name__ == '__main__':
#    runPlaymode()


 #MARCADO PARA ARREGLAR BOTONES