import pygame

pygame.init()
width = 1500
height = 800
screen = pygame.display.set_mode((width, height))
running = True

image = pygame.image.load("ball.png").convert()

xBall = width/2
yBall = height/2
vx = 5
vy = 0
dt = 1
G = 9.81
saut = 0
lineX = 0
lineY = 0
vitesse = [vx,vy]


clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            lineX = pygame.mouse.get_pos()[0]
            lineY = pygame.mouse.get_pos()[1]
        if event.type == pygame.MOUSEBUTTONUP :
            vx = (lineX - mouseX)/5
            vy = - ((lineY - mouseY)/(lineX - mouseX)) * vx
            dt = 1
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_LEFT]:
        vx = - 5
    if pressed[pygame.K_RIGHT]:
        vx = + 5
    if pressed[pygame.K_UP] and saut > 0:
        vy = 20
        dt = 1
        saut -= 1
    if pressed[pygame.K_DOWN]:
        running = False

    #Gravité

    xBall = xBall + vx * dt
    yBall = yBall - vy * dt
    vx = vx
    vy = vy - 0.1 * G * dt

    #Collision bords
    if xBall < 0 :  #bord gauche
        vx = 0
        xBall = 0
    if xBall > width - image.get_width():   #bord droit
        vx = 0
        xBall = width - image.get_width()
    if yBall < 0 :  #bord haut
        vy = 0
        yBall = 0
    if yBall + image.get_height() > height :    #bord bas
        vy = 0
        yBall = height - image.get_height()
        if saut < 5 :
            saut += 1




    #Gestion souris

    mousePos = pygame.mouse.get_pos()
    mouseX = mousePos[0]
    mouseY = mousePos[1]

    print(pygame.mouse.get_pressed())
    if pygame.mouse.get_pressed()[0]:
        line = pygame.draw.line(screen, (255, 255, 255), (lineX, lineY), (mouseX, mouseY), 4)



    screen.blit(image, (xBall, yBall))

    pygame.display.flip()
    clock.tick(60)
pygame.quit()