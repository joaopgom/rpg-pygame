# -*- encoding: utf-8 -*-
import sys
import pygame
from pygame import time
from pygame import event
from global_data import screen
from map import Map

class Game():
    def __init__(self):
        self.player = None
        self.team = None    
        self.maps = []
        self.map = Map('WORLD_MAP')
        self.time = time.Clock()
        
    def main_loop(self):
        while True:
            for ev in event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif ev.type == pygame.KEYDOWN:
                    print 'keydown mortal!!!'
            self.map.draw_map()
            pygame.display.flip()
            self.time.tick(30)

if __name__ == '__main__':
    pygame.init()
    #pygame.image.load('images/map/grass.jpg')
    game = Game()
    game.main_loop()