import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))

pygame.display.set_caption("pierwsza gra")

x = 50
y = 70
width = 10
height = 10
vel = 5

run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x = x - vel
    if keys[pygame.K_RIGHT]:
        x = x + vel
    if keys[pygame.K_UP]:
        y = y - vel
    if keys[pygame.K_DOWN]:
        y = y + vel

#    win.fill((0,0,0))
    pygame.draw.rect(win, (255, 255, 255), (x, y, width, height))
    pygame.display.update()

pygame.quit()