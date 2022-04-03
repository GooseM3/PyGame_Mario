import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        #self.image.fill('red')
        imag1 = pygame.image.load("images/mario.png")
        self.image = pygame.transform.scale(imag1, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
        #movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 10
        self.gravity = 0.6
        self.jump_speed = -16
    def get_intput(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            imag1 = pygame.image.load("images/mario.png")
            self.image = pygame.transform.scale(imag1, (64, 64))
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            image1 = pygame.transform.flip(pygame.image.load("images/mario.png"), True, False)
            self.image = pygame.transform.scale(image1, (64, 64))
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            self.jump()
            imag1 = pygame.image.load("images/jump.png")
            self.image = pygame.transform.scale(imag1, (64, 64))
        elif keys[pygame.K_UP]:
            self.jump()
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    def jump(self):
        self.direction.y = self.jump_speed
    def update(self):
        self.get_intput()
        self.apply_gravity()