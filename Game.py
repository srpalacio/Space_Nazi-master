from Sky import Sky
from Ship import Ship
import pygame
import random

class Game:
    
    def __init__(self):
        
        self.width= 400
        self.height= 400
        
        self.mySky= Sky(self.width, self.height, 50)
        
        self.screen= pygame.display.set_mode((self.width, self.height))
        self.clock= pygame.time.Clock()
        self.fps= 200
        #Cargar la hoja de imágenes
        
        self.sprites= pygame.image.load("sprites.png")
        
        self.shipsprite= pygame.Surface((64,64)).convert()
        self.shipsprite.blit(self.sprites,(0,0),(250,436,64,64))
        self.myShip=Ship()
        

    def run(self):
        
        pygame.init()
        
        control=True
        while control:
            
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    pygame.quit()
            
            self.screen.fill((0,0,0))
            
            #Show the Sky
            
            for star in self.mySky.stars:
                r= random.randint(0, 255)
                g= random.randint(0, 255)
                b= random.randint(0, 255)
                pygame.draw.circle(self.screen,(r,g,b), star, 1)

            
                
            self.mySky.move()            
            
            x=self.myShip.move(self.checkkeys())
            y=self.height/2
            self.screen.blit(self.shipsprite, (x,y))
                
            pygame.display.flip()
            
            self.clock.tick(self.fps)
    
    def checkkeys(self):
        keys=pygame.key.get_pressed()

        if  keys[pygame.K_LEFT]:
            return "LEFT"

        if  keys[pygame.K_RIGHT]:
            return "RIGHT"
            
myGame=Game()
myGame.run()
            