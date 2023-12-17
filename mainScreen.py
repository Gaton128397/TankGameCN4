import functions,proporciones
"""
Version final tankgame
CN4 Cannon-4 Game
"""
#pantalla en la cual inicia la ejecucion
pantalla = 4
while pantalla != -1:
    try:
        if pantalla != -1:
            pantalla = functions.run(proporciones.imgs[pantalla],proporciones.listaProporciones,pantalla)
    except TypeError:
        break