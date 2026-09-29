import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, groups, image, pos):
        super().__init__(groups)
        self.image = image
        self.image.fill("green")
        self.rect = self.image.get_frect(center = pos)
