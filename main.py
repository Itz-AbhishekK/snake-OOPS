"""
Imports:
Snake.py which contains the Snake class
Food.py which contains the Food class
Turtle module to implement game graphics
"""

import Snake
import Food
import turtle
import time

""""
The main file for the program that implements the Python game using 
the turtle module. 

Global variables:

DELAY: The value after which the main game loop reruns. This sets how 
fast the snake moves. This value is to be slowly decremented as the 
game progresses.

COUNTER: Variable to keep count of the number of elapsed frames since
the last decrement of the DELAY variable.
"""
DELAY = 100
COUNTER = 0
score = 0



def game_loop() -> None:
    """
    Function that implements the main game loop. All updations are to be
    done in this function. Function should also implement GAME OVER logic
    and do the decrement in DELAY appropriately.
    :return: None
    """

    ############ DO NOT CHANGE ###########
    global DELAY
    global COUNTER
    global score
    ######################################
    ########## WRITE BELOW ###############
    snake_obj.update_snake()
    snake_obj.keep_snake_onscreen()



    if snake_obj.check_food_collision(food_obj.position):
        score += 1
        pen.clear()
        pen.write("Score: {} ".format(score), align="left", font=("Courier", 15, "normal"))

        food_obj.update_random_food_position()
        food_turtle.setpos(food_obj.position)
        x, y = snake_obj.head.pos()
        new_segment_heading = snake_obj.head.heading()
        if new_segment_heading == 180.0:
            snake_obj.add_new_snake_segments((x-20, y))
            snake_obj.head = snake_obj.turtles[0]
            snake_obj.head.direction = 'left'
        if new_segment_heading == 0.0:
            snake_obj.add_new_snake_segments((x+20, y))
            snake_obj.head = snake_obj.turtles[0]
            snake_obj.head.direction = 'right'
        if new_segment_heading == 90.0:
            snake_obj.add_new_snake_segments((x, y+20))
            snake_obj.head = snake_obj.turtles[0]
            snake_obj.head.direction = 'up'
        if new_segment_heading == 270.0:
            snake_obj.add_new_snake_segments((x, y-20))
            snake_obj.head = snake_obj.turtles[0]
            snake_obj.head.direction = 'down'
    if snake_obj.GAME_OVER:
        turtle.write("GAME OVER, Your Score is {} ".format(score), align="center", font=("Courier", 24, "bold"))
        score = 0
        return






    ######################################
    ########### DO NOT CHANGE ############
    screen.update()

    if DELAY > 10 and COUNTER == 25:
        DELAY -= 1
        COUNTER = 0


    COUNTER += 1

    turtle.ontimer(game_loop, DELAY)
    #######################################


if __name__ == "__main__":
    """
    The main for the program.
    DO NOT CHANGE    
    """

    ############ DO NOT CHANGE ############
    screen_height = 600
    screen_width = 600
    start_time = time.time()

    screen = turtle.Screen()
    screen.setup(screen_width, screen_height)
    screen.title("Python in Python by Abhishek Karan")
    screen.bgcolor("blue")
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.penup()
    pen.hideturtle()
    pen.goto((-280, 280))
    pen.write("Score: {} ".format(score), align="left", font=("Courier", 15, "normal"))
    pen.clear()


    snake_obj = Snake.Snake(window_size=(screen_width, screen_height))
    food_obj = Food.Food(window_size=(screen_width, screen_height))
    food_obj.update_random_food_position()

    # snake_turtle = turtle.Turtle("turtle")
    # snake_turtle.color(snake_obj.color)
    # snake_turtle.penup()

    food_turtle = turtle.Turtle()
    food_turtle.shape(food_obj.shape)
    food_turtle.color(food_obj.color)
    food_turtle.pensize(food_obj.size)
    food_turtle.penup()
    food_turtle.setpos(food_obj.position)



    screen.listen()
    screen.onkey(snake_obj.go_up, "Up")
    screen.onkey(snake_obj.go_down, "Down")
    screen.onkey(snake_obj.go_right, "Right")
    screen.onkey(snake_obj.go_left, "Left")

    game_loop()
    turtle.done()
    #########################################
