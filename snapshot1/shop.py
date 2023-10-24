import pygame,time,params
pygame.init()
class Shop:
    def __init__(self,player,color):
        self.player = player
        self.color = color
        #money
        self.money = 1000

        #stats
        self.shield = 0
        self.dmg = 0
        self.health = 0
        self.stats = []
        self.statsBotones = []
        
        #ammo
        self.bigStone = 0
        self.mediumStone = 0
        self.smallStone = 0
        self.ammo = []
        self.ammoBotones = []

        self.font = pygame.font.Font(None, 36)
        self.moneyFont = pygame.font.Font(None, 50)

        self.PlayerInfo = []
        
        #imgs
        self.bigStoneIMG = pygame.image.load(params.bigStoneIMG)
        self.bigStoneIMG = pygame.transform.scale(self.bigStoneIMG,(int(params.WIDTH/20),int(params.WIDTH/20)))

        self.mediumStoneIMG = pygame.image.load(params.mediumStoneIMG)
        self.mediumStoneIMG = pygame.transform.scale(self.mediumStoneIMG,(int(params.WIDTH/20),int(params.WIDTH/20)))

        self.smallStoneIMG = pygame.image.load(params.smallStoneIMG)
        self.smallStoneIMG = pygame.transform.scale(self.smallStoneIMG,(int(params.WIDTH/20),int(params.WIDTH/20)))

        self.shieldIMG = pygame.image.load(params.shieldIMG)
        self.shieldIMG = pygame.transform.scale(self.shieldIMG,(int(params.WIDTH/20),int(params.WIDTH/20)))

        self.swordIMG = pygame.image.load(params.swordIMG)
        self.swordIMG = pygame.transform.scale(self.swordIMG,(int(params.WIDTH/20),int(params.WIDTH/20)))

        self.elixirIMG = pygame.image.load(params.elixirIMG)
        self.elixirIMG = pygame.transform.scale(self.elixirIMG,(int(params.WIDTH/20),int(params.WIDTH/20)))

        self.addIMG = pygame.image.load(params.addIMG)
        self.addIMG = pygame.transform.scale(self.addIMG,(int(params.WIDTH/30),int(params.WIDTH/30)))

        self.minusIMG = pygame.image.load(params.minusIMG)
        self.minusIMG = pygame.transform.scale(self.minusIMG,(int(params.WIDTH/30),int(params.WIDTH/30)))

        self.coinIMG = pygame.image.load(params.coinIMG)
        self.coinIMG = pygame.transform.scale(self.coinIMG,(int(params.WIDTH/20),int(params.WIDTH/20)))

        self.backgroundShopIMG = pygame.image.load(params.backgroundShopIMG)
        self.backgroundShopIMG = pygame.transform.scale(self.backgroundShopIMG,(params.WIDTH,params.HEIGHT))

        self.shopBannerIMG = pygame.image.load(params.shopBannerIMG)
        self.shopBannerIMG = pygame.transform.scale(self.shopBannerIMG,(int(params.WIDTH/2),int(params.HEIGHT/4)))

        self.tankRedIMG = pygame.image.load(params.redTank)
        self.tankRedIMG = pygame.transform.scale(self.tankRedIMG,(int(params.WIDTH/20),int(params.WIDTH/20)))

        self.tankBlueIMG = pygame.image.load(params.blueTank)
        self.tankBlueIMG = pygame.transform.scale(self.tankBlueIMG,(int(params.WIDTH/20),int(params.WIDTH/20)))



    def drawShop(self,shopSurface,width,height):
        shopSurface.blit(self.backgroundShopIMG,(0,0))
        shopSurface.blit(self.shopBannerIMG,(int(width/4),int(height//20)))
        shopSurface.blit(self.coinIMG,(int(width*0.035),int(height//20)))
        money = self.moneyFont.render(f"{self.money}",True,(0,0,0))
        shopSurface.blit(money,(int(width*0.1),int(height//12)))

        #projectiles-------------------------------------------------------

        #piedra grande
        shopSurface.blit(self.bigStoneIMG,(int(width/1.3),int(height//3)))
        shopSurface.blit(self.addIMG,(int(width//1.5),int(height//3+height//40)))
        bigStoneAddButton = pygame.Rect(int(width//1.5),int(height//3+height//40),int(width/30),int(width/30))
        shopSurface.blit(self.minusIMG,(int(width//1.15),int(height//3+height//40)))
        bigStoneMinusButton = pygame.Rect(int(width//1.15),int(height//3+height//40),int(width/30),int(width/30))
        precioPiedraGrande = self.font.render("100",True,(0,0,0))
        shopSurface.blit(precioPiedraGrande,(int(width//1.285),int(height//3+height//10)))

        #piedra mediana
        shopSurface.blit(self.mediumStoneIMG,(int(width/1.3),int(height//2)))
        shopSurface.blit(self.addIMG,(int(width//1.5),int(height//2+height//40)))
        mediumStoneAddButton = pygame.Rect(int(width//1.5),int(height//2+height//40),int(width/30),int(width/30))
        shopSurface.blit(self.minusIMG,(int(width//1.15),int(height//2+height//40)))
        mediumStoneMinusButton = pygame.Rect(int(width//1.15),int(height//2+height//40),int(width/30),int(width/30))
        precioPiedraMediana = self.font.render("50",True,(0,0,0))
        shopSurface.blit(precioPiedraMediana,(int(width//1.285),int(height//2+height//10)))

        #piedra pequeña
        shopSurface.blit(self.smallStoneIMG,(int(width/1.3),int(height//1.5)))
        shopSurface.blit(self.addIMG,(int(width//1.5),int(height//1.5+height//40)))
        smallStoneAddButton = pygame.Rect(int(width//1.5),int(height//1.5+height//40),int(width/30),int(width/30))
        shopSurface.blit(self.minusIMG,(int(width//1.15),int(height//1.5+height//40)))
        smallStoneMinusButton = pygame.Rect(int(width//1.15),int(height//1.5+height//40),int(width/30),int(width/30))
        precioPiedraPequeña = self.font.render("25",True,(0,0,0))
        shopSurface.blit(precioPiedraPequeña,(int(width//1.285),int(height//1.5+height//10)))


        #escudo------------------------------------------------------------
        shopSurface.blit(self.shieldIMG,(int(width/8),int(height//3)))
        shopSurface.blit(self.addIMG,(int(width//25),int(height//3+height//40)))
        shieldAddButton = pygame.Rect(int(width//25),int(height//3+height//40),int(width/30),int(width/30))
        shopSurface.blit(self.minusIMG,(int(width//4.5),int(height//3+height//40)))
        shieldMinusButton = pygame.Rect(int(width//4.5),int(height//3+height//40),int(width/30),int(width/30))
        precioEscudo = self.font.render("100",True,(0,0,0))
        shopSurface.blit(precioEscudo,(int(width//7.5),int(height//3+height//10)))

        #espada------------------------------------------------------------
        shopSurface.blit(self.swordIMG,(int(width/8),int(height//2)))
        shopSurface.blit(self.addIMG,(int(width//25),int(height//2+height//40)))
        swordAddButton = pygame.Rect(int(width//25),int(height//2+height//40),int(width/30),int(width/30))
        shopSurface.blit(self.minusIMG,(int(width//4.5),int(height//2+height//40)))
        swordMinusButton = pygame.Rect(int(width//4.5),int(height//2+height//40),int(width/30),int(width/30))
        precioEspada = self.font.render("100",True,(0,0,0))
        shopSurface.blit(precioEspada,(int(width//7.5),int(height//2+height//10)))

        #elixir------------------------------------------------------------
        shopSurface.blit(self.elixirIMG,(int(width/8),int(height//1.5)))
        shopSurface.blit(self.addIMG,(int(width//25),int(height//1.5+height//40)))
        elixirAddButton = pygame.Rect(int(width//25),int(height//1.5+height//40),int(width/30),int(width/30))
        shopSurface.blit(self.minusIMG,(int(width//4.5),int(height//1.5+height//40)))
        elixirMinusButton = pygame.Rect(int(width//4.5),int(height//1.5+height//40),int(width/30),int(width/30))
        precioElixir = self.font.render("100",True,(0,0,0))
        shopSurface.blit(precioElixir,(int(width//7.5),int(height//1.5+height//10)))

        #player-----------------------------------------------------------
        if self.color == "red":
            shopSurface.blit(self.tankRedIMG,(int(width//2),int(height//2)))
        elif self.color == "blue":
            shopSurface.blit(self.tankBlueIMG,(int(width//2),int(height//2)))

        #botones stats
        self.statsBotones.append(shieldAddButton) #0
        self.statsBotones.append(shieldMinusButton) #1
        self.statsBotones.append(swordAddButton) #2
        self.statsBotones.append(swordMinusButton) #3
        self.statsBotones.append(elixirAddButton) #4   
        self.statsBotones.append(elixirMinusButton) #5

        #botones piedras
        self.ammoBotones.append(bigStoneAddButton) #0
        self.ammoBotones.append(bigStoneMinusButton) #1
        self.ammoBotones.append(mediumStoneAddButton) #2
        self.ammoBotones.append(mediumStoneMinusButton) #3
        self.ammoBotones.append(smallStoneAddButton) #4
        self.ammoBotones.append(smallStoneMinusButton) #5
        
        self.Botones = []

        self.Botones.append(self.statsBotones)
        self.Botones.append(self.ammoBotones)

        self.PlayerInfo.append(self.stats) #0
        self.PlayerInfo.append(self.ammo) #1

        return self.Botones
    
    def getPlayerInfo(self):
        return self.PlayerInfo

# shopSurface = pygame.display.set_mode((params.WIDTH,params.HEIGHT))
# tienditaPlayer1 = Shop(1)
# tienditaPlayer2 = Shop(2)

# infoTiendita1 = tienditaPlayer1.drawShop(shopSurface,params.WIDTH,params.HEIGHT)
# infoTiendita2 = tienditaPlayer2.drawShop(shopSurface,params.WIDTH,params.HEIGHT)

# run = True
# turno = 1
# if turno == 1:
#     tienda = infoTiendita1
# else:
#     tienda = infoTiendita2
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run = False
#         elif event.type == pygame.MOUSEBUTTONDOWN:
#             if infoTiendita1[1][0].collidepoint(event.pos):
#                 print("shield Add")
#                 if tienditaPlayer1.money>0:
#                     if tienditaPlayer1.shield <2:
#                         tienditaPlayer1.money -= 100
#                         tienditaPlayer1.shield += 1
#             if infoTiendita1[1][1].collidepoint(event.pos):
#                 print("shield Minus")
#                 if tienditaPlayer1.money<1000:
#                     if tienditaPlayer1.shield >0:
#                         tienditaPlayer1.shield -= 1
#                         tienditaPlayer1.money += 100
#             if infoTiendita1[1][2].collidepoint(event.pos):
#                 print("sword Add")
#                 if tienditaPlayer1.money>0:
#                     if tienditaPlayer1.dmg <2:
#                         tienditaPlayer1.money -= 100
#                         tienditaPlayer1.dmg += 1
            
#             if infoTiendita1[1][3].collidepoint(event.pos):
#                 print("sword Minus")
#                 if tienditaPlayer1.money<1000:
#                     if tienditaPlayer1.dmg >0:
#                         tienditaPlayer1.money += 100
#                         tienditaPlayer1.dmg -= 1
#             if infoTiendita1[1][4].collidepoint(event.pos):
#                 print("elixir Add")
#                 if tienditaPlayer1.money>0:
#                     if tienditaPlayer1.health <2:
#                         tienditaPlayer1.money -= 100
#                         tienditaPlayer1.health += 1
#             if infoTiendita1[1][5].collidepoint(event.pos):
#                 print("elixir Minus")
#                 if tienditaPlayer1.money<1000:
#                     if tienditaPlayer1.health >0:
#                         tienditaPlayer1.money += 100
#                         tienditaPlayer1.health -= 1
#             if infoTiendita1[3][0].collidepoint(event.pos):
#                 print("bigStone Add")
#                 if tienditaPlayer1.money>0:
#                     if tienditaPlayer1.bigStone <2:
#                         tienditaPlayer1.money -= 100
#                         tienditaPlayer1.bigStone += 1
#             if infoTiendita1[3][1].collidepoint(event.pos):
#                 print("bigStone Minus")
#                 if tienditaPlayer1.money<1000:
#                     if tienditaPlayer1.bigStone >0:
#                         tienditaPlayer1.money += 100
#                         tienditaPlayer1.bigStone -= 1
#             if infoTiendita1[3][2].collidepoint(event.pos):
#                 print("mediumStone Add")
#                 if tienditaPlayer1.money>0:
#                     if tienditaPlayer1.mediumStone <2:
#                         tienditaPlayer1.money -= 100
#                         tienditaPlayer1.mediumStone += 1
#             if infoTiendita1[3][3].collidepoint(event.pos):
#                 print("mediumStone Minus")
#                 if tienditaPlayer1.money<1000:
#                     if tienditaPlayer1.mediumStone >0:
#                         tienditaPlayer1.money += 100
#                         tienditaPlayer1.mediumStone -= 1
#             if infoTiendita1[3][4].collidepoint(event.pos):
#                 print("smallStone Add")
#                 if tienditaPlayer1.money>0:
#                     if tienditaPlayer1.smallStone <2:
#                         tienditaPlayer1.money -= 100
#                         tienditaPlayer1.smallStone += 1
#             if infoTiendita1[3][5].collidepoint(event.pos):
#                 print("smallStone Minus")
#                 if tienditaPlayer1.money<1000:
#                     if tienditaPlayer1.smallStone >0:
#                         tienditaPlayer1.money += 100
#                         tienditaPlayer1.smallStone -= 1
            
#     tienditaPlayer1.drawShop(shopSurface,params.WIDTH,params.HEIGHT)
#     pygame.display.update()


