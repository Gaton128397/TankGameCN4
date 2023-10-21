import pygame
class ChooseMenu:
    def __init__(self,window,width,height):
        self.window = window
        self.width = width
        self.height = height
        positionX = width/2
        positionY = height/628
        widthSquare = width/21
        heightSquare = height/23
        radius = width/130
        self.pos=[610,30,40,40,10]
        self.pos2=[660,30,40,40,8]
        self.pos3=[710,30,40,40,6]

        self.matrizPos=[self.pos,self.pos2,self.pos3]

        self.size=0

        self.ammo=[3,10,3] 
    def noFillingRectangle(self,screen,rect_color,rect_position,rect_size):
        pygame.draw.line(screen, rect_color, rect_position, (rect_position[0] + rect_size[0], rect_position[1]), 2)
        pygame.draw.line(screen, rect_color, (rect_position[0] + rect_size[0], rect_position[1]), (rect_position[0] + rect_size[0], rect_position[1] + rect_size[1]), 2)
        pygame.draw.line(screen, rect_color, (rect_position[0] + rect_size[0], rect_position[1] + rect_size[1]), (rect_position[0], rect_position[1] + rect_size[1]), 2)
        pygame.draw.line(screen, rect_color, (rect_position[0], rect_position[1] + rect_size[1]), rect_position, 2)
                
    def options(self,window,position): 
        pygame.draw.circle(window, 'black',(position[0]+self.width/65,position[1]+self.width/65),position[4])
        pygame.draw.rect(window, 'white', (position[0],position[1]+self.width/28.8,position[2], position[3]))
        #("llega aqui")
        pygame.display.update()

    def choose(self,window,position):
        self.noFillingRectangle(window,'red',(position[0],position[1]),(position[2],position[3])) 


    def delOpBef(self,window,position):
        self.noFillingRectangle(window,'lightblue',(position[0],position[1]),(position[2],position[3]))  


    def choosing(self):
        

        self.options(self.window,self.matrizPos[0])
        self.options(self.window,self.matrizPos[1])
        self.options(self.window,self.matrizPos[2])
        i=0
        keys = pygame.key.get_pressed()
        if self.ammo[0] and self.ammo[1] and self.ammo[2] ==0:
            return self.size
        else:
            if keys[pygame.K_1]:
                if self.ammo[0] > 0:
                    self.choose(self.window,self.matrizPos[0])
                    self.delOpBef(self.window,self.matrizPos[1])
                    self.delOpBef(self.window,self.matrizPos[2])
                    self.size = 10
                    self.ammo[0] -=1
                    print('hola 1')
                else:
                    print("No 10mm ammo")

            if keys[pygame.K_2]:
                if self.ammo[1] > 0:
                    self.choose(self.window,self.matrizPos[1])
                    self.delOpBef(self.window,self.matrizPos[2])
                    self.delOpBef(self.window,self.matrizPos[0])
                    self.size = 8
                    self.ammo[1] -=1
                    print('hola 2')
                else:
                    print("No 8mm ammo")

            if keys[pygame.K_3]:
                if self.ammo[2] > 0:
                    self.choose(self.window,self.matrizPos[2])
                    self.delOpBef(self.window,self.matrizPos[0])
                    self.delOpBef(self.window,self.matrizPos[1])
                    self.size = 6
                    self.ammo[2] -=1
                    print('hola 3')
                else:
                    print("No 6mm ammo")
            