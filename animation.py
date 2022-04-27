import pygame

class AnimateSprite(pygame.sprite.Sprite):
    def __init__(self, name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = animation.get(name)
        self.annimation = False

    def start_animation(self):
        self.annimation = True

    def animate(self, loop=False):

        if self.annimation is True:
            if(self.current_image < 24):
                self.current_image += 1

                if self.current_image >= len(self.images):
                    self.current_image = 0

                self.image = self.images[self.current_image]
                self.image = pygame.transform.scale(self.image, self.size)

                if loop is False:
                    self.annimation = False
def load_animation_images(name):
    images = []
    path = f"assets/{name}/{name}"
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))
    return images
animation = {
    'mummy': load_animation_images('mummy'),
    'alien': load_animation_images('alien'),
    'player': load_animation_images('player')
}