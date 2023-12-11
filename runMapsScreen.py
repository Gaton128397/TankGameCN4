import pygame,sys,button,params,random,createMap


def runMaps():
    pygame.init()
    clock = pygame.time.Clock()
    mapa = None

    while True:
        loadScreen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            for btn in createButtons():
                if btn.check_click(event):
                    if btn.item == 'Home':
                        return [0,None]
                    elif btn.item == 'Settings':
                        return [2,None]
                    elif btn.item == 'Confirmar':
                        return [4,mapa]
                    else:
                        print(btn.item.ID)
                        mapa = btn.item #retorna el mapa seleccionado
        pygame.display.flip()
        clock.tick(60)

def createMaps():

    desierto = createMap.Map(0,params.mapaDesert, 9.8, random.randint(-1,1)*2, 'yellow') #gravedad = 0 y viento = 0
    selva = createMap.Map(1,params.mapaSelva, 9.8, random.randint(-1,1)*4, 'green')
    nieve = createMap.Map(2,params.mapaSnow, 9.8, random.randint(-1,1)*8, 'white')
    galaxia = createMap.Map(3,params.mapaGalaxia, 5.2, 0, 'purple')
    ciudad = createMap.Map(4,params.mapaCiudad, 9.8, random.randint(-1,1)*6, 'grey')
    return [selva, galaxia,nieve,desierto,ciudad]

def createButtons():
    width,height =params.size*16,params.size*9

    mapas = createMaps()

    home_button = button.Button((params.size*0.5 - params.size*0.1, params.size*0.5 - params.size*0.2, 100, 100), (255, 0, 0), 'Home', False)
    settings_button = button.Button((width - params.size*1.5 + params.size*0.15, params.size*0.5 - params.size*0.25, 100, 100), (255, 0, 0), 'Settings', False)
    confirmar_button = button.Button((width - params.size*3, height - params.size*1, 250, 80), (0, 255, 0), 'Confirmar', False)
    random_map_button = button.Button((width // 2 - params.size*6.15, height // 2 - params.size*1.85, params.size*3, params.size*1.75), (0, 255, 0), mapas[random.randint(0,4)], False)
    selva_button = button.Button((width // 2 - params.size*2.35, height // 2 - params.size*1.85, params.size*3, params.size*1.75), (0, 255, 0), mapas[0], False)
    galaxy_button = button.Button((width // 2 + params.size*1.55, height // 2 - params.size*1.85, params.size*3, params.size*1.75), (0, 255, 0), mapas[1], False)

    nieve_button = button.Button((width // 2 - params.size*6.15, height // 2 + params.size*1.25, params.size*3, params.size*1.75), (0, 255, 0), mapas[2], False)
    desierto_button = button.Button((width // 2 - params.size*2.4, height // 2 + params.size*1.25, params.size*3, params.size*1.75), (0, 255, 0), mapas[3], False)
    ciudad_button = button.Button((width // 2 + params.size*1.6, height // 2 + params.size*1.25, params.size*3, params.size*1.75), (0, 255, 0), mapas[4], False)

    return [home_button, settings_button, confirmar_button,
            random_map_button, selva_button, galaxy_button,
            nieve_button, desierto_button, ciudad_button]
    
def loadScreen():
    #if params.size == 120:
    #    params.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    #else:
    #    params.screen = pygame.display.set_mode((params.size*16, params.size*9))
    params.screen.blit(pygame.transform.scale(params.bgMapas, (params.size*16, params.size*9)), (0, 0))    
    #pygame.display.flip()

# if __name__ == '__main__':
    # runMaps()