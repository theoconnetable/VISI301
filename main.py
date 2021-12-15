import pygame, random
from fonctions import aleatoire
from fonctions import newhighscore

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
        self.dt = 0.2
        self.masse = 1

        ##########################################################################-----Ajout commentaires

    def move(self):
        ##Mouvement du joueur
        ##########################################################################-----Ajout commentaires
        self.force[1] = self.masse * 9.81

        self.vitesse = [(self.dt/self.masse)*self.force[0]+self.vitesse[0], (self.dt/self.masse)*self.force[1]+self.vitesse[1]]
        #print ("pos : ", self.position, "vitesse : ", self.vitesse, "force : ", self.force)
        self.rect.move_ip(self.dt * self.vitesse[0], self.dt * self.vitesse[1])
        if self.rect.left < 0:  #bord gauche
            self.vitesse[0] = - 0.5 * self.vitesse[0]
            self.rect.left = 0
        if  self.rect.right > screen.get_width():   #bord droit
            self.vitesse[0] = - 0.5 * self.vitesse[0]
            self.rect.right = screen.get_width()
        if self.rect.top < 100:   #bord haut
            self.rect.top = 100

    def set_time (self, time):
        self.dt = time

    def plafond (self) :
        res = False
        if self.rect.top <= 100:
            res = True
        return res

    def sol (self) :
        res = False
        if self.rect.bottom > screen.get_height():
            res = True
        return res

    def draw(self, screen):
        ##Affichage du joueur
        screen.blit(self.image, self.rect)

class Particle:
    ###############################
    def __init__(self):
        self.particles = []
    def emit(self):
        if self.particles:
            self.delete_particles()
            for particle in self.particles:
                particle[0][1] += particle[2][0]
                particle[0][0] += particle[2][1]
                particle[1] -= 0.2
                pygame.draw.circle(screen,pygame.Color((255,0,0)),particle[0], int(particle[1]))

    def add_particles(self,x,y):
        pos_x = x
        pos_y = y
        radius = 10
        direction_x = random.randint(0,2)
        direction_y = random.randint(0,2)
        particle_circle = [[pos_x,pos_y],radius,[direction_x,direction_y]]
        self.particles.append(particle_circle)

    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        self.particles = particle_copy



    
class health_bar :
    ##La barre de vie
    def __init__(self, screen, health):
        self.screen = screen
        self.health = health
        self.max_health = health
        self.background = Background()
        self.end_play = pygame.image.load("Image1.png")
        self.end_play_rect = self.end_play.get_rect()
        self.end_play_rect.x = 25
        self.end_play_rect.y = 400 
        self.play_button = pygame.image.load("Jouer.png")
        self.play_button = pygame.transform.scale(self.play_button,(350,150))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = 25
        self.play_button_rect.y = 400
        self.baisse = 0.1
        self.baisseOk = False

    def draw(self, health):
        ##Couleur de la barre de vie + barre d'arrière plan
        #self.screen = screen 
        bar_color = (255,0,0)
        back_bar_color = (127,127,127)

        ##position de la barre de vie
        bar_position = pygame.Rect(20,20,self.health,20)
        back_bar_position = pygame.Rect(20,20,self.max_health,20)

        ##dessiner la barre de vie
        pygame.draw.rect(self.screen, back_bar_color, back_bar_position)
        pygame.draw.rect(self.screen, bar_color, bar_position)
        #print(bar_color,bar_position)

    def augmente (self):
        if self.health < 170 :
            self.health = self.health + 15
        else :
            self.health = 200
            
    def decrease(self, is_playing):
        self.health = self.health - self.baisse
        if self.health < 0 :

            self.health = 0

    def augment_baisse(self):
        self.baisse += 0.1
        self.baisseOk = False

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
#class Bonus :
 #   def __init__(self,x2,y2):
  #      self.image_sablier = pygame.image.load("sablier.png")
   #     self.sablier_rect = self.image_sablier.get_rect(x=x2,y=y2)
    #    self.pos =[x2, y2]
    
    #def draw(self,screen):
     #   screen.blit(self.image_sablier, self.sablier_rect)
        
class Score:
    ##Le score
    def __init__(self, valscore, screen):
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.valscore = valscore

    def augmente (self):
        self.valscore = self.valscore + 1

    def draw(self, screen, menu):
        if menu :
            x = screen.get_width() // 2
            y = 135
        else :
            x = 300
            y = 30

        self.scorerendered = self.font.render('score: ' + str(self.valscore), True, (250,250,250))
        self.scorerendered_rect = self.scorerendered.get_rect(center=(x, y))

        pygame.draw.rect(screen, (200, 200, 200, 50), self.scorerendered.get_rect(center=(x,y)))

        screen.blit(self.scorerendered, self.scorerendered_rect)

class Highscore:
    ##Le score
    def __init__(self, valmeilscore, screen):
        self.font = pygame.font.Font('freesansbold.ttf', 22)
        self.valmeilscore = valmeilscore

    def update (self, valscore):
        self.valscore = valscore
        #print(self.valscore)
        self.valmeilscore = newhighscore(self.valscore,"joueur1")
        #print(self.valmeilscore)

    def draw(self, screen):
        self.scorerendered = self.font.render('meilleur score: ' + str(self.valmeilscore), True, (20,20,20) )
        screen.blit(self.scorerendered, (20, 45))
        
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

class Home :
    # Ecran d'acceuil 
    def display(self,is_score):
        self.background.draw(self.screen)
        screen.blit(self.play_button, self.play_button_rect)
        screen.blit(self.banner, (0, 200))
        if is_score:
            self.score.draw(self.screen, True)
            self.font = pygame.font.Font('freesansbold.ttf', 60)
            self.end = self.font.render('GAME OVER', True, (0, 0, 0))
            self.end_rect = self.end.get_rect(center=(screen.get_width()//2, 75))
            screen.blit(self.end, self.end_rect)
        pygame.display.flip()
        self.handling_events()


class Game:
    ##Le jeu

    def __init__(self, screen):
        ##Initialisation du jouer : x,y : entiers (position du joueur en(x,y))
        self.screen = screen
        self.running = True
        # Définir si le jeu à commencé
        self.is_playing = False
        self.gameover = False
        self.play_button = pygame.image.load("Jouer.png")
        self.play_button = pygame.transform.scale(self.play_button,(350,150))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = 25
        self.play_button_rect.y = 300
        self.banner = pygame.image.load("banner.png")
        self.banner = pygame.transform.scale(self.banner,(400,100))
        self.clock = pygame.time.Clock()
        ##########################################################################-----Ajout commentaires
        self.background = Background()
        self.health = 200
        self.health_bar = health_bar(screen, self.health)
        self.player = Player(200, 650)
        self.star1 = Star(aleatoire(screen.get_width(),self.screen.get_height())[0],aleatoire(screen.get_width(),self.screen.get_height())[1])
        self.star2 = Star(aleatoire(screen.get_width(),self.screen.get_height())[0],aleatoire(screen.get_width(),self.screen.get_height())[1])
        #self.sablier = Bonus(aleatoire(screen.get_width(),self.screen.get_height())[0],aleatoire(screen.get_width(),self.screen.get_height())[1])
        ##On definit les positions initiales du joueur et de l'étoile
        #self.health_max = 200
        self.valscore = 0
        self.score = Score(self.valscore, screen)
        self.meilscore = newhighscore(self.valscore,"joueur1")
        self.highscore = Highscore(self.meilscore, screen)
        self.particleball = Particle()

    def restart (self, screen):
        #réinitialisation de la partie
        self.running = True
        # Définir si le jeu à commencé
        self.play_button = pygame.image.load("Jouer.png")
        self.play_button = pygame.transform.scale(self.play_button, (350, 150))
        self.play_button_rect = self.play_button.get_rect()
        self.play_button_rect.x = 25
        self.play_button_rect.y = 300
        self.banner = pygame.image.load("banner.png")
        self.banner = pygame.transform.scale(self.banner, (400, 100))
        self.clock = pygame.time.Clock()
        ##########################################################################-----Ajout commentaires
        self.background = Background()
        self.health = 200
        self.health_bar = health_bar(screen, self.health)
        self.player = Player(200, 650)
        self.star1 = Star(aleatoire(screen.get_width(), self.screen.get_height())[0],
                          aleatoire(screen.get_width(), self.screen.get_height())[1])
        self.star2 = Star(aleatoire(screen.get_width(), self.screen.get_height())[0],
                          aleatoire(screen.get_width(), self.screen.get_height())[1])
        ##On definit les positions initiales du joueur et de l'étoile
        # self.health_max = 200
        self.valscore = 0
        self.score = Score(self.valscore, screen)
        ###############################################################
        self.particleball = Particle()

    def handling_events(self):
        ##Effectue les actions entrées par l'utilisteur (à l'aide du clavier/souris)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.player.set_time(0.1)
                #print ("coucou")

                
            if event.type == pygame.MOUSEBUTTONUP:
                vitesseX = - (self.player.rect.centerx - pygame.mouse.get_pos()[0])/3
                vitesseY = - (self.player.rect.centery - pygame.mouse.get_pos()[1])/3
                if (vitesseX < -100):
                    vitesseX = -100
                if (vitesseY < -100):
                    vitesseY = -100
                self.player.vitesse[0] = vitesseX
                self.player.vitesse[1] = vitesseY
                self.player.set_time(0.2)
                self.health_bar.health -= 15

                # Souris en collision avec le bouton
                if (self.play_button_rect.collidepoint(event.pos) and not (self.is_playing)):
                    self.is_playing = True
                    self.restart(self.screen)

        keys = pygame.key.get_pressed()

    def update(self):
        if (self.star1.area.bottom > self.screen.get_height()):
            self.star1 = Star(aleatoire(screen.get_width() - self.star1.image2.get_width(), screen.get_height() // 2)[0], aleatoire(screen.get_width() - self.star1.image2.get_width(), screen.get_height() // 2)[1])
        if (self.star2.area.bottom > self.screen.get_height()):
            self.star2 = Star(aleatoire(screen.get_width() - self.star2.image2.get_width(), screen.get_height() // 2)[0], aleatoire(screen.get_width() - self.star2.image2.get_width(), screen.get_height() // 2)[1])
        if (self.star1.area.colliderect(self.player.rect)):
            self.star1 = Star(aleatoire(screen.get_width() - self.star1.image2.get_width(), screen.get_height()//2)[0],aleatoire(screen.get_width() - self.star1.image2.get_width(), screen.get_height()//2)[1])
            self.health_bar.augmente()
            self.score.augmente()
            ###################
            self.valscore = self.valscore + 1
            self.highscore.update(self.valscore)
            ####################
        if (self.star2.area.colliderect(self.player.rect)):
            self.star2 = Star(aleatoire(screen.get_width() - self.star1.image2.get_width(), screen.get_height()//2)[0],aleatoire(screen.get_width() - self.star1.image2.get_width(), screen.get_height()//2)[1])
            self.health_bar.augmente()
            self.score.augmente()
             ######################
            self.valscore = self.valscore + 1
            self.highscore.update(self.valscore)
            ########################
        else :
            self.health_bar.decrease(self.is_playing)
            self.particleball.add_particles(self.player.rect.centerx,self.player.rect.centery) #---------------------------------

        # Augmentation du score en fonction du score
        if (self.score.valscore % 5 == 0 and self.health_bar.baisseOk):
            self.health_bar.augment_baisse()
            #Bonus.draw(self, self.screen)
        if (self.score.valscore % 20 == 1):
            self.health_bar.baisseOk = True

        #print ("star 1 ",self.star1.pos, "star 2 ",self.star2.pos, "width : ", self.star2.area.bottom, self.screen.get_height())
        self.player.move()
        #print (self.player.plafond())
        #print (self.player.vitesse[1])
        if (self.player.plafond()):
            self.star1.move(-self.player.vitesse[1])
            self.star2.move(-self.player.vitesse[1])
            self.background.move(-self.player.vitesse[1])
        if (self.player.sol()):
            #le joueur tombe tout en bas
            self.is_playing = False
            self.gameover = True
        if self.health_bar.health == 0 :
            self.is_playing = False
            self.gameover = True


    def display(self):
        #self.screen.fill("black")
        self.background.draw (self.screen)
        self.star1.draw(self.screen)
        self.star2.draw(self.screen)
        self.player.draw(self.screen)
        self.health_bar.draw(self.health)
        self.highscore.draw(self.screen)
        self.score.draw(self.screen, False)
        self.health_bar.decrease(self.is_playing)
        self.particleball.emit()
        pygame.display.flip()

        #pygame.draw.rect(self.screen,(255,0,0),pygame.rect(100,100,100,100))
        #pygame.display.flip()
        

    def run(self):
        while self.running:
            #print (self.gameover)
            if self.is_playing :
                self.display()
                self.handling_events()
                self.update()
                self.clock.tick(60)
            else :
                if (self.gameover) :
                    Home.display(self,True)
                else :
                    Home.display(self,False)
                



pygame.init()
screen = pygame.display.set_mode((400, 720))
game = Game(screen)

game.run()


pygame.quit()

