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
        self.acceleration = [0,0]
        self.vitesse = [0,0]
        self.position = [0,0]
        self.force = [0,0]
        self.masse = 5
        self.health = 100
        self.max_health = 100
        ##########################################################################-----Ajout commentaires

    def move(self):
        ##Mouvement du joueur
        ##########################################################################-----Ajout commentaires
        dt = 0.2
        self.force[1] = self.masse * 9.81

        self.vitesse = [(dt/self.masse)*self.force[0]+self.vitesse[0],(dt/self.masse)*self.force[1]+self.vitesse[1]]
        print ("pos : ", self.position, "vitesse : ", self.vitesse, "force : ", self.force)
        self.rect.move_ip(dt * self.vitesse[0], dt * self.vitesse[1])
        if self.rect.left < 0:
            self.vitesse[0] = 0
            self.rect.left = 0
        if  self.rect.right > screen.get_width():
            self.vitesse[0] = 0
            self.rect.right = screen.get_width()
        if self.rect.top < 0:
            self.vitesse[1] = 0
            self.rect.top = 0
        if  self.rect.bottom > screen.get_height():
            self.vitesse[1] = 0
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
                self.player.vitesse[0] = - (self.player.rect.centerx - pygame.mouse.get_pos()[0])/3
                self.player.vitesse[1] = - (self.player.rect.centery - pygame.mouse.get_pos()[1])/3

        keys = pygame.key.get_pressed()

        if pygame.mouse.get_pressed()[0]:
            pygame.draw.line(screen, (255,255,255), (pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1]), (self.player.rect.x,self.player.rect.y))

    def update(self):
        if self.star.area.colliderect(self.player.rect):
            self.star = star(aleatoire(1080,720)[0],aleatoire(1080,720)[1])  
        self.player.move()

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
            self.update()
            self.clock.tick(60)



pygame.init()
screen = pygame.display.set_mode((1080, 720))
game = Game(screen)
game.run()  
Player.update_health_bar(screen)


pygame.quit()

