import pygame
from random import choice, randint
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
    def __init__(self, symbol_sprites, player, font, text_sprites, big_font):
        self.text_sprites = text_sprites
        self.symbol_sprites = symbol_sprites
        self.font = font
        self.big_font = big_font
        self.player = player
        self.symbol_types = [Symbol1, Symbol2, Symbol3, Symbol4]
        self.symbol_group = []
        self.result = []
        self.amount = 0
        self.profit_text = None



    def spin(self, user_text, dt):
        bet = int(user_text)
        for symbol in self.symbol_sprites:
            symbol.kill()

        self.result = []
        for i in range(3):
            self.result.append(choice(self.symbol_types))

        self.show_result()
        self.get_result(bet, dt)


    def get_result(self, bet, dt):
        self.amount = 0
        self.symbol_group = []
        for symbol in self.symbol_sprites:
            self.symbol_group.append(symbol)

        if type(self.symbol_group[0]) == type(self.symbol_group[1]) == type(self.symbol_group[2]):

            if self.profit_text in self.text_sprites:
                self.text_sprites.remove(self.profit_text)
            
            self.amount = bet * self.symbol_group[0].get_value()

            self.profit_text = Text(self.big_font, f"{bet} x {self.symbol_group[0].get_value()} $", True, "green", (WINDOW_WIDTH/2, 80), self.text_sprites)
            self.profit_text.timer = True
            self.text_sprites.append(self.profit_text)
        
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
        self.text(bet, dt)

    def text(self, bet, dt):
        if self.amount > bet:
            text = f"+{int(self.amount)} $"
            color = "green"
        else:
            text = f"{int(self.amount)} $"
            color = "white"

        amount_text = Text(self.font, text, True, color, (randint(30, WINDOW_WIDTH -30), WINDOW_HEIGHT - 30), self.text_sprites)
        self.text_sprites.append(amount_text)
        amount_text.can_move = True



    def show_result(self):
        x = WINDOW_WIDTH / 3
        for symbol_type in self.result:
            symbol_type(self.symbol_sprites, pygame.Surface((80, 110)), (x, 233), self.get_color(symbol_type))
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


class Text():
    def __init__(self, font, text, antialias, color, pos, text_sprites):
        self.screen = pygame.display.get_surface()
        self.text_sprites = text_sprites

        self.font = font
        self.text = text
        self.antialias = antialias
        self.color = color
        self.pos = pos

        self.text_surf = font.render(self.text, self.antialias, self.color)
        self.rect = self.text_surf.get_frect(center = self.pos)

        self.can_move = False
        self.timer = None
        self.start_time = pygame.time.get_ticks() / 1000
        self.y = randint(350, 450)

    def move(self, dt):
        if self.rect.centery >= self.y:
            self.rect.centery -= 50 * dt
        else:
            self.text_sprites.remove(self)

    def timer_alive(self):
        timer = pygame.time.get_ticks() / 1000
        time_alive = 3
        if (timer - self.start_time) > time_alive:
            self.text_sprites.remove(self)

    def update_text(self, text):
        self.text_surf = self.font.render(text, self.antialias, self.color)
        

    def draw(self, dt):
        self.screen.blit(self.text_surf, self.rect)

        if self.can_move:
            self.move(dt)

        if self.timer:
            self.timer_alive()


        