import turtle

# 设置画布
screen = turtle.Screen()
screen.bgcolor("white")
t = turtle.Turtle()
t.pensize(3)
t.speed(8)

# === 画头部轮廓 ===
t.penup()
t.goto(0, -150)
t.pendown()
t.color("black")
t.begin_fill()
t.circle(150)  # 主体是个大圆
t.end_fill()


# === 画眼圈 ===
def draw_eye(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

    t.penup()
    t.goto(x + 5, y + 10)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(10)
    t.end_fill()


draw_eye(-50, 50)  # 左眼
draw_eye(50, 50)  # 右眼

# === 画五彩头环 ===
colors = ["red", "orange", "yellow", "green", "blue"]
radius = 160
for color in colors:
    t.penup()
    t.goto(0, -radius)
    t.setheading(0)
    t.pendown()
    t.color(color)
    t.circle(radius)
    radius += 5


# === 画耳朵 ===
def draw_ear(x, y):
    t.penup()
    t.goto(x, y)
    t.setheading(45)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()


draw_ear(-90, 130)  # 左耳
draw_ear(90, 130)  # 右耳

# === 结束 ===
t.hideturtle()
turtle.done()
