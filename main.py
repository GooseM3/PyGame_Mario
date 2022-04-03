import pygame
import sys
from settings import *
from Dashboard import Dashboard
from Level import Level
from pygame import mixer
bg = pygame.image.load("images/level_bg1.jpg")
# = pygame.image.load("images/bg.png")
bg = pygame.transform.scale(bg,(screen_width,screen_height))
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
dashboard = Dashboard("images/font.png", 8, screen)
mixer.music.load("images/main_theme.ogg")
mixer.music.set_volume(.06)
mixer.music.play(-1)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill((52, 186, 235))
    screen.blit(bg, (0,0))
    level.run()
    dashboard.update()
    pygame.display.update()
    clock.tick(60)

