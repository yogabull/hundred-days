# Exercise using the turtle module to make class objects


# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('red')
# timmy.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Picachu', 'Steve', 'Bob'])
table.add_column('Type', ['Electric', 'Air', 'Mud'])

print(table.align)
table.align = 'l'
print(table.align)


print(table)
