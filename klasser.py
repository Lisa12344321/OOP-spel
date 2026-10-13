import pygame
from random import choice
from os.path import join
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500

class Sprite(pygame.sprite.Sprite):
    def __init__(self, groups, image, pos, color):
        super().__init__(groups)
        self.image = image
        self.color = color
        if self.color:
            self.image.fill(self.color)
        self.rect = self.image.get_frect(center = pos)

    def update(self):
        if self.color:
            self.image.fill(self.color)

class Player():
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def check_balance(self, user_text):
        bet = int(user_text)
        if 0 < bet <= self.__balance: return True
        else: return False

    def change_balance(self, amount):
        self.__balance += int(amount)
        self.__balance = max(0, self.__balance)


class SlotMachine():
    def __init__(self, symbol_sprites, player):
        self.symbol_sprites = symbol_sprites
        self.player = player
        self.symbol_types = [Symbol1, Symbol2, Symbol3, Symbol4]
        self.symbol_group = []
        self.result = []
        self.amount = 0



    def spin(self, user_text):
        bet = int(user_text)
        for symbol in self.symbol_sprites:
            symbol.kill()

        self.result = []
        for i in range(3):
            self.result.append(choice(self.symbol_types))

        self.show_result()
        self.get_result(bet)


    def get_result(self, bet):
        self.amount = 0
        self.symbol_group = []
        for symbol in self.symbol_sprites:
            self.symbol_group.append(symbol)

        if type(self.symbol_group[0]) == type(self.symbol_group[1]) == type(self.symbol_group[2]):
            self.amount = bet * self.symbol_group[0].get_value()    
        elif type(self.symbol_group[0]) == type(self.symbol_group[1]):
            if bet > 1: self.amount = -bet/2
            else: self.amount = -bet
        elif type(self.symbol_group[0]) == type(self.symbol_group[2]):
            if bet > 1: self.amount = -bet/2
            else: self.amount = -bet
        elif type(self.symbol_group[1]) == type(self.symbol_group[2]):
            if bet > 1: self.amount = -bet/2
            else: self.amount = -bet
        else:
            print("inget")
            self.amount = -bet

        self.player.change_balance(self.amount)


    def show_result(self):
        x = WINDOW_WIDTH / 3
        for symbol_type in self.result:
            symbol_type(self.symbol_sprites, pygame.Surface((50, 50)), (x, 100), self.get_color(symbol_type))
            x += 100


    def get_color(self, symbol_type):
        colors = {
            Symbol1: "green",
            Symbol2: "yellow",
            Symbol3: "blue",
            Symbol4: "red"
        }
        return colors[symbol_type]


class Symbol(Sprite):
    def __init__(self, groups, image, pos, color):
        super().__init__(groups, image, pos, color)

    def get_value(self):
        return 0


class Symbol1(Symbol):
    def get_value(self):
        return 2

class Symbol2(Symbol):
    def get_value(self):
        return 5

class Symbol3(Symbol):
    def get_value(self):
        return 10

class Symbol4(Symbol):
    def get_value(self):
        return 15