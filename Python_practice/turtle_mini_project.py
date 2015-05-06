import turtle


def draw_square(a_turtle, size):
    for turn in range(1, 5):
        a_turtle.forward(size)
        a_turtle.right(90)

def draw_triangle(a_turtle, size):
    for turn in range(1, 4):
        a_turtle.forward(size)
        a_turtle.right(120)

def draw_stuff():
    # This sets up the background
    window = turtle.Screen()
    window.bgcolor("#99EBFF")
    window.title("Stephanie's Turtle Flower")

    # This sets up the turtle
    flower = turtle.Turtle()
    flower.shape("turtle")
    flower.speed(0)
    flower.color("#004824", "#00CC7A")
    # The turtle draws the stem fo the flower
    flower.fill(True)
    flower.forward(5)
    flower.right(90)
    flower.forward(400)
    flower.right(90)
    flower.forward(10)
    flower.right(90)
    flower.forward(400)
    flower.right(90)
    flower.forward(5)
    flower.fill(False)
    # The turtle draws the background leaves
    flower.fill(True)
    for i in range(1, 19):
        draw_triangle(flower, 235)
        flower.right(20)
    flower.fill(False)
    # The turtle draws the flower petals
    flower.color("#991F5C", "#FFA3E0")
    flower.fill(True)
    for i in range(1, 19):
        flower.circle(100)
        flower.right(20)
    flower.fill(False)
    # The turtle draws the center of the flower
    flower.color("#991F5C", "#EE8DCD")
    flower.fill(True)
    for i in range(1, 37):
        draw_square(flower, 50)
        flower.right(10)
    flower.fill(False)
    flower.color("#991F5C", "#E65CB8")
    flower.fill(True)
    for i in range(1, 37):
        draw_square(flower, 35)
        flower.right(10)
    flower.fill(False)
    flower.color("#004824", "#00CC7A")
    
    window.exitonclick()



draw_stuff()
