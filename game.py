import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("pierwsza gra")

x = 50
y = 440
width = 40
height = 60
vel = 5


isJump = False
jumpVelUp = 10
jumpVelDown = 0

run = True
while run:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x = x - vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x = x + vel
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if (jumpVelUp > 0):
            y = y - jumpVelUp
            jumpVelUp = jumpVelUp - 1
        else:
            if (jumpVelDown <= 11):
                y = y + jumpVelDown
                jumpVelDown = jumpVelDown + 1
                if jumpVelDown == 11:
                    isJump = False
                    jumpVelUp = 10
                    jumpVelDown = 0

    # if keys[pygame.K_UP] and y > 0:
    #     y = y - vel
    # if keys[pygame.K_DOWN] and y <500 - height:
    #     y = y + vel

    win.fill((0,0,0))
    pygame.draw.rect(win, (50, 255, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()