import pygame
class InfoBlock:
    def __init__(self,screen,player,width,height,angle,power,lastPower,maxRange,maxHeight):
        self.player = player
        self.screen = screen
        self.width = width
        self.height = height
        self.font = pygame.font.Font(None, 25)
        self.big_font = pygame.font.Font(None, 72)
        
        self.angle = angle
        self.power = power

        self.lastAngle = angle
        self.lastPower = lastPower
        self.lastRange = maxRange
        self.lastHeight = maxHeight



    def drawInfoBlock(self,surfaceInfoBlock,power,angle,lastPower,lastAngle,lastRange,maxHeight):

        self.angle = angle
        self.power = power
        self.lastAngle = lastAngle
        self.lastPower = lastPower
        self.lastRange = lastRange
        self.lastHeight = maxHeight

        #nueva info
        
        
        textoAngulo = self.font.render(f'ACTUAL ANGLE PLAYER  {self.player}: {self.angle:.1f}', True, 'black')
        textoPotencia = self.font.render(f'ACTUAL POWER PLAYER  {self.player}: {self.power:.1f}', True, 'black')
        textoAltura = self.font.render(f'MAX HEIGHT PLAYER  {self.player}: {self.lastHeight:.1f}', True, 'black')

        #anterior info
        textoLastAngle = self.font.render(f'LAST ANGLE PLAYER  {self.player}: {self.lastAngle:.1f}', True, 'black')
        textoLastPower = self.font.render(f'LAST POWER PLAYER  {self.player}: {self.lastPower:.1f}', True, 'black')
        textoLastRange = self.font.render(f'LAST RANGE PLAYER  {self.player}: {self.lastRange:.1f}', True, 'black')
        textoLastHeight = self.font.render(f'LAST HEIGHT PLAYER  {self.player}: {self.lastHeight:.1f}', True, 'black')

        #escribe en pantalla
        if self.player ==1:
            surfaceInfoBlock.blit(textoAngulo,(20,self.height*0.7))
            surfaceInfoBlock.blit(textoPotencia,(20,self.height*0.7 +30))
            surfaceInfoBlock.blit(textoAltura,(20,self.height*0.7 +60))
            surfaceInfoBlock.blit(textoLastAngle,(20,self.height*0.7 +90))
            surfaceInfoBlock.blit(textoLastPower,(20,self.height*0.7 +120))
            surfaceInfoBlock.blit(textoLastRange,(20,self.height*0.7 +150))
            surfaceInfoBlock.blit(textoLastHeight,(20,self.height*0.7 +180))

        if self.player ==2:
            textoAngulo = self.font.render(f'ACTUAL ANGLE PLAYER  {self.player}: {180-self.angle:.1f}', True, 'black')
            surfaceInfoBlock.blit(textoAngulo,(20 + self.width*0.7,self.height*0.7))
            surfaceInfoBlock.blit(textoPotencia,(20 + self.width*0.7,self.height*0.7 +30))
            surfaceInfoBlock.blit(textoAltura,(20 + self.width*0.7,self.height*0.7 +60))
            surfaceInfoBlock.blit(textoLastAngle,(20 + self.width*0.7,self.height*0.7 +90))
            surfaceInfoBlock.blit(textoLastPower,(20 + self.width*0.7,self.height*0.7 +120))
            surfaceInfoBlock.blit(textoLastRange,(20 + self.width*0.7,self.height*0.7 +150))
            surfaceInfoBlock.blit(textoLastHeight,(20 + self.width*0.7,self.height*0.7 +180))
            #pygame.draw.rect(surfaceInfoBlock, 'white', (20,self.height*0.7,self.width,self.height*0.3))    
    def deleteLast(self,surfaceInfoBlock):
        if self.player ==1:
            pygame.draw.rect(surfaceInfoBlock, (255, 213, 158), (20,self.height*0.7,self.width//2,self.height*0.3))
        if self.player ==2:
            pygame.draw.rect(surfaceInfoBlock, (255, 213, 158), (20 + self.width*0.7,self.height*0.7,self.width//2,self.height*0.3))