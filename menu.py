import pygame

class Menu:

    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.run_display =True
        self.cursor_rect = pygame.Rect(20,50,150,150)
        self.offset = -100

    def draw_cursor(self):
        self.game.draw_text('x', 40, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0,0))
        pygame.display.update()
        self.game.reset_key()

class MainMenu(Menu):
    def __init__(self,game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 70
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 120
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 170
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)
        self.image = pygame.image.load('maze1.jpg')

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.blit(self.image, (0,0))
            self.game.draw_text_font("PATHFINDER", 90, 400,200)
            #self.game.draw_text("Main Menu", 70, self.game.DISPLAY_W/2, self.game.DISPLAY_H/2)
            self.game.draw_text("Start", 50, self.startx, self.starty)
            #self.game.draw_text("Options", 50,  self.optionsx, self.optionsy)
            #self.game.draw_text("Credits", 50,  self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
            if self.game.DOWN_KEY:
                if self.state == 'Start':
                    self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)

    def check_input(self):
        #self.move_cursor()
        if self.game.START_KEY :
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == "Options":
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            self.run_display = False
