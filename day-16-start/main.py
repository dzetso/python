# import another_module
#
# print(another_module.another_variable)

# # import turtle
# from turtle import Turtle, Screen
#
# # timmy = turtle.Turtle()
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("darkslategray")
# # print(timmy)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.speed(3)
# for x in range(0, 4):
#     timmy.forward(100)
#     timmy.right(90)
#     timmy.forward(100)
#     timmy.left(90)
#     timmy.forward(100)
#     timmy.left(90)
#     timmy.speed(15)
#     timmy.forward(200)
#     timmy.speed(3)
#     timmy.left(90)
#     timmy.forward(100)
#     timmy.left(90)
#     timmy.forward(100)
#     timmy.right(90)
#     timmy.forward(100)
#     timmy.right(180)
#
#
# my_screen.exitonclick()

# import prettytable

from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)

# end
