import pygame

def create_screen(width, height):
    
    _screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Game :)')
    _screen.fill((255, 255, 255))
    return _screen

screen = create_screen(800, 608)