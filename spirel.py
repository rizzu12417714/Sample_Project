import turtle
import random
import math

# -------------------------
# Screen
# -------------------------
screen = turtle.Screen()
screen.setup(1000, 700)
screen.bgcolor("black")
screen.title("Interactive Space")

turtle.tracer(0)
turtle.colormode(1)

# -------------------------
# 🌍 Earth Horizon
# -------------------------
earth = turtle.Turtle()
earth.hideturtle()
earth.penup()

def draw_earth():
    earth.goto(0, -250)
    earth.color(0, 0.4, 1)
    earth.begin_fill()
    earth.circle(400)
    earth.end_fill()

# -------------------------
# ⭐ Stars
# -------------------------
stars = []
for _ in range(150):
    stars.append((random.randint(-500, 500), random.randint(-300, 350)))

# -------------------------
# 🌌 Galaxy Points
# -------------------------
galaxy = []
for i in range(300):
    angle = i * 0.2
    radius = i * 0.8
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    galaxy.append([x, y])

# Rotation angle
rotation = 0

# -------------------------
# 🎮 Mouse Control
# -------------------------
mouse_x = 0

def move_mouse(x, y):
    global mouse_x
    mouse_x = x / 200   # sensitivity

screen.onscreenclick(move_mouse)

# -------------------------
# 🔄 Animation Loop
# -------------------------
drawer = turtle.Turtle()
drawer.hideturtle()
drawer.penup()

while True:

    drawer.clear()

    # 🌍 Earth
    draw_earth()

    # ⭐ Stars
    for (x, y) in stars:
        drawer.goto(x, y)
        drawer.dot(2, "white")

    # 🌌 Rotating Galaxy
    for point in galaxy:
        x, y = point

        # rotation math
        rx = x * math.cos(rotation + mouse_x) - y * math.sin(rotation + mouse_x)
        ry = x * math.sin(rotation + mouse_x) + y * math.cos(rotation + mouse_x)

        drawer.goto(rx, ry)
        drawer.dot(2, "cyan")

    rotation += 0.01

    turtle.update()