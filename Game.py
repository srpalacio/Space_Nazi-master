from Sky import Sky
from Ship import Ship
from Bullet import Bullet
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
        
        self.sprites_2= pygame.image.load("bulletsprite.png")
        
        self.bulletsprite= pygame.Surface((10,10)).convert()
        self.bulletsprite.blit(self.sprites_2,(0,0),(94,180,270,360))

        self.myShip=Ship()
        self.myBullets=Bullet()
        

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
            y=300
            self.screen.blit(self.shipsprite, (x,y))
            

            bullet_x=x
            bullet_y=self.myBullets.bmove(self.checkshoot())
            self.screen.blit(self.bulletsprite, (bullet_x,bullet_y))

            pygame.display.flip()
            
            self.clock.tick(self.fps)
    
    def checkkeys(self):
        keys=pygame.key.get_pressed()

        if  keys[pygame.K_LEFT]:
            return "LEFT"

        if  keys[pygame.K_RIGHT]:
            return "RIGHT"
        
    def checkshoot(self):
        keys=pygame.key.get_pressed()
        shoot=False
        if  keys[pygame.K_w]:
             shoot=True
        return shoot     
            
myGame=Game()
myGame.run()
            