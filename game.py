# -*- encoding: utf-8 -*-
import sys
import pygame
from math import ceil
from pygame import time
from pygame import event
from pygame.locals import K_LEFT, K_RIGHT, K_UP, K_DOWN
from global_data import screen
from map import Map
from player import Player

class Game():
    def __init__(self):
        self.player = Player('CLOUD')
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
    
    def camera_effect(self, x_axis, y_axis):
        self.player.walk_change_sprite(x_axis, y_axis)

        player_x, player_y = self.player.position[0]+x_axis, self.player.position[1]+y_axis
        
        x = (self.map.camera[0] * (-1)) + self.player.position[0] if self.map.camera[0] < 0 else self.map.camera[0] + self.player.position[0]
        y = (self.map.camera[1] * (-1)) + self.player.position[1] if self.map.camera[1] < 0 else self.map.camera[1] + self.player.position[1]
        x = (x + 2) if x_axis > 0 else (x + 2)
        y = (y + 2) if y_axis > 0 else (y + 2)
        
        y = int(ceil(y/32))
        x = int(ceil(x/32))
        
        y_sum = 0
        x_sum = 0
        
        if y_axis != 0:
            y_sum = -1 if y_axis > 0 else 1
        if x_axis != 0:
            x_sum = -1 if x_axis > 0 else 1
        x += x_sum
        y += y_sum
        
        if x < 0:
            x = 0
        if x >= len(self.map.tiles[0]):
            x = len(self.map.tiles[0]) - 1 
        
        if y < 0:
            y = 0
        if y > len(self.map.tiles):
            y = len(self.map.tiles)
        #print x, y, self.map.tiles[y][x].can_walk
        if self.map.tiles[y][x].can_walk:
            if self.map.move_camera(x_axis, y_axis):
                self.map.set_camera(x_axis, y_axis)
            else:
                x_axis = x_axis*(-1)
                y_axis = y_axis*(-1)
                #print x_axis, y_axis
                if x_axis != 0:
                    if x_axis > 0:
                        if self.player.position[0] + x_axis > (800-25):
                            x_axis = 0
                    else:
                        if self.player.position[0] + x_axis + 25 < 25:
                            x_axis = 0
    
                if y_axis != 0:
                    if y_axis > 0:
                        print self.player.position[1] + y_axis
                        if self.player.position[1] + y_axis > (608-38):                                
                            y_axis = 0
                    else:
                        if self.player.position[1] + y_axis + 38 < 38:
                            y_axis = 0                                
    
                self.player.move_player(x_axis, y_axis)
    
    def main_loop(self):
        pygame.key.set_repeat(1, 10)
        while True:
            
            for ev in event.get():
                if ev.type == pygame.QUIT:
                    for i in range(30):
                        for j in range(30):
                           if not self.map.tiles[i][j].can_walk:
                               print i, j, self.map.tiles[i][j] 
            
                    pygame.quit()
                    sys.exit()
                elif ev.type == pygame.KEYDOWN:
                    self.player_input(pygame.key.get_pressed())            
            self.map.draw_map()
            self.player.draw()
            self.player.make_move = False
            pygame.display.update()
            self.time.tick(15)

if __name__ == '__main__':
    pygame.init()
    game = Game()
    game.main_loop()