import pygame,sys,button,params
def borrarNumero(surfaceNumero):
    surfaceNumero.fill((255,0,255))

def actualizarNumero(surfaceNumero,pos,jugador):
    borrarNumero(surfaceNumero)
    texto = str(jugador) 
    fuente = pygame.font.Font(None, int(surfaceNumero.get_width() *0.5))
    superficie_texto = fuente.render(texto, True, (0, 0, 0))
    surfaceNumero.blit(superficie_texto, (0,0))

def runSettings():
    pygame.init()
    clock = pygame.time.Clock()
    proporcion  = 0.1
    surfaceNumeroJugadores = pygame.Surface((params.size*16*proporcion, params.size*9*proporcion))
    alphaColor = (255,0,255)
    surfaceNumeroJugadores.set_alpha()
    surfaceNumeroJugadores.set_colorkey(alphaColor)
    surfaceNumero = pygame.Surface((params.size*16*proporcion, params.size*9*proporcion))
    surfaceNumero.set_alpha()
    surfaceNumero.set_colorkey(alphaColor)

    jugadores = 2
    rondas = 1
    actualizarNumero(surfaceNumeroJugadores,(0, 0),jugadores)
    actualizarNumero(surfaceNumero,(0, 0),rondas)
    #screen = pygame.display.set_mode((params.size*16, params.size*9))
    while True:
        params.screen.blit(pygame.transform.scale(params.settingsImg, (params.size*16,params.size*9)), (0, 0))
        params.screen.blit(surfaceNumeroJugadores,(params.size*16*0.74, params.size*9*0.38))
        params.screen.blit(surfaceNumero,(params.size*16*0.74, params.size*9*0.82))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_f:
                    if params.size == 120:
                        params.size=80
                    else:
                        params.size=120
            for btn in buttons():
                if btn.check_click(event):
                    if btn.item == 'Home':
                        print('boton home')
                        return [0,2,1]#vuelve al menu con las configuraciones por defecto
                    elif btn.item == 'Confirmar':
                        return [3,jugadores,rondas]

                    elif btn.item == 'MasPlayer':
                        if jugadores < 6 and jugadores >= 0:
                            params.playersNumber += 1
                            actualizarNumero(surfaceNumeroJugadores,(0, 0),params.playersNumber)
                            #deberia blitear en pantalla el numero de jugadores

                    elif btn.item == 'MenosPlayer':
                        if jugadores > 2 and jugadores <= 6:
                            params.playersNumber -= 1
                            actualizarNumero(surfaceNumeroJugadores,(params.size*16*0.5, params.size*9*0.5),params.playersNumber)
                            #deberia blitear en pantalla el numero de jugadores
                    elif btn.item == 'MasRonda':
                        if rondas < 5 and rondas >= 0:
                            rondas += 1
                            actualizarNumero(surfaceNumero,(0, 0),rondas)
                            print(rondas)
                            #deberia blitear en pantalla el numero de rondas
                    elif btn.item == 'MenosRonda':
                        if rondas > 1 and rondas <= 5:
                            rondas -= 1
                            actualizarNumero(surfaceNumero,(0, 0),rondas)
                            print(rondas)
                            #deberia blitear en pantalla el numero de ronda
                    elif btn.item == 'IncreaseSize':
                        if params.size < 120:
                            params.size +=5
                            params.screen = pygame.display.set_mode((params.size*16, params.size*9))
                    elif btn.item == 'DecreaseSize':
                        if params.size > 25:
                            params.size -=5
                            params.screen = pygame.display.set_mode((params.size*16, params.size*9))
            pygame.display.flip()

def buttons():
    x,width,height = params.size,params.size*16,params.size*9 

    home_button = button.Button((params.size*0.4,params.size*0.3,params.size,params.size*0.8), (255, 0, 0), 'Home', False)
    confirmar_button = button.Button((width - x*1.5 - params.size*2.5, x*0.5 - params.size*0.25, params.size*3, params.size), (255, 0, 0), 'Confirmar', False)
    mas_player_button = button.Button((width // 2 + params.size*5.1, height // 2 - params.size*1.2, params.size, params.size*0.75), (0, 255, 0), 'MasPlayer', False)
    menos_player_button = button.Button((width // 2 + params.size*2.1, height // 2 - params.size*1.2, params.size, params.size*0.75), (0, 255, 0), 'MenosPlayer', False)
    mas_ronda_button = button.Button((width // 2 + params.size*5.1, height // 2 + params.size*2.75, params.size, params.size*0.75), (0, 255, 0), 'MasRonda', False)
    menos_ronda_button = button.Button((width // 2 + params.size*2.1, height // 2 + params.size*2.75, params.size, params.size*0.75), (0, 255, 0), 'MenosRonda', False)
    increase_size_button = button.Button((params.size*2.8, params.size*3.2, params.size, params.size*0.75), (0, 255, 0), 'IncreaseSize', False)
    decrease_size_button = button.Button((params.size*0.9, params.size*3.2, params.size, params.size*0.75), (0, 255, 0), 'DecreaseSize', False)

    buttons = [home_button, confirmar_button, mas_player_button, menos_player_button, mas_ronda_button, menos_ronda_button, increase_size_button, decrease_size_button]
    return buttons


<<<<<<< HEAD
#if __name__ == '__main__':
    #runSettings()


 #MARCADO PARA ARREGLAR BOTONES
=======
if __name__ == '__main__':
    runSettings()
>>>>>>> origin/Maru
