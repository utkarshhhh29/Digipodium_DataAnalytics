from turtle import *

def square():
    for i in range(4):
        forward(100)
        right(360/4)
        
for i in range(3):
    fd(50)
    square()
    right(90)    
        
#calling
square()

hideturtle()
mainloop() #holding the screen