import pygame
import string
from klasser import *

class Game():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Gambling Simulator")
        self.clock = pygame.time.Clock()
        self.running = True
        self.setup()

    def setup(self):
        self.all_sprites = pygame.sprite.Group()
        self.symbol_sprites = pygame.sprite.Group()
        self.text_sprites = []

        self.big_font = pygame.font.Font(None, 60)
        self.font = pygame.font.Font(None, 30)
        self.small_font = pygame.font.Font(None, 20)

        #bilder
        self.slot_machine_image = pygame.image.load(join("images", "slot-machine.png")).convert_alpha()
        self.spin_btn_image = pygame.image.load(join("images", "spin-knapp.png")).convert_alpha()
        self.spin_btn_down_image = pygame.image.load(join("images", "spin-knapp-ner.png")).convert_alpha()
                
        
        #objekt
        self.slot_machine_sprite = Sprite(self.all_sprites, self.slot_machine_image, (WINDOW_WIDTH/2, WINDOW_HEIGHT/2), None)

        self.spin_btn = Sprite(self.all_sprites, self.spin_btn_image, (430, 385), None)

        self.player = Player(1000)

        self.slot_machine = SlotMachine(self.symbol_sprites, self.player, self.small_font, self.text_sprites, self.big_font)


        

        #pengar text
        self.money_text = Text(self.font, f"{self.player.get_balance()} $", True, "white", (WINDOW_WIDTH/2, WINDOW_HEIGHT - 30), self.text_sprites)
        self.text_sprites.append(self.money_text)

        #skrivfält
        self.user_text = ""

        self.active_color = "#7a1e1f"
        self.passive_color = "#950102"

        self.input_box = Sprite(self.all_sprites, pygame.Surface((170, 40)), (220, 385), self.passive_color)
        self.input_text = self.font.render(self.user_text, True, "white")

        self.input_empty_text = self.font.render("Bet here", True, "white")
        
        self.input_active = False




        

    def run(self):

        while self.running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                #om man klickar på spinknappen
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.spin_btn.rect.collidepoint(event.pos):
                        self.spin_btn.image = self.spin_btn_down_image
                        if self.user_text:
                            if self.player.check_balance(self.user_text):
                                self.slot_machine.spin(self.user_text)
                elif event.type == pygame.MOUSEBUTTONUP:
                    self.spin_btn.image = self.spin_btn_image

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.input_box.rect.collidepoint(event.pos):
                        self.input_active = True
                        self.input_box.color = self.active_color
                    else:
                        self.input_active = False
                        self.input_box.color = self.passive_color

                if self.input_active:
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            self.user_text = self.user_text[:-1]
                        else:
                            if len(self.user_text) < 10:
                                if event.unicode in string.digits:
                                    self.user_text += event.unicode


            #draw
            self.screen.fill("black")
            self.symbol_sprites.draw(self.screen)
            self.all_sprites.draw(self.screen)
            
            for text in self.text_sprites:
                text.draw(dt)
            self.screen.blit(self.input_text, (self.input_box.rect.x + 5, self.input_box.rect.y + 10))

            if not self.input_active and not self.user_text:
                self.screen.blit(self.input_empty_text, (self.input_box.rect.x + 5, self.input_box.rect.y + 10))
            
            #update
            self.symbol_sprites.update(dt)
            self.all_sprites.update(dt)
            self.money_text.update_text(f"{self.player.get_balance()} $")
            
            self.input_text = self.font.render(self.user_text, True, "white")
            pygame.display.update()

        pygame.quit()


game = Game()

if __name__ == "__main__":
    game.run()




