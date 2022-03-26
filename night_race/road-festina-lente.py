from turtle import Turtle


class Road:

    def __init__(self):
        left_road, right_road = Turtle(), Turtle()
        self.roads = [left_road, right_road]
        for road in self.roads:
            # road.hideturtle()
            road.speed("fastest")
            road.hideturtle()
            road.color("white")
            road.penup()
            if self.roads.index(road) == 1:
                road.goto(112, -250)
            else:
                road.goto(-112, -250)
            road.setheading(90)
            road.pendown()
            road.forward(510)
