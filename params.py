from pygame import image,transform,Surface


size = 100 #fullScreen = 120
WIDTH,HEIGHT = size*16,size*9
playersNumber = 6
#screens
menuImg = image.load('imgs/startEnd/Menu.png')
bGganador1 = image.load('imgs/startEnd/ganador1.png')
bGanador2 = image.load('imgs/startEnd/ganador2.png')
shopIniImg = image.load('imgs/shop/shopIni.png')
shopMidImg = image.load('imgs/shop/shopMid.png')
shopFinImg = image.load('imgs/shop/shopFin.png')
pausaImg = image.load('imgs/pausa/pausa.png')
settingsPausa = image.load('imgs/pausa/settingsPause.png')
settingsImg = image.load('imgs/varios/settings.png')
controlesImg = image.load('imgs/varios/controles.png')
playModeImg = image.load('imgs/varios/playmode.png')
bgMapas = image.load('imgs/maps/mapas.png')
difficulty = image.load('imgs/varios/dificultad.png')

#mapas
mapaDesert = image.load('imgs/maps/desierto.png')
mapaSelva = image.load('imgs/maps/selva.png')
mapaSnow = image.load('imgs/maps/nieve.png')
mapaGalaxia = image.load('imgs/maps/galaxia.png')
mapaCiudad = image.load('imgs/maps/ciudad.png')

#icons
shield = image.load('imgs/icons/shield.png')
dmg = image.load('imgs/icons/dmg.png')
health = image.load('imgs/icons/health.png')
bigStone = image.load('imgs/icons/BigStone.png')
mediumStone = image.load('imgs/icons/mediumStone.png')
smallStone = image.load('imgs/icons/smallStone.png')

heartFull = image.load('imgs/health/full.png')
heartsHalf = image.load('imgs/health/half.png')
heartsNone = image.load('imgs/health/none.png')
parachute = image.load('imgs/icons/parachute.png')
anguloICO = image.load('imgs/icons/angulo.png')
balaICO = image.load('imgs/icons/bala.png')
balasICO = image.load('imgs/icons/balas.png')
distanciaICO = image.load('imgs/icons/distancia.png')

#loads
menuImg = transform.scale(menuImg, (WIDTH, HEIGHT))
shopIniImg = transform.scale(shopIniImg, (WIDTH, HEIGHT))
shopMidImg = transform.scale(shopMidImg, (WIDTH, HEIGHT))
shopFinImg = transform.scale(shopFinImg, (WIDTH, HEIGHT))
bgGanador1 = transform.scale(bGganador1, (WIDTH, HEIGHT))
bgGanador2 = transform.scale(bGanador2, (WIDTH, HEIGHT))
bgMapas = transform.scale(bgMapas, (WIDTH, HEIGHT))
pausaImg = transform.scale(pausaImg, (WIDTH, HEIGHT))
settingsPausa = transform.scale(settingsPausa, (WIDTH, HEIGHT))
controlesImg = transform.scale(controlesImg, (WIDTH, HEIGHT))
playModeImg = transform.scale(playModeImg, (WIDTH, HEIGHT))
settingsImg = transform.scale(settingsImg, (WIDTH, HEIGHT))

bgDesert = transform.scale(mapaDesert, (WIDTH, HEIGHT))
bgSelva = transform.scale(mapaSelva, (WIDTH, HEIGHT))
bgSnow = transform.scale(mapaSnow, (WIDTH, HEIGHT))
bgGalaxia = transform.scale(mapaGalaxia, (WIDTH, HEIGHT))
bgCiudad = transform.scale(mapaCiudad, (WIDTH, HEIGHT))

shield = transform.scale(shield, (size, size))
dmg = transform.scale(dmg, (size, size))
health = transform.scale(health, (size, size))
bigStone = transform.scale(bigStone, (size, size))
mediumStone = transform.scale(mediumStone, (size, size))
smallStone = transform.scale(smallStone, (size, size))

parachute = transform.scale(parachute, (size*0.2,size*0.5))
#METODOS