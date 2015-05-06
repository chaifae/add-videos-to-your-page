import turtle


def draw_square(a_turtle):
    for turn in range(1, 5):
        a_turtle.forward(100)
        a_turtle.right(90)

def draw_triangle(a_turtle):
    for turn in range(1, 4):
        a_turtle.forward(100)
        a_turtle.right(120)

def draw_stuff():
    window = turtle.Screen()
    window.bgcolor("light blue")
    window.title("Stephanie's Pet Turtle")
    #turtle for brad draws a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("dark green", "green")
    brad.speed(1)
    draw_square(brad)
    #turtle for angie draws a circle
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)
    #turtle for sara draws a triangle
    sara = turtle.Turtle()
    sara.shape("turtle")
    sara.color("brown", "red")
    sara.right(100)
    draw_triangle(sara)
    
    
    window.exitonclick()



draw_stuff()
