class Map():
    def __init__(self, name):
        self.name = name
        self.current_tile = None
        self.tiles = []      
        self.collisions = []
        