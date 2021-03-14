import pygame
import random
import os, sys
from pygame.locals import *
import pygame.font
from pygame import mixer
import time
from time import sleep, time


#WHITE = (255, 255, 255)
#GREEN = (20, 255, 140)
#BLACK = (0, 0, 0)
pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1980,1020))
pygame.display.set_caption('Beat Dat Monkay')
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((255,255,255))
# background.fill((0,0,0))

clock = pygame.time.Clock()

def load_image(name, colorkey=None):
    fullname = name #os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print('Cannot load image:', name)
        raise SystemExit(message)
    image = image.convert()
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0,0))
        image.set_colorkey(colorkey, pygame.RLEACCEL)
    return image, image.get_rect()

class Fist(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('hank.png', -1)
        self.rect.midright = 1700, 540
        self.speed = 0
        self.slapping = 0
    
    def update(self):
        pos = pygame.mouse.get_pos()
        self.rect.midtop = pos
        if self.slapping:
            self.rect.move_ip(0, 1)
    
    def slap(self, target):
        if not self.slapping:
            self.slapping = 1
            hitbox = self.rect.inflate(1,1)
            return hitbox.colliderect(target.rect)
            
    def unslap(self):
        self.slapping = 0



class Monkay(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('yeehaw.jpeg', -1)
        screen = pygame.display.get_surface()
        self.area = screen.get_rect()
        self.rect.midleft = 200, 540
        self.move = 9
        self.yeet = 0
        self.dizzy = 0
        self.state = self.image.get_rect()


    def slapped(self):
        if not self.dizzy:
            self.dizzy = 1
            self.original = self.image

    def move_the_monkey(self):
        # print(f'Move -- > {self.rect}')
        self.rect.move_ip(-1000, 0)
        font = pygame.font.Font(None, 100) # None can be a font file instead
        text = font.render("BEAT ME MORE SNAKE, MORE", 1, (0, 0, 0))
        background.blit(text, (0,0))
        # print(f'Rect -> {self.rect} and State -> {self.state}')


    def reset_the_monkey(self):
        # print(f'Reset -- > {self.rect}')
     
        self.rect.x = random.randrange(100,1000)
        self.rect.y = random.randrange(100,1000)

class Unit():
    def __init__(self):
        self.last = pygame.time.get_ticks()
        self.cooldown = 300
# if pygame.font:
#     font = pygame.font.Font(None, 36)
#     text = font.render("SLAP DAT MONKAY FOO", 1, (10,10,10))
#     textpos = text.get_rect(centerx=background.getwidth()/2)
#     background.blit(text, textpos)

screen.blit(background, (0,0))
pygame.display.flip()

fist = Fist()
monkay = Monkay()


allsprites = pygame.sprite.RenderPlain((fist, monkay))

# font = pygame.font.Font(None, 36) # None can be a font file instead
# text = font.render("MONKEY HAS BEEN YEETED", 1, (0, 0, 0))
# background.blit(text, (0,0))


last_time = time()

while True:
    clock.tick(60)
    for event in pygame.event.get():        
        if fist.rect.colliderect(monkay.rect):
            monkay.move_the_monkey()
            monkay.reset_the_monkey()
            


    allsprites.update() 

    screen.blit(background, (0,0))
    allsprites.draw(screen)
    pygame.display.flip()


















































