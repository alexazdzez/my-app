import pygame
import random
import game
import monster


class Comet(pygame.sprite.Sprite):
    def __init__(self, comet_event, game):
        super().__init__()
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.velocity = random.randint(1, 3)
        self.comet_event = comet_event
        self.game = game


    def remove(self):
        self.comet_event.all_comets.remove(self)
        self.comet_event.game.sound_manager.play('meteorite')
        if len(self.comet_event.all_comets) == 0:
            print("fini")
            self.comet_event.reset_percent()
            self.comet_event.fall_mode = False
            self.comet_event.game.add_score(103)
            self.comet_event.game.spawn_monster(monster.Mummy)
            self.comet_event.game.spawn_monster(monster.Mummy)
            self.comet_event.game.spawn_monster(monster.Alien)


    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 500:
            print("une comet a touché le sol")
            self.remove()

            if len(self.comet_event.all_comets) == 0:
                print("fini")
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(
                self, self.comet_event.game.all_player
        ):
            print("une comet a touché le joueur")
            self.remove()
            self.comet_event.game.player.damage(20)