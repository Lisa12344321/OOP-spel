import pygame
from klasser import *

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Spel")
        self.clock = pygame.time.Clock()
        self.running = True
        self.setup()

    def setup(self):
        self.all_sprites = pygame.sprite.Group()
        self.symbol_sprites = pygame.sprite.Group()

        #objekt
        self.spin_btn = Sprite(self.all_sprites, pygame.Surface((130, 50)), (WINDOW_WIDTH/2, WINDOW_HEIGHT - 80), "green")

        self.player = Player(1000)

        # self.symbol1 = Symbol(self.symbol_sprites, pygame.Surface((50, 50)), (0,0), "red", 5)
        # self.symbol2 = Symbol(self.symbol_sprites, pygame.Surface((50, 50)), (0,0), "blue", 10)
        # self.symbol3 = Symbol(self.symbol_sprites, pygame.Surface((50, 50)), (0,0), "yellow", 15)
        # self.symbol4 = Symbol(self.symbol_sprites, pygame.Surface((50, 50)), (0,0), "green", 20)
        # self.symbols = [self.symbol1, self.symbol2, self.symbol3, self.symbol4]
        
        self.slot_machine = SlotMachine(self.symbol_sprites)

    def run(self):

        while self.running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                #om man klickar på spinknappen
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.spin_btn.rect.collidepoint(event.pos):
                        self.slot_machine.spin()


            #draw
            self.screen.fill("black")
            self.all_sprites.draw(self.screen)
            self.symbol_sprites.draw(self.screen)

            #update
            self.all_sprites.update()
            self.symbol_sprites.update()

            pygame.display.update()

        pygame.quit()


game = Game()

if __name__ == "__main__":
    game.run()




