# -*- encoding: utf-8 -*-
import sys
import pygame
from pygame import time
from pygame import event
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN
from global_data import screen
from map import Map

class Game():
    def __init__(self):
        self.player = None
        self.team = None    
        self.maps = []
        self.map = Map('WORLD_MAP')
        self.time = time.Clock()
    
    def player_input(self, key_pressed):
        if key_pressed[K_LEFT]:
            self.camera_effect(3, 0)
        elif key_pressed[K_RIGHT]:
            self.camera_effect(-3, 0)
        elif key_pressed[K_UP]:
            self.camera_effect(0, 3)
        elif key_pressed[K_DOWN]:
            self.camera_effect(0, -3)
        #self.map.load_maptiles()
    
    def camera_effect(self, x_axis, y_axis):
        self.map.set_camera(x_axis, y_axis)
    
    def main_loop(self):
        pygame.key.set_repeat(1, 10)
        while True:
            for ev in event.get():
                if ev.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif ev.type == pygame.KEYDOWN:
                    self.player_input(pygame.key.get_pressed())            
            self.map.draw_map()
            pygame.display.update()
            self.time.tick(45)

if __name__ == '__main__':
    pygame.init()
    #pygame.image.load('images/map/grass.jpg')
    game = Game()
    game.main_loop()