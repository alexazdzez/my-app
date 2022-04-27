from builtins import property

import pygame

import projectile
import animation


class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.health_base = 100
        self.max_health = 1000000
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 500
        self.rect.y = 500

    def regen(self):
        self.health += 10

    def regen_piege(self):
        self.health -= 50
        print("piège")

    def boom(self):
        for i in range(200, 201):
            self.lauch_projectile()
        self.health *= 50
        print("boom bravo")



    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else:
            self.game.game_over()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.health, 5])
        pygame.draw.rect(surface, (67, 223, 41), [self.rect.x + 50, self.rect.y + 20, self.health, 5])

    def lauch_projectile(self):
        self.start_animation()
        self.all_projectiles.add(projectile.Projectile(self))
        self.game.sound_manager.play('tir')


    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity


    def move_left(self):
        self.rect.x -= self.velocity