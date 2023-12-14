from pygame import display,image
size = 100
screen = display.set_mode((size*16, size*9))

#imgs
#icons
shield = image.load('items/shield.png')
dmg = image.load('items/dmg.png')
health = image.load('items/health.png')
bigStone = image.load('items/105mmStone.png')
mediumStone = image.load('items/80mmStone.png')
smallStone = image.load('items/60mmStone.png')