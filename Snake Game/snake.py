import turtle
import time
import random


class Snake():
    def __init__(self):
        self.ui_init()

    def ui_init(self):
        self.pencere = turtle.Screen()
        self.pencere.title("Snake")
        self.pencere.bgcolor("lightgreen")
        self.pencere.setup(width=600, height=600)
        self.pencere.tracer(0)

        self.kafa = turtle.Turtle()
        self.kafa.speed(0)
        self.kafa.shape("circle")
        self.kafa.color("gray")
        self.kafa.penup()
        self.kafa.goto(0, 100)
        self.kafa.direction = "stop"

        self.yemek = turtle.Turtle()
        self.yemek.speed(0)
        self.yemek.shape("circle")
        self.yemek.color("red")
        self.yemek.penup()
        self.yemek.goto(0, 0)
        self.yemek.shapesize(0.80, 0.80)

        self.kuyruklar = []
        self.puan = 0

        self.yazi = turtle.Turtle()
        self.yazi.speed(0)
        self.yazi.shape("circle")
        self.yazi.color("white")
        self.yazi.penup()
        self.yazi.goto(0, 260)
        self.yazi.hideturtle()
        self.yazi.write(f"Puan: {self.puan}",
                        align="center", font=("Corier", 24, "normal"))

        self.pencere.listen()
        self.pencere.onkey(self.goUp, "Up")
        self.pencere.onkey(self.goDown, "Down")
        self.pencere.onkey(self.goRight, "Right")
        self.pencere.onkey(self.goLeft, "Left")

        while True:
            self.pencere.update()
            self.areaControl()
            self.queueControl()
            self.eat()
            self.move()
            time.sleep(0.15)

    def move(self):
        if self.kafa.direction == "up":
            y = self.kafa.ycor()
            self.kafa.sety(y+20)
        elif self.kafa.direction == "down":
            y = self.kafa.ycor()
            self.kafa.sety(y-20)
        elif self.kafa.direction == "right":
            x = self.kafa.xcor()
            self.kafa.setx(x+20)
        elif self.kafa.direction == "left":
            x = self.kafa.xcor()
            self.kafa.setx(x-20)

    def goUp(self):
        if self.kafa.direction != "down":
            self.kafa.direction = "up"

    def goDown(self):
        if self.kafa.direction != "up":
            self.kafa.direction = "down"

    def goRight(self):
        if self.kafa.direction != "left":
            self.kafa.direction = "right"

    def goLeft(self):
        if self.kafa.direction != "right":
            self.kafa.direction = "left"

    def eat(self):
        if self.kafa.distance(self.yemek) < 20:
            x = random.randint(-250, 250)
            y = random.randint(-250, 250)
            self.yemek.goto(x, y)
            self.yeniKuyruk = turtle.Turtle()
            self.yeniKuyruk.speed(0)
            self.yeniKuyruk.shape("square")
            self.yeniKuyruk.color("white")
            self.yeniKuyruk.penup()
            self.kuyruklar.append(self.yeniKuyruk)
            self.puan += 10
            self.yazi.clear()
            self.yazi.write(f"Puan: {self.puan}",
                            align="center", font=("Corier", 24, "normal"))
        for i in range(len(self.kuyruklar)-1, 0, -1):
            x = self.kuyruklar[i-1].xcor()
            y = self.kuyruklar[i-1].ycor()
            self.kuyruklar[i].goto(x, y)
        if len(self.kuyruklar) > 0:
            x = self.kafa.xcor()
            y = self.kafa.ycor()
            self.kuyruklar[0].goto(x, y)

    def areaControl(self):
        if self.kafa.xcor() > 300 or self.kafa.xcor() < -300 or self.kafa.ycor() > 300 or self.kafa.ycor() < -300:
            time.sleep(1)
            self.kafa.goto(0, 0)
            self.kafa.direction = "stop"
            for kuyruk in self.kuyruklar:
                kuyruk.goto(1000, 1000)
            self.kuyruklar = []
            self.puan = 0
            self.yazi.clear()
            self.yazi.write(f"Puan: {self.puan}", align="center", font=(
                "Corier", 24, "normal"))

    def queueControl(self):
        for i in self.kuyruklar:
            if i.distance(self.kafa) < 20:
                time.sleep(1)
                self.kafa.goto(0, 0)
                self.kafa.direction = "stop"
                for kuyruk in self.kuyruklar:
                    kuyruk.goto(1000, 1000)
                self.kuyruklar = []
                self.puan = 0
                self.yazi.clear()
                self.yazi.write(f"Puan: {self.puan}", align="center", font=(
                    "Corier", 24, "normal"))


if __name__ == "__main__":
    yilan = Snake()
