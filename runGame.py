import functions,proporciones

#pantalla inicial 
pantalla = 4
while pantalla != -1:
    try:
        if pantalla != -1:
            pantalla = functions.run(proporciones.imgs[pantalla],proporciones.listaProporciones,pantalla)
    except TypeError:
        break