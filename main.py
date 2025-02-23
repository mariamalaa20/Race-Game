import turtle
from turtle import Turtle,Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="which turtle will win the race? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
all_turtles = []
print(user_bet)

x_axis = -230
y_axis = -100

for index in range (0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=x_axis,y=y_axis)
    y_axis += 30
    all_turtles.append(new_turtle)



if user_bet:
    is_race_on = True


while is_race_on :
    for turtle in all_turtles :
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtule is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtule is the winner!")

        random_distanse = random.randint(0,10)
        turtle.forward(random_distanse)


screen.exitonclick()
#Etch-A-Sketch App #################################################################################################
# from turtle import Turtle,Screen
#
# tim = Turtle()
# screen = Screen()
# def move_forwards():
#     tim.forward(10)
#
# def move_backwords():
#     tim.backward(10)
#
# def move_counterClockwise():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
# def move_clockwise():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwords)
# screen.onkey(key="a", fun=move_counterClockwise)
# screen.onkey(key="d", fun=move_clockwise)
# screen.onkey(key="c", fun=clear)
# screen.exitonclick()
########################################################################################################################









