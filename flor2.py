import turtle

# Define the flower's shape
def draw_flower(size):
  turtle.begin_fill()
  for i in range(5):
    turtle.forward(size)
    turtle.left(72)
  turtle.end_fill()

# Create the flower
size = 100
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
draw_flower(size)

# Show the flower
turtle.done()