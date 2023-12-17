from pygame import display, image
playersNumber = 2
roundNumber = 1

gravityConstant = 9.8
size = 100
screen = display.set_mode((size*16, size*9))
#icons
shield = image.load('items/shield.png')
dmg = image.load('items/dmg.png')
health = image.load('items/health.png')
bigStone = image.load('items/105mmStone.png')
mediumStone = image.load('items/80mmStone.png')
smallStone = image.load('items/60mmStone.png')
mapa = None
modo = 0
jugadorNoIa = None