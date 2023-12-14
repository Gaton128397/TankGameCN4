
import pygame,sys,button,params

def runPausa(): #lastScreen es la pantalla que se estaba ejecutando antes de pausa
    pygame.init()
    clock = pygame.time.Clock()
    loadScreen()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_ESCAPE:
                    return 5 #regresa a la pantalla que se estaba ejecutando antes de pausa
            for btn in buttons():
                if btn.check_click(event):
                    if btn.item == 'Home':
                        return 0
                    elif btn.item == 'Settings':
                        return 3
                    elif btn.item == 'Controls':
                        return 7
                    elif btn.item == 'Exit':
                        pygame.quit()
                        running = False
                        sys.exit()
        
            pygame.display.flip()
            clock.tick(60)
            
def buttons():
    x,width,height = params.size,params.size*16,params.size*9
    
    home_button = button.Button((width // 2 - (params.size*4 + params.size*0.1) // 2, height // 2 - params.size*0.45 - params.size, params.size*4 + params.size*0.1, params.size*0.75), (255, 0, 0), 'Home', False)
    settings_button = button.Button((width // 2 - (params.size*4 + params.size*0.1) // 2, height // 2 - params.size*0.45 , params.size*4 + params.size*0.1, params.size*0.75), (255, 0, 0), 'Settings', False)
    controls_button = button.Button((width // 2 - (params.size*4 + params.size*0.1) // 2, height // 2 + params.size, params.size*4 + params.size*0.1, params.size*0.75), (0, 0, 255), 'Controls', False)
    exit_button = button.Button((width // 2 - params.size*1.5, height - params.size*1.25, params.size*3, params.size*0.75), (255, 255, 0), 'Exit', False)

    return [home_button, settings_button, controls_button, exit_button]

def loadScreen():
    if params.size == 120:
        params.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    else:
        params.screen = pygame.display.set_mode((params.size*16, params.size*9))
    params.screen.blit(pygame.transform.scale(params.pausaImg, (params.size*16,params.size*9)), (0, 0))
    pygame.display.flip()


# if __name__ == '__main__':
    # runPausa()


 #MARCADO PARA ARREGLAR BOTONES

