import pgzrun
from random import randint

#screen size
WIDTH = 1000
HEIGHT = 500

#objects
p = Actor('hero')
e = Actor('enemy')
c = Actor('fruit')

#configs
c.x = randint(50,WIDTH-50)
c.y = randint(50,HEIGHT-50)
p.pos = (WIDTH/2,HEIGHT/2)
e.pos = (-100,HEIGHT/2)
ps = 5
es = 2
score = 0

#drawing on sccreen
def draw():
    screen.clear()
    p.draw()
    e.draw()
    c.draw()
    screen.draw.text(f'Score: {score}',(10,10),color='white')
    
def update(dt):

    global score
    
    #player control
    if keyboard.a:
        p.x -= ps
    if keyboard.d:
        p.x += ps
    if keyboard.w:
        p.y -= ps
    if keyboard.s:
        p.y += ps  
    if keyboard.space:
        p.angle += ps
        
    #enemy tracks player
    if p.x > e.x:
        e.x += es
    if p.x < e.x:
        e.x -= es
    if p.y > e.y:
        e.y += es
    if p.y < e.y:
        e.y -= es
        
    #fruit collide
    if p.colliderect(c):
        c.x = randint(50, WIDTH-50)
        c.y = randint(50,HEIGHT-50)
        score += 10
        sounds.clap.play()
        

#game loop
pgzrun.go()