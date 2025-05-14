import turtle

turtle.shape("turtle")

turtle.width()

#turtle draws a triangle
turtle.forward(80)    
turtle.left(120)
turtle.forward(80)
turtle.left(120)
turtle.forward(80)
turtle.left(120)              

#turtle shifts to draw separate shapes
turtle.right(90)              
turtle.forward(50)
turtle.left(90)

#create a while loop to draw a square
num = 0

while num < 4:
    turtle.forward(50)
    turtle.left(90)
    num = num + 1


    
turtle.exitonclick()
