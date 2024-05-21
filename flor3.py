import turtle

# Configurar la ventana y el lápiz
window = turtle.Screen()
window.bgcolor("white")
pen = turtle.Turtle()
pen.speed(2)
pen.color("red")

# Dibujar pétalos de la flor
for _ in range(36):
    pen.forward(100)
    pen.right(45)
    pen.forward(100)
    pen.right(135)
    pen.forward(100)
    pen.right(45)
    pen.forward(100)
    pen.right(135)
    pen.right(10)

# Ocultar el lápiz y cerrar la ventana al hacer clic
pen.hideturtle()
window.exitonclick()