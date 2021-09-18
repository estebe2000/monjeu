import pygame


# definir une classe animation

class AnimateSprite(pygame.sprite.Sprite):

    # definir les init
    def __init__(self, sprite_name):
        super().__init__()
        self.sprite_sheet = pygame.image.load(f'./images/{sprite_name}.png')
        self.image = self.get_image(0, 0)
        self.current_image = 0
        self.current_image_count = 0
        self.current_image_speed = 20

    # defirnir une methode pour animer le sprite
    def animate(self, sprite_name, direction):
        self.images = load_animation_images(self, sprite_name).get(direction)

        self.current_image_count += self.current_image_speed

        if self.current_image_count >= 100:

            # passer a l'image suivante
            self.current_image += 1
            self.current_image_count = 0

        # verifier si fin animation
        if self.current_image >= 3:
            self.current_image = 0
            pas = pygame.mixer.Sound('./sounds/pasp.wav')
            pas.play(1)
        # modifier l'image de l'animation
        self.image = self.images[self.current_image]
        # return self.image

    def get_image(self, X, Y):
        image = pygame.Surface([32, 32])
        image.blit(self.sprite_sheet, (0, 0), (X, Y, 32, 32))
        return image

# definir une fonction de chargement des images
def load_animation_images(self, sprite_name):
    images_down = []
    images_up = []
    images_left = []
    images_right = []
    images = []
    for num in range (0,3):
        images_down.append(self.get_image(num * 32, 0))
        images_up.append(self.get_image(num * 32, 96))
        images_left.append(self.get_image(num * 32, 32))
        images_right.append(self.get_image(num * 32, 64))
    images.append(images_down)
    images.append(images_up)
    images.append(images_left)
    images.append(images_right)
    # renvoyer les listes d'images
    animations = {
        'down': images_down,
        'up': images_up,
        'left': images_left,
        'right': images_right
    }
    return animations

