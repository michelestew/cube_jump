import pygame as pg
from config import *
from sprites import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((width,height))
        pg.display.set_caption("cube_jump")

        self.clock = pg.time.Clock()
        self.running = True


    def new(self):
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player()
        self.all_sprites.add(self.player)
        self.plat1 = Platform(0, height - 40, width, 40)
        self.all_sprites.add(self.plat1)
        self.platforms.add(self.plat1)

        self.run()


    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()


    def update(self):
        self.all_sprites.update()
        hits= pg.sprite.spritecollide(self.player, self.platforms, False)
        self.player.isHitting = False
        if hits:
            self.player.vy = 0
            self.player.pos = hits[0].rect.top + 1
            self.player.isHitting = True
        if self.player.rect.y > height:
            self.player.rect.y = 0
            self.player.rect.center = (width / 2, height / 2)
            self.player.vy = 0
            self.player.vx = 0
            self.player.rect.x = self.plat1.rect.x + 235


    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    self.player.jump()


    def draw(self):
        self.screen.fill(black)

        offsetX = -self.player.rect.x + (width/2) -(15)

        self.player.rect.x += offsetX
        self.plat1.rect.x += offsetX


        self.all_sprites.draw(self.screen)
        pg.display.flip()


g=Game()
while g.running:
    g.new()


pg.quit()
