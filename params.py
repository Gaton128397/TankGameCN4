from pygame import image,transform,Surface,display


size = 80 #fullScreen = 120
playersNumber = 2
gravityConstant = 9.8
screen = display.set_mode((size*16, size*9))
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
bigStone = image.load('imgs/icons/105mmStone.png')
mediumStone = image.load('imgs/icons/80mmStone.png')
smallStone = image.load('imgs/icons/60mmStone.png')

heartFull = image.load('imgs/health/full.png')
heartsHalf = image.load('imgs/health/half.png')
heartsNone = image.load('imgs/health/none.png')
parachute = image.load('imgs/icons/parachute.png')
anguloICO = image.load('imgs/icons/angulo.png')
balaICO = image.load('imgs/icons/bala.png')
balasICO = image.load('imgs/icons/balas.png')
distanciaICO = image.load('imgs/icons/distancia.png')

#loads
menuImg = transform.scale(menuImg, (size*16, size*9))
shopIniImg = transform.scale(shopIniImg, (size*16, size*9))
shopMidImg = transform.scale(shopMidImg, (size*16, size*9))
shopFinImg = transform.scale(shopFinImg, (size*16, size*9))
bgGanador1 = transform.scale(bGganador1, (size*16, size*9))
bgGanador2 = transform.scale(bGanador2, (size*16, size*9))
bgMapas = transform.scale(bgMapas, (size*16, size*9))
pausaImg = transform.scale(pausaImg, (size*16, size*9))
settingsPausa = transform.scale(settingsPausa, (size*16, size*9))
controlesImg = transform.scale(controlesImg, (size*16, size*9))
playModeImg = transform.scale(playModeImg, (size*16, size*9))
settingsImg = transform.scale(settingsImg, (size*16, size*9))

bgDesert = transform.scale(mapaDesert, (size*16, size*9))
bgSelva = transform.scale(mapaSelva, (size*16, size*9))
bgSnow = transform.scale(mapaSnow, (size*16, size*9))
bgGalaxia = transform.scale(mapaGalaxia, (size*16, size*9))
bgCiudad = transform.scale(mapaCiudad, (size*16, size*9))

shield = transform.scale(shield, (size, size))
dmg = transform.scale(dmg, (size, size))
health = transform.scale(health, (size, size))
bigStone = transform.scale(bigStone, (size, size))
mediumStone = transform.scale(mediumStone, (size, size))
smallStone = transform.scale(smallStone, (size, size))

parachute = transform.scale(parachute, (size*0.2,size*0.5))
#METODOS



