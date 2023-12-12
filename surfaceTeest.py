import pygame ,sys

pygame.init()
window = pygame.display.set_mode((800,800))
window.fill((255,255,255))
pygame.display.set_caption('TANKS')
clock = pygame.time.Clock()




superfice = pygame.Surface((200,200))
superfice.fill((255,0,0))

item1text = pygame.font.Font(None, 30)
item1text = item1text.render(("x"), True, (0, 255, 0))




pygame.draw.rect(superfice,(0,0,0),(75,75,50,50),0)
superfice.blit(item1text,(25,25))
window.blit(superfice,(200,200))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(60)

