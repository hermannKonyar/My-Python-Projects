import turtle


class Pinpong():
    def __init__(self):
        self.ui_init()

    def ui_init(self):
        self.window = turtle.Screen()
        self.window.title("PinPong")
        self.window.bgcolor("black")
        self.window.setup(width=800, height=600)
        self.window.tracer(0)

        self.racket_a = turtle.Turtle()
        self.racket_a.speed(0)
        self.racket_a.shape("square")
        self.racket_a.color("white")
        self.racket_a.penup()
        self.racket_a.goto(-350, 0)
        self.racket_a.shapesize(5, 1)

        self.racket_b = turtle.Turtle()
        self.racket_b.speed(0)
        self.racket_b.shape("square")
        self.racket_b.color("white")
        self.racket_b.penup()
        self.racket_b.goto(350, 0)
        self.racket_b.shapesize(5, 1)

        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.dx = 0.15
        self.ball.dy = 0.15

        self.puanA = 0
        self.puanB = 0

        self.words = turtle.Turtle()
        self.words.speed(0)
        self.words.color("white")
        self.words.penup()
        self.words.goto(0, 260)
        self.words.write(f"Player A:{self.puanA}  PLayer B:{self.puanB}",
                         align="center", font=("courier", 24, "bold"))
        self.words.hideturtle()

        self.window.onkeypress(self.racket_a_up, "w")
        self.window.onkeypress(self.racket_a_down, "s")
        self.window.onkeypress(self.racket_b_up, "Up")
        self.window.onkeypress(self.racket_b_down, "Down")
        self.window.listen()

        self.run()

    def run(self):
        while True:
            self.window.update()
            self.ballMove()

    def ballMove(self):
        self.ball.setx(self.ball.xcor()+self.ball.dx)
        self.ball.sety(self.ball.ycor()+self.ball.dy)

        if self.ball.ycor() > 290 or self.ball.ycor() < -290:
            self.ball.dy = self.ball.dy*(-1)

        if self.ball.xcor() > 390:
            self.ball.goto(0, 0)
            self.ball.dx = self.ball.dx*(-1)
            self.puanA += 1
            self.words.clear()
            self.words.write(f"Player A:{self.puanA}  PLayer B:{self.puanB}",
                             align="center", font=("courier", 24, "bold"))

        if self.ball.xcor() < -390:
            self.ball.goto(0, 0)
            self.ball.dx = self.ball.dx*(-1)
            self.puanB += 1
            self.words.clear()
            self.words.write(f"Player A:{self.puanA}  PLayer B:{self.puanB}",
                             align="center", font=("courier", 24, "bold"))

        if (self.ball.xcor() > 340 and self.ball.xcor() < 350) and (self.ball.ycor() < self.racket_b.ycor()+60 and self.ball.ycor() > self.racket_b.ycor()-60):
            self.ball.setx(340)
            self.ball.dx = self.ball.dx*(-1)

        if (self.ball.xcor() < - 340 and self.ball.xcor() > - 350) and (self.ball.ycor() < self.racket_a.ycor()+60 and self.ball.ycor() > self.racket_a.ycor()-60):
            self.ball.setx(-340)
            self.ball.dx = self.ball.dx*(-1)

    def racket_a_up(self):
        if self.racket_a.ycor() < 290:
            y = self.racket_a.ycor()
            y += 20
            self.racket_a.sety(y)

    def racket_a_down(self):
        if self.racket_a.ycor() > - 290:
            y = self.racket_a.ycor()
            y -= 20
            self.racket_a.sety(y)

    def racket_b_up(self):
        if self.racket_b.ycor() < 290:
            y = self.racket_b.ycor()
            y += 20
            self.racket_b.sety(y)

    def racket_b_down(self):
        if self.racket_b.ycor() > - 290:
            y = self.racket_b.ycor()
            y -= 20
            self.racket_b.sety(y)


if __name__ == "__main__":
    pinpong = Pinpong()
