import pygame as pg
from config import *



class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30,30))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.pos = self.rect.center
        self.vx = 0.0
        self.vy = 0.0
        self.ay = 20.0
        self.isHitting = False


    def jump(self):
        self.rect.y -= 1
        if self.isHitting:
            self.vy = -60


    def update(self):
        dt = 10.0/FPS
        self.vx = 0
        self.ay = 20
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.vx = -20.0
        if keys[pg.K_RIGHT]:
            self.vx = 30.0
        self.rect.x = self.rect.x + (self.vx * dt)
        self.vy += self.ay * dt
        self.rect.y += (self.vy * dt)



class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, width, height):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((width, height))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
