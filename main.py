import pygame
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

    def setup():
        pass
        

    def run(self):

        while self.running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False


            #draw
            self.screen.fill("black")

            #update
            pygame.display.update()

        pygame.quit()


game = Game()

if __name__ == "__main__":
    game.run()




