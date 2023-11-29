from pygame import image,transform

size = 100 #fullScreen = 120
WIDTH,HEIGHT = size*16,size*9

#bg
menuImg = image.load('imgs/Menu.png')
shopIniImg = image.load('imgs/shopIni.png')
shopMidImg = image.load('imgs/shopMid.png')
shopFinImg = image.load('imgs/shopFin.png')
playModeImg = image.load('imgs/playmode.png')
settingsImg = image.load('imgs/settings.png')
bGganador1 = image.load('imgs/ganador1.png')
bGanador2 = image.load('imgs/ganador2.png')
bgMapas = image.load('imgs/mapas.png')

#mapas
mapaDesert = image.load('imgs/desierto.png')
mapaSelva = image.load('imgs/selva.png')
mapaSnow = image.load('imgs/nieve.png')
mapaGalaxia = image.load('imgs/galaxia.png')
mapaCiudad = image.load('imgs/ciudad.png')

#icons
shield = image.load('imgs/shield.png')
dmg = image.load('imgs/dmg.png')
health = image.load('imgs/health.png')
bigStone = image.load('imgs/BigStone.png')
mediumStone = image.load('imgs/mediumStone.png')
smallStone = image.load('imgs/smallStone.png')

#loads
menuImg = transform.scale(menuImg, (WIDTH, HEIGHT))

shopIniImg = transform.scale(shopIniImg, (WIDTH, HEIGHT))
shopMidImg = transform.scale(shopMidImg, (WIDTH, HEIGHT))
shopFinImg = transform.scale(shopFinImg, (WIDTH, HEIGHT))
bgGanador1 = transform.scale(bGganador1, (WIDTH, HEIGHT))
bgGanador2 = transform.scale(bGanador2, (WIDTH, HEIGHT))
bgMapas = transform.scale(bgMapas, (WIDTH, HEIGHT))

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

