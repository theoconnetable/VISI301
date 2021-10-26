import pygame
from aleatoire import aleatoire


class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("ball.png")
        self.image
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 5
        self.velocity = [0, 0]
        self.health = 100
        self.max_health = 100

    def move(self):
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
        


class Game:
    def __init__(self, screen, x1, y1):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(0, 0)
        self.image2 = pygame.image.load("star.png")
        self.area = self.image2.get_rect(x=x1,y=y1)


    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.velocity[0] = -1
        elif keys[pygame.K_RIGHT]:
            self.player.velocity[0] = 1
        else:
            self.player.velocity[0] = 0

        if keys[pygame.K_UP]:
            self.player.velocity[1] = -1
        elif keys[pygame.K_DOWN]:
            self.player.velocity[1] = 1
        else:
            self.player.velocity[1] = 0

    def update(self):
        self.player.move()
        if self.area.colliderect(self.player.rect):
            ##mettre score
            ##Changer position sprite (creer var)
        ##else: pas besoin pour le moment
            score = 1


    def display(self):
        self.screen.fill("black")
        screen.blit(self.image2, self.area)
        self.player.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            
            #Gestion de la barre de vie 
    def update_health_bar(surface):
        #Couleru de la barre de vie
        bar_color = (255,255,255) 
        back_bar_color = (127,127,127)
        
        #position de la barre de vie 
        bar_position = [x1+20,y1+20,50,10]
        back_bar_position = [x1+20,y1+20,100,10]
        
        #dessiner la barre de vie
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)
        
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(60)


pygame.init()
screen = pygame.display.set_mode((1080, 720))
x1 = aleatoire(1080,720)[0]
y1 = aleatoire(1080,720)[1]
game = Game(screen,x1,y1)
game.run()  
Player.update_health_bar(screen)

pygame.quit()
