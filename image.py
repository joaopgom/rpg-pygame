import pygame

class Image():
    def __init__(self):
        self.textures = dict()
    
    def load_texture(self, texture_name, file_location, color_key=None):
        pygame.init()
        #print pygame.image.load('images/map/WORLD_MAP.png'), pygame.image.load('images\/map\/grama.jpg')
        image_file = pygame.image.load(file_location)
        self.textures[texture_name] = [image_file, image_file.get_rect()]
        
        
         
    