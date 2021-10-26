import pygame


class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load("ball.png")
        self.image
        self.rect = self.image.get_rect(x=x, y=y)
        self.speed = 1
        self.velocity = [0, 0]

    def move(self):
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
        screen.blit(self.image, self.rect)


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()
        self.player = Player(200, 200)
        self.area = pygame.Rect(150, 80, 50, 50)
        self.area_color = "red"

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if pygame.mouse.get_pressed()[0]:
                print("appuyé")
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
        self.player.move()
        if self.area.colliderect(self.player.rect):
            self.area_color = "green"
        else:
            self.area_color = "red"

        #gravité
        self.player.velocity[1] += 0.05 * 9.81

    def display(self):
        self.screen.fill("black")
        pygame.draw.rect(self.screen, self.area_color, self.area)
        self.player.draw(self.screen)
        pygame.display.flip()

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

pygame.quit()
