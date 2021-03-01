import pygame
from menu import MainMenu
from A_star_algo import main

WIDTH = 800
WIN = pygame.display.set_mode((WIDTH, WIDTH))
class Game:
    def __init__(self):
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 800
        self.display= pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W, self.DISPLAY_H)))
        self.font_name = 'LobsterTwo-Bold.otf'
        self.font_name2 = 'SEASRN__.ttf'
        self.font_name1 = pygame.font.get_default_font()
        self.BLACK, self.WHITE = (0,0,0), (255,255,255)
        self.main_menu = MainMenu(self)
        #self.options = OptionsMenu(self)
        #self.credits = CreditsMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing:
            self.check_events()
            if self.START_KEY:
                self.playing = False
            #self.display.fill(self.BLACK)
            #self.draw_text('Thanks for playing', 50, self.DISPLAY_W/2, self.DISPLAY_H/2)
            self.window.blit(self.display, main(WIN,WIDTH), (0,0))
            pygame.display.update()
            self.reset_key()
            
    def check_events(self):
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                self.running,self.playing = False, False
                self.curr_menu.run_display= False
            if event.type== pygame.KEYDOWN:
                if event.key== pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                if self.playing == True:
                    if event.key == pygame.K_BACKSPACE:
                        self.display.quit()
    def reset_key(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x,y):
        font = pygame.font.Font(self.font_name1,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)

    def draw_text_font(self, text, size, x,y):
        font = pygame.font.Font(self.font_name2,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)
