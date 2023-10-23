if event.key == pygame.K_1:
    if turno ==1:
        if ammoPlayer1[0] > 0:
            ammoPlayer1[0] -=1
            bulletTypePlayer1 = 1
        else:
            print("no 10mm ammo")
    else:
        if ammoPlayer2[0] > 0:
            ammoPlayer2[0] -=1
            bulletTypePlayer2 = 1
        else:
            print("no 10mm ammo")
if event.key == pygame.K_2:
    if turno ==1:
        if ammoPlayer1[1] > 0:
            ammoPlayer1[1] -=1
            bulletTypePlayer1 = 2
        else:
            
            print("no 8mm ammo")
    else:
        if ammoPlayer2[1] > 0:
            ammoPlayer2[1] -=1
            bulletTypePlayer2 = 2
        else:
            print("no 8mm ammo")
if event.key == pygame.K_3:
    if turno ==1:
        if ammoPlayer1[2] > 0:
            ammoPlayer1[2] -=1
            bulletTypePlayer1 = 3
        else:
            print("no 6mm ammo")
    else:
        if ammoPlayer2[2] > 0:
            ammoPlayer2[2] -=1
            bulletTypePlayer2 = 3
        else:
            print("no 6mm ammo")