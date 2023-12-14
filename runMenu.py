import pygame,sys,button,params


    
    
def runMenu():
    pygame.init()
    clock = pygame.time.Clock()
    while True:
        loadScreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_f:
                    if params.size != 120:
                        params.size = 120
                    else:
                        params.size = 80
            for btn in buttons():
                if btn.check_click(event):
                    if btn.item == 'Play': #start choosing who to play against
                        return 1
                    elif btn.item == 'Settings':
                        return 2
                    elif btn.item == 'Controls':
                        return 7
                        # params.size +=5
                        # return 7
                    elif btn.item == 'Exit':
                        pygame.quit()
                        running =  False
                        sys.exit()
                        
            
            pygame.display.flip()
        clock.tick(60)

def buttons():
    width,height =params.size*16,params.size*9
    play_button = button.Button((params.size*2, height // 2 - params.size*0.45, params.size*4, params.size*0.75 + params.size*0.2), (0, 255, 0), 'Play', False)
    settings_button = button.Button((params.size, height - params.size*1.25, params.size*4 + params.size*0.1, params.size*0.75), (255, 0, 0), 'Settings', False)
    controls_button = button.Button((params.size*5 + params.size*0.75, params.size*6 + params.size*1.75, params.size*3, params.size*0.75), (0, 0, 255), 'Controls', False)
    exit_button = button.Button((width - params.size*3.5, height - params.size*1.25, params.size*3, params.size*0.75), (255, 255, 0), 'Exit', False)

    return [play_button, settings_button, controls_button, exit_button]

def loadScreen():
    if params.size == 120:
        screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    else:
        screen = pygame.display.set_mode((params.size*16, params.size*9))
    screen.blit(pygame.transform.scale(params.menuImg, (params.size*16,params.size*9)), (0, 0))
    pygame.display.flip()

# if __name__ == '__main__':
    # runMenu()