import pygame,sys,items
class Button:
    def __init__(self, rect, color,item,virtual):
        self.rect = pygame.Rect(rect)
        self.color = color
        self.clicked = False
        self.virtual = virtual
        self.item = item
        
    def draw(self, screen):
        if not self.virtual:
            pygame.draw.rect(screen, self.color, self.rect)

    def check_click(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos) and not self.clicked:
                self.clicked = True
                return True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.clicked = False
        return False


