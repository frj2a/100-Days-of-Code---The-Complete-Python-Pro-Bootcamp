import random
from turtle import Turtle, Screen
import time
import random as rnd

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.max_x = 0

    def create_car(self):
        car = Turtle()
        car.shape("square")
        car.penup()
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.color(rnd.choice(COLORS))
        car.setheading(180)
        max_y = int(car.screen.window_height() / 2) - 40
        self.max_x = int(car.screen.window_width() / 2) # - 20
        x_init = self.max_x # + self.rand_int(0, self.max_x * 2, 40)
        y_init = self.rand_int(-max_y, max_y, 20)
        # x_init = max_x + rnd.randint(0, int(max_x / 40)) * 40
        # y_init = rnd.randint(-int(max_y / 20) , int(max_y / 20) ) * 20
        car.setpos(x_init, y_init)
        self.cars.append(car)

    def rand_int(self, a, b, mod):
        x = int((random.random() * (b - a) + a) / mod) * mod
        return x

    def level_up(self):
        self.car_speed += MOVE_INCREMENT


    def move(self):
        if random.randint(1,6) == 1:
            self.create_car()
        for car in self.cars:
            car.forward(self.car_speed)
            if car.xcor() < -(self.max_x + 40):
                self.cars.remove(car)
                # car.setpos(self.max_x, car.ycor())
        if len(self.cars) > 0:
            self.cars[0].screen.update()

if __name__ == "__main__":
    screen = Screen()
    screen.setup(width=600, height=600, startx=100, starty=100)
    screen.bgcolor("white")
    screen.title("Turtle Crossing's Cars")
    screen.tracer(0)

    cars = CarManager()

    for _ in range(200):
        cars.move()
        screen.update()
        time.sleep(0.05)

    screen.exitonclick()


