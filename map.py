# -*- encoding: utf-8 -*-
import pygame
import global_data

MAPS_LIST = {'WORLD_MAP':[True, 50, 30, 30],
             'MIDGARD':[False, 0, 30, 30]
            }

class MapTile():
    def __init__(self):
        self.name = ''
        self.can_walk = False
        self.pos = (0, 0)
        self.width = 0
        self.height = 0
        self.image = None
        self.rect = None
        self.rect_back = None
        self.backg = None
        self.backg_img_x = None
        self.backg_img_y = None
        
    def draw(self, x, y, camera):
        if self.backg:
            global_data.screen.blit(global_data.texture_manager.textures[self.name+'_back'][0], (self.pos[0]+camera[0], self.pos[1]+camera[1]))
        #if not self.can_walk:
            #print self.pos[0]+camera[0], self.pos[1]+camera[1], self.rect
        global_data.screen.blit(global_data.texture_manager.textures[self.name][0], (self.pos[0]+camera[0], self.pos[1]+camera[1]), self.rect)
        
class Map():
    def __init__(self, name):
        self.name = name
        self.current_tile = None
        self.has_enemies = MAPS_LIST[self.name][0]
        self.enemy_freq = MAPS_LIST[self.name][1]
        self.map_width = MAPS_LIST[self.name][2]
        self.map_height = MAPS_LIST[self.name][3]
        self.tiles = [[MapTile() for i in range(self.map_width)] for j in range(self.map_height)]
        self.collisions = [[pygame.Rect(0,0,0,0) for i in range(self.map_height)] for j in range(self.map_width)]
        self.camera = [0, 0]
        self.load_maptiles()
        
    
    def load_maptiles(self):
        file = open('data/maps/'+self.name+'.map', 'r')
        for x in range(self.map_width):
            for y in range(self.map_height):
                line_data = file.readline().split(';')
                self.tiles[x][y].name = line_data[0]
                self.tiles[x][y].can_walk = True if line_data[1] == 'True' else False                
                self.tiles[x][y].pos_img_x = int(line_data[2]) 
                self.tiles[x][y].pos_img_y = int(line_data[3])
                self.tiles[x][y].pos = (int(line_data[4]) + self.camera[0], int(line_data[5]) + self.camera[1])
                if self.tiles[x][y].name not in global_data.texture_manager.textures:
                    global_data.texture_manager.load_texture(self.tiles[x][y].name, 'images/'+line_data[6])
                
                if len(line_data) > 7:
                    global_data.texture_manager.load_texture(self.tiles[x][y].name+'_back', 'images/'+line_data[9])
                    self.tiles[x][y].backg = global_data.texture_manager.textures[self.tiles[x][y].name+'_back']
                    self.tiles[x][y].backg_img_x = int(line_data[7])
                    self.tiles[x][y].backg_img_y = int(line_data[8])
                self.tiles[x][y].image = global_data.texture_manager.textures[self.tiles[x][y].name]
                self.tiles[x][y].rect = pygame.Rect(self.tiles[x][y].pos_img_x, self.tiles[x][y].pos_img_y, 32, 32)
        file.close()
        
                
    def draw_map(self):
        for x in range(30):
            for y in range(30):
                self.tiles[x][y].draw(x, y, self.camera)

    def move_camera(self, x, y):
        if x > 0 and self.camera[0] < 0 or x < 0 and (800 - (self.map_width*32)) < self.camera[0]:
            return True
        elif y > 0 and self.camera[1] < 0 or y < 0 and (800 - (self.map_height*32)) < self.camera[1]:
            return True
        return False
    
    def set_camera(self, x, y):
        if x > 0 and self.camera[0] < 0 or x < 0 and (800 - (self.map_width*32)) < self.camera[0]:
            self.camera[0] = (self.camera[0] + x)

        if y > 0 and self.camera[1] < 0 or y < 0 and (800 - (self.map_height*32)) < self.camera[1]:
            self.camera[1] = (self.camera[1] + y)
        