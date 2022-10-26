import pygame

class Ship:
    
    def __init__(self):
        self.x=200
        self.coord_y=200
        pass

    def move(self, direction):

        
        if direction=="RIGHT":
            self.x+=1
        elif direction=="LEFT":
            self.x-=1
        return self.x
    
    def shoot(self):
        pass
    
    def explode(self):
        pass
    
    
    