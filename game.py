import pygame
from pygame import timer
from global_data import screen

class Game():
    def __init__(self):
        self.player = None
        self.team = None    
        self.maps = []
        self.map = None

    def main_loop(self):
        while True:
            pygame.display.flip()
            timer.Tick(30)

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.main_loop()