from click import pass_context
from Ship import Ship

class Bullet:
    
    def __init__(self):
        
        self.bullets=[(0,0)]
        self.myCoordinates=Ship()
        self.x=self.myCoordinates.x
        self.y=300
  
    def bmove(self,shoot):
        
        if shoot==True:
            self.y-=1
        return self.y