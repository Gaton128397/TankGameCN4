import pygame
import sys
# pygame.init()

# #colors
# WHITE = (255, 255, 255)
# BLACK = (0,0,0)

# #Screen
# size = (800, 600)
# screen=pygame.display.set_mode(size)

class Cloud:
    def __init__(self,window, x, y, tangible):
        self.screen = window
        self.x = x
        self.y = y
        self.tangible = tangible

    def draw(self):
        pygame.draw.circle(self.screen, 'white', (self.x, self.y), 30)
        pygame.draw.circle(self.screen, 'white', (self.x+15, self.y-10), 30)
        pygame.draw.circle(self.screen, 'white', (self.x+45, self.y-10), 30)
        pygame.draw.circle(self.screen, 'white', (self.x+60, self.y), 30)
        pygame.draw.circle(self.screen, 'white', (self.x+30, self.y), 30)

# cloud1 = Cloud(100, 100, tangible=True)

# while True: 
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             sys.exit()
    
# 	#background color
#     screen.fill(BLACK)
#     #Draw
#     cloud1.draw()
#     #ScreenRefresh
#     pygame.display.flip()
