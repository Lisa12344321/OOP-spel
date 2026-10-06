import pygame
from random import choice
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500

class Sprite(pygame.sprite.Sprite):
    def __init__(self, groups, image, pos, color):
        super().__init__(groups)
        self.image = image
        self.color = color
        self.image.fill(self.color)
        self.rect = self.image.get_frect(center = pos)

    def update(self):
        self.image.fill(self.color)

class Player():
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def check_balance(self, amount):
        pass

    def increase_balance(self, amount):
        self.__balance += amount


class SlotMachine():
    def __init__(self, symbol_sprites, player):
        self.symbol_sprites = symbol_sprites
        self.player = player
        self.symbols = [(5, "green"), (10, "yellow"), (15, "blue"), (20, "red")]
        self.result = []
        self.amount = 0


    def spin(self):
        for symbol in self.symbol_sprites:
            symbol.kill()

        self.result = []
        for i in range(3):
            self.result.append(choice(self.symbols))
        print(self.result)
        self.show_result()
        self.get_result()
        

    def get_result(self):
        if self.result[0] == self.result[1] == self.result[2]:
            self.amount = 0
            for symbol in self.symbol_sprites:
                self.amount += symbol.get_value()
            self.amount *= 10


        elif self.result[0] == self.result[1]:
            pass
        elif self.result[0] == self.result[2]:
            pass
        elif self.result[1] == self.result[2]:
            pass
        else:
            print("inget")

        self.player.increase_balance(self.amount)
        

    def show_result(self):
        x = WINDOW_WIDTH / 3
        for symbol in self.result:
            Symbol(self.symbol_sprites, pygame.Surface((50, 50)), (x, 100), symbol[1], symbol[0])
            x += 100

class Symbol(Sprite):
    def __init__(self, groups, image, pos, color, value):
        super().__init__(groups, image, pos, color)
        self.__value = value

    def get_value(self):
        return self.__value
        
