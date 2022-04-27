import game

class step:
    def __init__(self):
        self.game = game
        self.vague = 1

    def spawn_five_mummy(self):
        self.game.spawn_monster(self.game.monster.Mummy)
        self.game.spawn_monster(self.game.monster.Mummy)
        self.game.spawn_monster(self.game.monster.Mummy)
        self.game.spawn_monster(self.game.monster.Mummy)
        self.game.spawn_monster(self.game.monster.Mummy)

    def spawn_ten_mummy(self):
        self.game.spawn_monster(self.game.monster.Mummy)
        self.game.spawn_monster(self.game.monster.Mummy)
        self.game.spawn_monster(self.game.monster.Mummy)
        self.game.spawn_monster(self.game.monster.Mummy)
        self.game.spawn_monster(self.game.monster.Mummy)
        self.game.spawn_monster(self.game.monster.Mummy)
        self.game.spawn_monster(self.game.monster.Mummy)
        self.game.spawn_monster(self.game.monster.Mummy)
        self.game.spawn_monster(self.game.monster.Mummy)
        self.game.spawn_monster(self.game.monster.Mummy)

    def final_step(self):
        print("boss")
        self.spawn_ten_mummy()
        self.game.spawn_monster(self.game.monster.Alien)
        self.game.spawn_monster(self.game.monster.Alien)
        self.game.spawn_monster(self.game.monster.Alien)

    def new_step(self, add_vague_for_new_step=0):
        if self.vague == 2:
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Alien)
            self.vague += add_vague_for_new_step
        if self.vague == 3:
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Alien)
            self.vague += add_vague_for_new_step
        if self.vague == 4:
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Alien)
            self.vague += add_vague_for_new_step
        if self.vague == 5:
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Alien)
            self.game.spawn_monster(self.game.monster.Alien)
            self.vague += add_vague_for_new_step
        if self.vague == 6:
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Alien)
            self.game.spawn_monster(self.game.monster.Alien)
            self.vague += add_vague_for_new_step
        if self.vague == 7:
            self.spawn_five_mummy()
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Alien)
            self.game.spawn_monster(self.game.monster.Alien)
            self.vague += add_vague_for_new_step
        if self.vague == 8:
            self.spawn_five_mummy()
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Alien)
            self.game.spawn_monster(self.game.monster.Alien)
            self.vague += add_vague_for_new_step
        if self.vague == 9:
            self.game.spawn_monster(self.game.monster.Mummy)
            self.game.spawn_monster(self.game.monster.Alien)
            self.vague += add_vague_for_new_step
        if self.vague == 10:
            self.spawn_ten_mummy()
            self.game.spawn_monster(self.game.monster.Alien)
            self.vague += add_vague_for_new_step
        if self.vague == 11:
            self.final_step()
            self.vague += add_vague_for_new_step
        if self.vague <= 12:
            self.vague = 1
