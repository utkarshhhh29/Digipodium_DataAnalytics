from turtle import *

pencolor('green')
pensize(1)
bgcolor('black')

for i in range(5):
    fd(100)
    rt(360/5)
    for i in range(5):
        fd(50)
        rt(360/5)
        
for i in range(4):
    fd(200)
    rt(360/4)
    for i in range(4):
        fd(20)
        rt(360/4)
        
for i in range(4):
    fd(200)
    lt(360/4)
    for i in range(4):
        fd(20)
        lt(360/4)
    
     
        
hideturtle()
mainloop()