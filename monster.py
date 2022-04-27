import random
import animation
import pygame

class Monster(animation.AnimateSprite):

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.2
        self.rect = self.image.get_rect()
        self.rect.x = 1200 + random.randint(0, 300)
        self.rect.y = 540 - offset
        self.start_animation()
        self.loot_amount = 1

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocité = random.randint(2, 3)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        self.health -= amount

        if self.health <= 0:
            self.game.add_score(self.loot_amount)
            self.rect.x = 1200 + random.randint(0, 300)
            self.velocité = self.default_speed
            self.game.player.health += 1
            if random.random() < 0.25:
                self.max_health += 5
            self.health = self.max_health

            if self.game.comet_event.is_full_loaded():
                self.game.all_monsters.remove(self)
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):

        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.health, 5])
        pygame.draw.rect(surface, (67, 223, 41), [self.rect.x + 10, self.rect.y - 20, self.health, 5])

    def forward(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocité
        else:
            self.game.player.damage(self.attack)

class Mummy(Monster):

    def __init__(self, game):
        super().__init__(game, 'mummy', (130, 130))
        self.set_speed(2)
        self.set_loot_amount(18)

class Alien(Monster):

    def __init__(self, game):
        super().__init__(game, 'alien', (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.5
        self.set_speed(0.01)
        self.set_loot_amount(41)