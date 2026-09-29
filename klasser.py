import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, groups, image, pos):
        super().__init__(groups)
        self.image = image
        self.image.fill("green")
        self.rect = self.image.get_frect(center = pos)

class SlotMachine():
    def __init__(self, slots):
        self.slots = slots

    def spin(self):
        print("ja")

    def get_result(self):
        pass

    def show_result(self):
        pass

class Symbol(Sprite):
    def __init__(self, groups, image, pos, value):
        super().__init__(groups, image, pos)
        self.__value = value

    def get_value(self):
        return self.__value
