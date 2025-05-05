import turtle

# Setup layar
screen = turtle.Screen()
screen.bgcolor("black")

# Buat objek turtle
flower = turtle.Turtle()
flower.speed(0)
flower.color("magenta")
flower.pensize(2)

# Fungsi menggambar kelopak
def draw_flower():
    for i in range(36):
        flower.forward(100)
        flower.left(45)
        flower.forward(100)
        flower.left(135)
        flower.forward(100)
        flower.left(45)
        flower.forward(100)
        flower.left(135)
        flower.left(10)  # rotasi sedikit untuk efek melingkar

draw_flower()

# Selesai
flower.hideturtle()
screen.mainloop()
