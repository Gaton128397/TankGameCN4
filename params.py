from pygame import image,transform

size = 100 #fullScreen = 120
WIDTH,HEIGHT = size*16,size*9

#bg
menuImg = image.load('imgs/Menu.png')
shopImg = image.load('imgs/shop.png')
playModeImg = image.load('imgs/playmode.png')
settingsImg = image.load('imgs/settings.png')
bgDesert = image.load('imgs/desierto.png')
bgSelva = image.load('imgs/selva.png')
bgSnow = image.load('imgs/nieve.png')

menuImg = transform.scale(menuImg, (WIDTH, HEIGHT))
shopImg = transform.scale(shopImg, (WIDTH, HEIGHT))
playModeImg = transform.scale(playModeImg, (WIDTH, HEIGHT))
settingsImg = transform.scale(settingsImg, (WIDTH, HEIGHT))
bgDesert = transform.scale(bgDesert, (WIDTH, HEIGHT))
bgSelva = transform.scale(bgSelva, (WIDTH, HEIGHT))
bgSnow = transform.scale(bgSnow, (WIDTH, HEIGHT))

#icons
shield = image.load('imgs/shield.png')
dmg = image.load('imgs/dmg.png')
health = image.load('imgs/health.png')
bigStone = image.load('imgs/BigStone.png')
mediumStone = image.load('imgs/mediumStone.png')
smallStone = image.load('imgs/smallStone.png')
shield = transform.scale(shield, (size, size))
dmg = transform.scale(dmg, (size, size))
health = transform.scale(health, (size, size))
bigStone = transform.scale(bigStone, (size, size))
mediumStone = transform.scale(mediumStone, (size, size))
smallStone = transform.scale(smallStone, (size, size))

