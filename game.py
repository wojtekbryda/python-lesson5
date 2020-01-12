import pygame
pygame.init()

win = pygame.display.set_mode((500, 485))

pygame.display.set_caption("pierwsza gra")
walkRight = [
    pygame.image.load('Game/R1.png'),
    pygame.image.load('Game/R2.png'),
    pygame.image.load('Game/R3.png'),
    pygame.image.load('Game/R4.png'),
    pygame.image.load('Game/R5.png'),
    pygame.image.load('Game/R6.png'),
    pygame.image.load('Game/R7.png'),
    pygame.image.load('Game/R8.png'),
    pygame.image.load('Game/R9.png')
]
walkLeft = [
    pygame.image.load('Game/L1.png'),
    pygame.image.load('Game/L2.png'),
    pygame.image.load('Game/L3.png'),
    pygame.image.load('Game/L4.png'),
    pygame.image.load('Game/L5.png'),
    pygame.image.load('Game/L6.png'),
    pygame.image.load('Game/L7.png'),
    pygame.image.load('Game/L8.png'),
    pygame.image.load('Game/L9.png')
]
bg = pygame.image.load('Game/bg.jpg')
char = pygame.image.load('Game/standing.png')

clock = pygame.time.Clock()


x = 50
y = 415
width = 64
height = 64
vel = 5
left = False
right = False
walkCount = 0


def redrawGameWindow():
    global walkCount
    win.blit(bg, (0,0))
    if walkCount + 1 >= 27:
        walkCount = 0
    if left:
        win.blit(walkLeft[walkCount//3], (x,y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x,y))


    pygame.display.update()


isJump = False
jumpVelUp = 10
jumpVelDown = 0

run = True
while run:
    clock.tick(27)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 0:
        x = x - vel
        right = False
        left = True
    elif keys[pygame.K_RIGHT] and x < 500 - width:
        x = x + vel
        right = True
        left = False
    else:
        right = False
        left = False
        walkCount = 0
    if not(isJump):
        if keys[pygame.K_SPACE]:
            isJump = True
            right = False
            left = False
            walkCount = 0
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
    redrawGameWindow()

pygame.quit()