import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("pierwsza gra")

x = 50
y = 440
width = 40
height = 60
vel = 5

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x > 0:
        x = x - vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x = x + vel
    if keys[pygame.K_UP] and y > 0:
        y = y - vel
    if keys[pygame.K_DOWN] and y <500 - height:
        y = y + vel

    win.fill((0,0,0))
    pygame.draw.rect(win, (50, 255, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()