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

        self.font = pygame.font.Font(None, 30)



        #objekt
        self.spin_btn = Sprite(self.all_sprites, pygame.Surface((130, 50)), (WINDOW_WIDTH/2, WINDOW_HEIGHT - 80), "green")

        self.player = Player(1000)

        self.slot_machine = SlotMachine(self.symbol_sprites, self.player)

        #pengar text
        self.money_text = self.font.render(f"{self.player.get_balance()}", True, "white")
        self.money_rect = self.money_text.get_frect(center = (WINDOW_WIDTH/2, WINDOW_HEIGHT - 30))


        #skrivfält
        self.user_text = ""

        self.active_color = "white"
        self.passive_color = "grey"

        self.input_box = Sprite(self.all_sprites, pygame.Surface((130, 50)), (WINDOW_WIDTH/2, WINDOW_HEIGHT - 150), self.passive_color)
        self.input_text = self.font.render(self.user_text, True, "white")
        
        self.input_active = False
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

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.rect.collidepoint(event.pos):
                        self.input_active = True
                        self.input_box.color = self.active_color
                    else:
                        self.input_active = False
                        self.input_box.color = self.passive_color

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.user_text = self.user_text[:-1]
                    else:
                        self.user_text += event.unicode


            #draw
            self.screen.fill("black")
            self.all_sprites.draw(self.screen)
            self.symbol_sprites.draw(self.screen)
            self.screen.blit(self.money_text, self.money_rect)
            self.screen.blit(self.input_text, (self.input_box.rect.x + 5, self.input_box.rect.y + 5))
            
            #update
            self.all_sprites.update()
            self.symbol_sprites.update()
            self.money_text = self.font.render(f"{self.player.get_balance()}", True, "white")
            self.input_text = self.font.render(self.user_text, True, "white")

            pygame.display.update()

        pygame.quit()


game = Game()

if __name__ == "__main__":
    game.run()




