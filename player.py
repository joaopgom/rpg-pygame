# -*- encoding: utf-8 -*-
import pygame
from global_data import texture_manager
from global_data import screen
from map import Map

PLAYER_LIST = {
               'CLOUD':{'MAX_HP': 50, 'MAX_MP': 30, 'STR': 5, 'DEF': 5, 'DEFM': 3, 'ATK': 5, 'ATKM': 3}
               }

class Player():
    def __init__(self, name):
        self.name = name
        self.attr = dict()
        self.load_attributes()
        self.hp = self.attr['MAX_HP']
        self.mp = self.attr['MAX_MP']
        self.l_hand = None
        self.r_hand = None
        self.armor = None
        self.level = 1
        self.bag  = []
        self.texture = dict()
        self.direction = 0
        self.position = [0, 0]
        self.in_battle = False
        self.rect = {}
        self.image = {}
        self.load_player_sprite()
    
    def load_attributes(self):
        self.attr = PLAYER_LIST[self.name]
    
    def load_player_sprite(self):
        skin = 'skin'
        if self.in_battle:
            skin = 'battle'
        if not skin in self.image:
            self.image[skin] = []
            self.rect[skin] = []
        texture_manager.load_texture(self.name, 'images/character/'+self.name+'/'+skin+'/'+self.name+'.png')
        
        for x in range(4):
            for y in range(4):
                self.image[skin].append(texture_manager.textures[self.name])
                self.rect[skin].append(pygame.Rect(25.5*x, 38.25*y, 25.5, 38.25))
    
    def walk_change_sprite(self, x, y):
        if x > 0:
            self.direction = 1
        elif x < 0:
            self.direction = 2
        
        if y > 0:
            self.direction = 3
        elif y < 0:
            self.direction = 0
    def move_player(self, x, y):
        self.position[0] += x
        self.position[1] += y

    def draw(self):
        screen.blit(texture_manager.textures[self.name][0], (self.position[0], self.position[1]), self.rect['skin'][self.direction])