import pygame
from player import Player
from monster import Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager


class Game:

    def __init__(self):
        self.is_playing = False
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.comet_event = CometFallEvent(self)
        self.all_monsters = pygame.sprite.Group()
        self.score = 0
        self.font = pygame.font.SysFont("assets/font_custom.ttf", 25)
        self.sound_manager = SoundManager()
        self.pressed = {}

    def add_score(self, amount=20):
        self.score += amount

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)
        print("            JEU               ")


    def close(self):
        running = False
        print("            JEU               ")
        print("            FERMER            ")
        print("Coder par mpxp(PyGame) en python.")
        print("minecraft 1.18.1 ip: inertiacreeps.net:21181")
        print("            FERMER            ")


    def game_over(self):

        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.player.health = self.player.health_base
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')

    def update(self, screen):

        score_text = self.font.render(f"Score : {self.score}", 1, (0, 200, 0))
        screen.blit(score_text, (20, 20))

        self.player.update_health_bar(screen)

        self.comet_event.update_bar(screen)

        screen.blit(self.player.image, self.player.rect)

        self.player.update_animation()

        for projectile in self.player.all_projectiles:
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        for comet in self.comet_event.all_comets:
            comet.fall()

        self.player.all_projectiles.draw(screen)

        self.all_monsters.draw(screen)

        self.comet_event.all_comets.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        if self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self, monster_name):
        self.all_monsters.add(monster_name.__call__(self))
        self.player.regen()

    def regen(self):
        self.player.regen()

    def regen_p(self):
        self.player.regen_piege()

    def boom(self):
        self.player.boom()
