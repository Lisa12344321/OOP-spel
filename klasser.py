import pygame

class Sprite(pygame.sprite.Sprite):
    def __init__(self, groups, image, pos):
        super().__init__(groups)
        self.image = image
        self.image.fill("green")
        self.rect = self.image.get_frect(center = pos)

class Player():
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def check_balance(self, amount):
        pass

    


class SlotMachine():
    def __init__(self):
        pass

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
        
