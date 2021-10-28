import pygame
from aleatoire import aleatoire


class Player:
    #Le joueur
    
    def __init__(self, x, y):
         ##Initialisation du jouer : x,y : entiers (position du joueur en(x,y))
        self.image = pygame.image.load("ball.png")
        ######################################################################-------------------------------------------------------------------------self.image
        self.rect = self.image.get_rect(x=x, y=y)
        ##L'affichage du joueur est définie par la variable 'image'
        ##Sa position ainsi que "hitbox" sont définies par 'rect'
        self.speed = 1
        self.velocity = [0, 0]
        self.health = 100
        self.max_health = 100
        ##########################################################################-----Ajout commentaires

    def move(self):
        ##Mouvement du joueur
        ##########################################################################-----Ajout commentaires
        self.rect.move_ip(self.velocity[0] * self.speed, self.velocity[1] * self.speed)
        if self.rect.left < 0:
            self.velocity[0] = 0
            self.rect.left = 0
        if  self.rect.right > screen.get_width():
            self.velocity[0] = 0
            self.rect.right = screen.get_width()
        if self.rect.top < 0:
            self.velocity[1] = 0
            self.rect.top = 0
        if  self.rect.bottom > screen.get_height():
            self.velocity[1] = 0
            self.rect.bottom = screen.get_height()

    def draw(self, screen):
        ##Affichage du joueur
        screen.blit(self.image, self.rect)


    ##La barre de vie 
    def update_health_bar(self, screen):
        ##Couleur de la barre de vie + barre d'arrière plan
        bar_color = (255,255,255) 
        back_bar_color = (127,127,127)
        
        ##position de la barre de vie 
        bar_position = [100,100,50,10]
        back_bar_position = [20,20,100,10]
        
        ##dessiner la barre de vie
        pygame.draw.rect(screen, back_bar_color, back_bar_position)
        pygame.draw.rect(screen, bar_color, bar_position)
        

class star:
    ##L'étoile
    def __init__(self,x1, y1):
         ##Initialisation du jouer : x,y : entiers (position du joueur en(x1,y1))
        self.image2 = pygame.image.load("star.png")
        self.area = self.image2.get_rect(x=x1,y=y1)
        ##L'affichage de l'étoile est définit par la variable 'image2'
        ##Sa position ainsi que "hitbox" sont définies par 'area'

    def move(self):
        ####-----------------------if self.area.colliderect(self.player.rect):
            star(aleatoire(1080,720)[0],aleatoire(1080,720)[1])
            ##mettre score
            ##Changer position sprite (creer var)
        ##else: pas besoin pour le moment

    def draw(self, screen):
        screen.blit(self.image2, self.area)

            
class Game:
    ##Le jeu

    def __init__(self, screen):
        ##Initialisation du jouer : x,y : entiers (position du joueur en(x,y))
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        ##########################################################################-----Ajout commentaires
        self.player = Player(200, 200)
        self.star = star(aleatoire(1080,720)[0],aleatoire(1080,720)[1])
        ##On definit les positions initiales du joueur et de l'étoile
        
    def handling_events(self):
        ##Effectue les actions entrées par l'utilisteur (à l'aide du clavier/souris)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if pygame.mouse.get_pressed()[0]:
                #print("appuyé")
                pygame.draw.line(self.screen, (255, 255, 255), (0, 0), (200, 200), 4)
            if event.type == pygame.MOUSEBUTTONUP:
                self.player.velocity[0] = - (self.player.rect.centerx - pygame.mouse.get_pos()[0])/5
                self.player.velocity[1] = - (self.player.rect.centery - pygame.mouse.get_pos()[1])/5

        keys = pygame.key.get_pressed()
        '''if keys[pygame.K_LEFT]:
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
            self.player.velocity[1] = 0'''

        if pygame.mouse.get_pressed()[0]:
            pygame.draw.line(screen, (255,255,255), (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]), (self.player.rect.x,self.player.rect.y))

    def update(self):
        if self.star.area.colliderect(self.player.rect):
            self.star.move()
        self.player.move()
        #gravité
        self.player.velocity[1] += 0.05 * 9.81

    def display(self):
        self.screen.fill("black")
        self.star.draw(self.screen)
        self.player.draw(self.screen)
        pygame.display.flip()
        self.player.update_health_bar(self.screen)
        
    def run(self):
        while self.running:
            self.display()
            self.handling_events()
            self.star.move()
            self.update()
            self.clock.tick(60)



pygame.init()
screen = pygame.display.set_mode((1080, 720))
##x1 = aleatoire(1080,720)[0]
##y1 = aleatoire(1080,720)[1]
game = Game(screen)
game.run()  
Player.update_health_bar(screen)


pygame.quit()

