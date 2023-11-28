import pygame
class ChooseMenu:
    def __init__(self,window,width,height):
        self.window = window
        self.width = width
        self.height = height
        self.pos=[width*0.41,height*0.7,40,40,10]
        self.pos2=[width*0.41+50,height*0.7,40,40,8]
        self.pos3=[width*0.41+100,height*0.7,40,40,6]

        self.matrizPos=[self.pos,self.pos2,self.pos3]
        self.typeBullet=1
    def noFillingRectangle(self,screen,rect_color,rect_position,rect_size):
        pygame.draw.line(screen, rect_color, rect_position, (rect_position[0] + rect_size[0], rect_position[1]), 2)
        pygame.draw.line(screen, rect_color, (rect_position[0] + rect_size[0], rect_position[1]), (rect_position[0] + rect_size[0], rect_position[1] + rect_size[1]), 2)
        pygame.draw.line(screen, rect_color, (rect_position[0] + rect_size[0], rect_position[1] + rect_size[1]), (rect_position[0], rect_position[1] + rect_size[1]), 2)
        pygame.draw.line(screen, rect_color, (rect_position[0], rect_position[1] + rect_size[1]), rect_position, 2)
                
    def options(self,surfaceChooseMenu,position): 
        pygame.draw.circle(surfaceChooseMenu, 'black',(position[0]+self.width/65,position[1]+self.width/65),position[4])

        
    def delOpBef(self,surfaceChooseMenu,position):
        self.noFillingRectangle(surfaceChooseMenu,(255, 213, 158),(position[0],position[1]),(position[2],position[3]))
        
    def choose(self,surfaceChooseMenu,position):
        self.noFillingRectangle(surfaceChooseMenu,'red',(position[0],position[1]),(position[2],position[3])) 

    def drawChooseMenu(self,surfaceChooseMenu,state,cantidad):
        rectangulo = pygame.Surface((310,50))
        rectangulo.fill((255, 213, 158))
        font = pygame.font.Font(None, 20)

        textAmmo1 = font.render(f"x{cantidad[0]}", True, 'black')
        surfaceChooseMenu.blit(textAmmo1,(self.pos[0]+20,self.pos[1]+55))
        
        textAmmo2 = font.render(f"x{cantidad[1]}", True, 'black')
        surfaceChooseMenu.blit(textAmmo2,(self.pos[0]+60,self.pos[1]+55))

        textAmmo = font.render(f"x{cantidad[2]}", True, 'black')
        surfaceChooseMenu.blit(textAmmo,(self.pos[0]+120,self.pos[1]+55))

        if state == 0:
            self.choose(surfaceChooseMenu,self.matrizPos[0])
            self.options(surfaceChooseMenu,self.matrizPos[0])
            self.options(surfaceChooseMenu,self.matrizPos[1])
            self.options(surfaceChooseMenu,self.matrizPos[2])
            
            
        if state == 1:
            surfaceChooseMenu.blit(rectangulo,(self.width*0.40,self.height*0.70))

            self.choose(surfaceChooseMenu,self.matrizPos[0])
            self.options(surfaceChooseMenu,self.matrizPos[0])
            self.options(surfaceChooseMenu,self.matrizPos[1])
            self.options(surfaceChooseMenu,self.matrizPos[2])
            
        if state == 2:
            surfaceChooseMenu.blit(rectangulo,(self.width*0.40,self.height*0.70))

            self.choose(surfaceChooseMenu,self.matrizPos[1])
            self.options(surfaceChooseMenu,self.matrizPos[0])
            self.options(surfaceChooseMenu,self.matrizPos[1])
            self.options(surfaceChooseMenu,self.matrizPos[2])
            

        if state == 3:
            # surfaceChooseMenu.blit(rectangulo,(self.width*0.40,self.height*0.70))

            #borra los anteriores y lo cambia al nuevo
            self.choose(surfaceChooseMenu,self.matrizPos[2])
            self.options(surfaceChooseMenu,self.matrizPos[0])
            self.options(surfaceChooseMenu,self.matrizPos[1])
            self.options(surfaceChooseMenu,self.matrizPos[2])



        
        