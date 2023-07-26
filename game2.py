from random import randint
import pgzrun

WIDTH = 1000
HEIGHT = 500

class Player(Actor):
    
    pos = (WIDTH/2,HEIGHT/2)
    speed = 5
    
    #player control
    def movement(self):
    
        if keyboard.a:
            self.x -= self.speed
        if keyboard.d:
            self.x += self.speed
        if keyboard.w:
            self.y -= self.speed
        if keyboard.s:
            self.y += self.speed
        if keyboard.space:
            self.angle += self.speed 
    
class Enemy(Actor):
    
    pos = (-100,HEIGHT/2)
    speed = 2
    
    #enemy tracks player
    def tracking(self,p):
        
        if p.x > self.x:
            self.x += self.speed
        if p.x < self.x:
            self.x -= self.speed
        if p.y > self.y:
            self.y += self.speed
        if p.y < self.y:
            self.y -= self.speed
    
        #enemy collide
        if self.colliderect(p):
            exit()
    
class Fruits(Actor):
    x = randint(50,WIDTH-50)
    y = randint(50,HEIGHT-50)
    
    def relocate(self):
        self.x = randint(50,WIDTH-50)
        self.y = randint(50,HEIGHT-50)
        
#game code

p = Player('hero')
e = Player('enemy')
c = Player('fruits')
score = 0

#drawing on sccreen
def draw():
    
    screen.clear()
    p.draw()
    e.draw()
    c.draw()
    screen.draw.text(f'Score: {score}',(10,10),color='white')
    
def update(dt):
    movement()
    tracking()
    fruit_eating() 