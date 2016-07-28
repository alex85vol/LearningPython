import turtle

def draw_square(some_turtle):
    for i in range(1, 50):
        some_turtle.forward(50)
        some_turtle.right(15)


def draw_art():
    window = turtle.Screen()
    window.bgcolor('red')
    # Create turtle Brad - Draws a square
    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('yellow')
    brad.speed(100)
    for i in range(1,15):
        draw_square(brad)
        brad.right(10)

    # Create the turtle Angie - Draws a circle
    #angie = turtle.Turtle()
    #angie.shape('arrow')
    #angie.color('blue')
    #angie.circle(100)

    window.exitonclick()


draw_art()