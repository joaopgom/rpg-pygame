# -*- encoding: utf-8 -*-
import sys
import pygame
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

        #print self.player.position[0]+x_axis+self.map.camera[0],  self.player.position[1]+y_axis+self.map.camera[1] 

        player_x, player_y = self.player.position[0]+x_axis, self.player.position[1]+y_axis
        print self.player.position[0]+x_axis+self.map.camera[0], self.player.position[1]+y_axis+self.map.camera[1]
        #print int(player_x/self.map.map_width), int(player_y/self.map.map_height)
        if self.map.tiles[int(player_x/self.map.map_width)][int(player_y/self.map.map_height)].can_walk:
            if self.map.move_camera(x_axis, y_axis):
                self.map.set_camera(x_axis, y_axis)
            else:
                x_axis = x_axis*(-1)
                y_axis = y_axis*(-1)
                if x_axis != 0:
                    if x_axis > 0:
                        if self.player.position[0] + x_axis > (800-25):
                            x_axis = 0
                    else:
                        if self.player.position[0] + x_axis + 25 < 25:
                            x_axis = 0

                if y_axis != 0:
                    if y_axis > 0:
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
                    pygame.quit()
                    sys.exit()
                elif ev.type == pygame.KEYDOWN:
                    self.player_input(pygame.key.get_pressed())            
            self.map.draw_map()
            self.player.draw()
            pygame.display.update()
            self.time.tick(45)

if __name__ == '__main__':
    pygame.init()
    #pygame.image.load('images/map/grass.jpg')
    game = Game()
    game.main_loop()