import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_CARS = 180


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DISTANCE
        for no in range(NUMBER_OF_CARS):
            self.create_cars(no)

    def create_cars(self, car_number):
        new_car = Turtle()
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shape("square")
        new_car.shapesize(stretch_len=2, stretch_wid=1)
        new_car_y_cor = random.randint(-220, 240)
        new_car.goto(300 + car_number * 30, new_car_y_cor)
        new_car.setheading(180)
        self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT

    def loose(self):
        self.car_speed = STARTING_MOVE_DISTANCE
        self.reset_cars()

    def reset_cars(self):
        for no in range(NUMBER_OF_CARS):
            new_car_y_cor = random.randint(-220, 240)
            self.cars[no].goto(300 + no * 30, new_car_y_cor)
