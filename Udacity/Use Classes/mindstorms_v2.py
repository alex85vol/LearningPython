import turtle

window = turtle.Screen()
window.bgcolor('black')
def draw_shape(name, shape, color, speed):

    if name == 'brad':
        name = turtle.Turtle()
        name.pensize(8)
        name.penup()
        name.backward(100)
        name.pendown()
        name.shape(shape)
        name.color(color)
        name.speed(speed)
        i = 0
        while i < 4:
            name.forward(100)
            name.right(90)
            i = i + 1
    elif name == 'angie' :
        name = turtle.Turtle()
        name.shape(shape)
        name.color(color)
        name.penup()
        name.forward(200)
        name.pendown()
        name.pensize(6)
        name.circle(100)
    elif name == 'jack' :
        name = turtle.Turtle()
        name.shape(shape)
        name.color(color)
        name.speed(speed)
        name.penup()
        name.backward(300)
        name.pendown()
        name.pensize(5)
        name.right(135)
        name.forward(100)
        name.right(135)
        name.forward(150)
        name.right(135)
        name.forward(100)

def draw_art():
    draw_shape('brad', 'turtle', 'yellow', 2)
    draw_shape('angie', 'arrow', 'blue', 2)
    draw_shape('jack', 'circle', 'green', 2)

    window.exitonclick()

draw_art()





