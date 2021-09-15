import pygame
import animation

class Player(animation.AnimateSprite):
    def __init__(self, x, y, mob_name):
        super().__init__(mob_name)
        self.mob = mob_name
        self.image.set_colorkey([255, 255, 255])
        self.rect = self.image.get_rect()
        self.position = [x, y]
        self.images = {
            'down': self.get_image(0, 0),
            'up': self.get_image(0, 96),
            'left': self.get_image(0, 32),
            'right': self.get_image(0, 64)
        }
        self.feet = pygame.Rect(0, 0, self.rect.width * 0.5, 12)
        self.old_position = self.position.copy()
        self.speed = 5

    def sav_location(self): self.old_position = self.position.copy()


    def change_animation(self, name):
        self.animate(self.mob,name)
        self.image.set_colorkey([255, 255, 255])

    def move_right(self):
        self.position[0] += self.speed


    def move_left(self):
        self.position[0] -= self.speed


    def move_up(self):
        self.position[1] -= self.speed


    def move_down(self):
        self.position[1] += self.speed


    def update(self):
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

    def move_back(self):
        self.position = self.old_position
        self.rect.topleft = self.position
        self.feet.midbottom = self.rect.midbottom

