import pygame
from klasser import *
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500

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

        #spin knapp
        self.spin_btn = Sprite(self.all_sprites, pygame.Surface((130, 50)), (WINDOW_WIDTH/2, WINDOW_HEIGHT - 80))
        

    def run(self):

        while self.running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    if self.spin_btn.rect.collidepoint(event.pos):
                        pass


            #draw
            self.screen.fill("black")
            self.all_sprites.draw(self.screen)

            #update
            self.all_sprites.update()
            pygame.display.update()

        pygame.quit()


game = Game()

if __name__ == "__main__":
    game.run()




