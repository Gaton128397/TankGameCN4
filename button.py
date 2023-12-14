import pygame,params

class Button:
    def __init__(self, x_percent, y_percent, width_percent, height_percent,item):
        self.x_percent = x_percent
        self.y_percent = y_percent
        self.width_percent = width_percent
        self.height_percent = height_percent

        self.rect = pygame.Rect(
            params.size*16 * self.x_percent,
            params.size*9 * self.y_percent,
            params.size*16 * self.width_percent,
            params.size*9 * self.height_percent
)
        self.clicked = False

        #lo que tiene que hacer, algo asi como el evento 
        self.item = item
    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos) and not self.clicked:
                return True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.clicked = False
        return False
    
    def resizeButton(self):
        self.rect = pygame.Rect(
            params.size*16 * self.x_percent,
            params.size*9 * self.y_percent,
            params.size*16 * self.width_percent,
            params.size*9 * self.height_percent
)
    def getBoton(self):
        return (self.rect.x,self.rect.y,self.rect.width,self.rect.height,self.item)
