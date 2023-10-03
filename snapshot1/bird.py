import pygame
import sys
pygame.init()

#colors
WHITE = (255, 255, 255)
BLACK = (0,0,0)
YELLOW = (255, 255, 0)

#Screen
size = (800, 600)
screen=pygame.display.set_mode(size)

def draw_bird(window,x, y):
    pygame.draw.polygon(window, YELLOW, [(x+30, y-15), (x+50, y), (x+30, y+15)])  # Pico
    pygame.draw.circle(window, WHITE, (x+40, y-5), 5)  # Ojo
def prueba():
    pygame.draw.polygon(screen, YELLOW, [(100, 100), (120, 120), (100, 140)])  # Pico
    pygame.draw.circle(screen, WHITE, (110, 110), 5)  # Ojo

# while True: 
# 	for event in pygame.event.get():
# 		if event.type == pygame.QUIT:
# 			sys.exit()
# 	#background color
# 	screen.fill(BLACK)
# 	#Draw	
# 	draw_bird(100, 100)
# 	#ScreenRefresh