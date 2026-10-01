import pygame
from random import choice
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500

class Sprite(pygame.sprite.Sprite):
    def __init__(self, groups, image, pos, color):
        super().__init__(groups)
        self.image = image
        self.image.fill(color)
        self.rect = self.image.get_frect(center = pos)

class Player():
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def check_balance(self, amount):
        pass


class SlotMachine():
    def __init__(self, symbol_sprites):
        self.symbol_sprites = symbol_sprites
        self.symbols = [(1, "green"), (2, "yellow"), (3, "blue"), (4, "red")]
        self.result = []


    def spin(self):
        for symbol in self.symbol_sprites:
            symbol.kill()

        self.result = []
        for i in range(3):
            self.result.append(choice(self.symbols))
        print(self.result)
        self.show_result()
        

    def get_result(self):
        return self.result

    def show_result(self):
        x = WINDOW_WIDTH / 3 - 100
        for symbol in self.result:
            Symbol(self.symbol_sprites, pygame.Surface((50, 50)), (x, 100), symbol[1], symbol[0])
            x += 100

class Symbol(Sprite):
    def __init__(self, groups, image, pos, color, value):
        super().__init__(groups, image, pos, color)
        self.__value = value

    def get_value(self):
        return self.__value
        
