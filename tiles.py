import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        #self.image = pygame.Surface((size,size))
        #self.image.fill("grey")
        imag1 = pygame.image.load("images/Ground_Brick.png")
        self.image = pygame.transform.scale(imag1, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
    def update(self,x_shift):
        self.rect.x += x_shift
class Brick(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        imag1 = pygame.image.load("images/Red_Brick.png")
        self.image = pygame.transform.scale(imag1, (64, 64))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift
class Goomba(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        #self.image.fill("red")
        imag1 = pygame.image.load("images/Goomba.png")
        self.image = pygame.transform.scale(imag1, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
    def update(self,x_shift):
        self.rect.x += x_shift
class Koopa(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        #self.image.fill("red")
        imag1 = pygame.image.load("images/Koopa.png")
        self.image = pygame.transform.scale(imag1, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
    def update(self,x_shift):
        self.rect.x += x_shift
class Red(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        imag1 = pygame.image.load("images/Item_Brick.png")
        self.image = pygame.transform.scale(imag1, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
    def update(self,x_shift):
        self.rect.x += x_shift
class Stair(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        imag1 = pygame.image.load("images/Stair_Brick.png")
        self.image = pygame.transform.scale(imag1, (64, 64))
        self.rect = self.image.get_rect(topleft = pos)
    def update(self,x_shift):
        self.rect.x += x_shift
        #images/Stair_Brick.png
class Sky(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        imag1 = pygame.image.load("images/Invisible_Block.png")
        self.image = pygame.transform.scale(imag1, (64, 64))
        #self.rect = self.image.get_rect(topleft = pos)
    #def update(self,x_shift):
        #self.rect.x += x_shift