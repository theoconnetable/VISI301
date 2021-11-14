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
        self.vitesse = [0,-100]
        self.position = [x,y]
        self.force = [0,0]
        self.masse = 5

        ##########################################################################-----Ajout commentaires

    def move(self):
        ##Mouvement du joueur
        ##########################################################################-----Ajout commentaires
        dt = 0.2
        self.force[1] = self.masse * 9.81

        self.vitesse = [(dt/self.masse)*self.force[0]+self.vitesse[0], (dt/self.masse)*self.force[1]+self.vitesse[1]]
        #print ("pos : ", self.position, "vitesse : ", self.vitesse, "force : ", self.force)
        self.rect.move_ip(dt * self.vitesse[0], dt * self.vitesse[1])
        if self.rect.left < 0:  #bord gauche
            self.vitesse[0] = - 0.5 * self.vitesse[0]
            self.rect.left = 0
        if  self.rect.right > screen.get_width():   #bord droit
            self.vitesse[0] = - 0.5 * self.vitesse[0]
            self.rect.right = screen.get_width()
        if self.rect.top < 100:   #bord haut
            self.rect.top = 100
        if  self.rect.bottom > screen.get_height(): #bord bas
            self.vitesse[1] = 0
            self.rect.bottom = screen.get_height()

    def plafond (self) :
        res = False
        if self.rect.top <= 100:
            res = True
        return res

    def draw(self, screen):
        ##Affichage du joueur
        screen.blit(self.image, self.rect)


class health_bar :
    ##La barre de vie 
    def __init__(self, screen, health):
        self.screen=screen
        self.max_health = 200
        
    def draw(self, health):
        ##Couleur de la barre de vie + barre d'arrière plan
        bar_color = (255,0,0) 
        back_bar_color = (127,127,127)
        
        ##position de la barre de vie 
        bar_position = pygame.Rect(20,20,health,20)
        back_bar_position = pygame.Rect(20,20,200,20)
        
        ##dessiner la barre de vie
        pygame.draw.rect(self.screen, back_bar_color, back_bar_position)
        pygame.draw.rect(self.screen, bar_color, bar_position)
        #print(bar_color,bar_position)


class Star:
    ##L'étoile
    def __init__(self,x1, y1):
         ##Initialisation du jouer : x,y : entiers (position du joueur en(x1,y1))
        self.image2 = pygame.image.load("star.png")
        self.area = self.image2.get_rect(x=x1,y=y1)
        self.pos = [x1, y1]
        ##L'affichage de l'étoile est définit par la variable 'image2'
        ##Sa position ainsi que "hitbox" sont définies par 'area'

    def move (self, x):
        self.area.move_ip(0,x)

    def draw(self, screen):
        screen.blit(self.image2, self.area) 


class Background:
    def __init__(self):
        self.image1 = pygame.image.load("fond-nuage.png")
        self.image2 = pygame.image.load("fond-nuage.png")
        self.rect1 = self.image1.get_rect(x=0,y=0)
        self.rect2 = self.image2.get_rect(x=0, y=-self.rect1.height)

    def draw(self, screen):
        screen.blit (self.image1, self.rect1)
        screen.blit (self.image2, self.rect2)

    def move (self, x):
        self.rect1.move_ip(0, x)
        self.rect2.move_ip(0, x)
        #print (self.rect1.top, self.rect1.bottom)
        if (self.rect1.top >= screen.get_height()):
            self.rect1.top = 0
            self.rect2.bottom = 0
    
class Game:
    ##Le jeu

    def __init__(self, screen):
        ##Initialisation du jouer : x,y : entiers (position du joueur en(x,y))
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        ##########################################################################-----Ajout commentaires
        self.background = Background()
        self.health_bar = health_bar(screen, health)
        self.player = Player(200, 700)
        self.star1 = Star(aleatoire(screen.get_width(),self.screen.get_height())[0],aleatoire(screen.get_width(),self.screen.get_height())[1])
        self.star2 = Star(aleatoire(screen.get_width(),self.screen.get_height())[0],aleatoire(screen.get_width(),self.screen.get_height())[1])
        ##On definit les positions initiales du joueur et de l'étoile
        self.health = health
        #self.health_max = 200
        
    def handling_events(self):
        ##Effectue les actions entrées par l'utilisteur (à l'aide du clavier/souris)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONUP:
                vitesseX = - (self.player.rect.centerx - pygame.mouse.get_pos()[0])/3
                vitesseY = - (self.player.rect.centery - pygame.mouse.get_pos()[1])/3
                if (vitesseX < -100):
                    vitesseX = -100
                if (vitesseY < -100):
                    vitesseY = -100
                self.player.vitesse[0] = vitesseX
                self.player.vitesse[1] = vitesseY

        keys = pygame.key.get_pressed()

    def update(self):
        if (self.star1.area.colliderect(self.player.rect) or (self.star1.area.bottom > self.screen.get_height())):
            self.star1 = Star(aleatoire(screen.get_width(),screen.get_height())[0],aleatoire(screen.get_width(),screen.get_height())[1])
            self.health = self.health +10
        if (self.star2.area.colliderect(self.player.rect) or (self.star2.area.bottom > self.screen.get_height())):
            self.star2 = Star(aleatoire(screen.get_width(),screen.get_height())[0],aleatoire(screen.get_width(),screen.get_height())[1])
            self.health = self.health + 10
        else :
            self.health = self.health - 0.5
            if self.health == 0 :
                pygame.quit()
        #print ("star 1 ",self.star1.pos, "star 2 ",self.star2.pos, "width : ", self.star2.area.bottom, self.screen.get_height())
        self.player.move()
        #print (self.player.plafond())
        #print (self.player.vitesse[1])
        if (self.player.plafond()):
            self.star1.move(-self.player.vitesse[1])
            self.star2.move(-self.player.vitesse[1])
            self.background.move(-self.player.vitesse[1])


    def display(self):
        #self.screen.fill("black")
        self.background.draw (self.screen)
        self.star1.draw(self.screen)
        self.star2.draw(self.screen)
        self.player.draw(self.screen)
        self.health_bar.draw(self.health)
        pygame.display.flip()
        
        #pygame.draw.rect(self.screen,(255,0,0),pygame.rect(100,100,100,100))
        #pygame.display.flip()
        
    def run(self):
        while self.running:
            self.display()
            self.handling_events()
            self.update()
            self.clock.tick(60)



pygame.init()
screen = pygame.display.set_mode((400, 720))
health = 200
game = Game(screen)
game.run()


pygame.quit()

