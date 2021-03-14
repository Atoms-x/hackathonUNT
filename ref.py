import pygame
import random
import os, sys
from pygame.locals import *


#WHITE = (255, 255, 255)
#GREEN = (20, 255, 140)
#BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1980,1020))
pygame.display.set_caption('Slap Dat Monkay')
#display_rect = display.get_rect()
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((125,125,125))


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
        self.image, self.rect = load_image('muhand.jpeg', -1)
        self.speed = 0
        self.punching = 0
    
    def update(self):
        pos = pygame.mouse.get_pos()
        # print(f'The position is -> {pos}.')
        self.rect.midtop = pos
        if self.punching:
            self.rect.move_ip(0, 1)
    
    def slap(self, target):
        if not self.punching:
            self.punching = 1
            hitbox = self.rect.inflate(1,1)
            return hitbox.collidrict(target.rect)
            
    def unslap(self):
        self.punching = 0

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

    def update(self):
        if self.dizzy:
            self._spin()
        else:
            self._walk()
    
    def _walk(self):
        newpos = self.rect.move((self.move, 0))
        if not self.area.contains(newpos):
            if self.rect.left < self.area.left or \
                    self.rect.right > self.area.right:
                self.move = -self.move
                newpos = self.rect.move((self.move, 0))
                self.image = pygame.transform.flip(self.image, 1, 0)
            self.rect = newpos
    
    def _spin(self):
        center = self.rect.center   
        self.yeet += 200
        if self.dizzy >= 360:
            self.dizzy = 0
            self.image = self.original
        else:
            rotate = pygame.transform.rotate
            self.image = rotate(self.original, self.dizzy)
        self.rect = self.image.get_rect(center=center)

    def punched(self):
        if not self.dizzy:
            self.dizzy = 1
            self.original = self.image

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

while True:
    clock.tick(30)
    allsprites.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            # print('YEEEEEEHAW')
            screen.blit(background, (0,0))
            # zx = mouse_position[0]
            # zy = mouse_position[1]
    screen.blit(background, (0,0))
    allsprites.draw(screen)
    pygame.display.flip()


















































