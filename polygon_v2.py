from turtle import*

def polygon(sides,length,width,color):
    pencolor(color)
    pensize(width)
    for i in range(sides):
        forward(length)
        right(360/sides)

#calling
polygon(4,50,5,'green') #square
goto(100,90)
polygon(5,100,10,'red') #pentagon
goto(30,50)
polygon(8,120,15,'blue') #octagon
    