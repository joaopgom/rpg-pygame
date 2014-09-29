# -*- encoding: utf-8 -*-
import pygame
import image

def create_screen(width, height):
    
    _screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Game :)')
    _screen.fill((255, 255, 255))
    return _screen

screen = create_screen(800, 608)
texture_manager = image.Image()