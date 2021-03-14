#!/usr/bin/env python3
import os,sys
import pygame as pg #lazy but responsible (avoid namespace flooding)
from pygame.locals import *
all_sprites = pg.sprite.Group()
class Slap:
    def __init__(self,rect):
        self.rect = pg.Rect(rect)
        self.click = False
        self.image = pg.image.load('muhand.jpeg')
    
    def update(self,surface):
        if self.click:
            self.rect.center = pg.mouse.get_pos()
        surface.blit(self.image,self.rect)
##################################################
class Munky:
    def __init__(self,rect):
        # self.rect = pg.Rect(rect)
        pg.sprite.Sprite.__init__(self)
        self.click = False
        self.image = pg.image.load('yeehaw.jpeg')
        self.rect = self.image.get_rect(x=0, y=0)

    def update(self,surface):
        if self.click:
            self.rect.center = pg.mouse.get_pos()
        surface.blit(self.image,self.rect)
#######################################################33
    
def main(Surface,Slap,Munky):
    game_event_loop(Slap)
    Surface.fill(0)
    Slap.update(Surface)
    Munky.update(Surface)

############################
def game_event_loop(Slap):
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if Slap.rect.collidepoint(event.pos):
                Slap.click = True
        elif event.type == pg.MOUSEBUTTONUP:
            Slap.click = False
        elif event.type == pg.QUIT:
            pg.quit(); sys.exit()
##########################33
if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((1980,1020))
    MyClock = pg.time.Clock()
    MySlap = Slap((0,0,150,150)) # left top width height
    MyMonkay = Munky((0,0,150, 150))
    MySlap.rect.midright = Screen.get_rect().midright=(1300, 610) # Start position width, height
    MyMonkay.rect.midleft = Screen.get_rect().midleft=(200, 510)
    while 1:
        main(Screen,MySlap, MyMonkay)
        #main(Screen,MyMonkay)
        pg.display.update()
        MyClock.tick(60)
##################################
def is_collided_with(self, sprite):
    return self.rect.collidirect(sprite.rect)