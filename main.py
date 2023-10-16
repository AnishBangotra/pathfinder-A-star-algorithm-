from game import Game
from pygame import mixer 

mixer.init() 
mixer.music.load("music.mp3") 
mixer.music.set_volume(0.7) 
mixer.music.play()

g=Game()
while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
