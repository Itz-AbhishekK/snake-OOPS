import turtle


class Snake:
    """
    Class Snake that holds all the attributes of the snake that the player controls
    while playing the game.
    """

    def __init__(self, window_size: tuple):
        """
        Constructor for the Snake class. Has to initialize the
        following variables.

        __offsets__: dictionary
                    A dictonary that maps 'up', 'down', 'right'
                    and 'left' to the appropriate actions for the
                    snake segment positions.
        shape:      List of lists
                    A list of the segments of the snake.

        direction:  str
                    A string holding the current direction in which the
                    snake is moving.

        color:      str
                    A string holding the color of the snake

        window_size: tuple
                    A tuple of integers holding the game window size

        GAME_OVER:  bool
                    A flag to tell if the Game Over condition has been triggered

        :param window_size: The size of the game window given as
                            a tuple containing (window_width, window_height)
        """
        self.__offsets__ = {'Up': (0, 20), 'Down': (0, -20), 'Left': (-20, 0), 'Right': (20, 0)}
        self.shape = [[0, 0], [-20, 0], [-40, 0]]
        self.color = 'black'
        self.direction = 'Right'
        self.window_size = window_size
        self.GAME_OVER = False
        self.turtles = []
        self.mapper = {'up': 90, 'down': 270, 'left': 180, 'right': 0}
        for count, (x, y) in enumerate(self.shape):

            segment = turtle.Turtle()
            segment.shape("turtle")
            segment.color('grey')
            segment.penup()
            segment.goto((x, y))
            self.turtles.append(segment)
        self.head = self.turtles[0]
        self.head.direction = 'stop'

    def add_new_snake_segments(self, position):
        new_snake_segment = turtle.Turtle()
        new_snake_segment.shape('turtle')
        new_snake_segment.color('grey')
        new_snake_segment.penup()
        new_snake_segment.goto(position)
        self.turtles.insert(0, new_snake_segment)


    def go_up(self) -> None:
        """
        Function that implements what happens when
        the up arrow is pressed on the keyboard
        :return: None
        """
        ############## WRITE BELOW ###############
        if self.head.direction != 'down':
            self.head.direction = 'up'

        ##########################################

    def go_down(self) -> None:
        """
                Function that implements what happens when
                the down arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.head.direction != 'up':
            self.head.direction = 'down'
        ##########################################

    def go_left(self) -> None:
        """
                Function that implements what happens when
                the left arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.head.direction != 'right':
            self.head.direction = 'left'
        ##########################################

    def go_right(self) -> None:
        """
                Function that implements what happens when
                the right arrow is pressed on the keyboard
                :return: None
                """
        ############## WRITE BELOW ###############
        if self.head.direction != 'left':
            self.head.direction = 'right'

        ##########################################

    def check_food_collision(self, current_food_position: tuple) -> bool:
        """
        Function that checks if the snake has collided with the food.
        :param current_food_position: A tuple of integers representing the
                                      current position of the food.
        :return: bool
                 Returns True if the snake has collided with the food, False
                 otherwise
        """

        ############## WRITE BELOW ###############
        if self.head.distance(current_food_position) < 20:
            return True
        else:
            return False

        ##########################################

    def keep_snake_onscreen(self) -> None:
        """
        Function that implements the logic that prevents
        the snake from going off the side of the game window.
        The snake is to reappear from the other side of the
        window.

        :return: None
        """
        ############## WRITE BELOW ###############
        for turtle in self.turtles:
            x, y = turtle.pos()
            if x > 290:
                turtle.setx(-290)
            if x < -290:
                turtle.setx(290)
            if y > 290:
                turtle.sety(-290)
            if y < -290:
                turtle.sety(290)

    def update_snake(self) -> None:
        """
        Function that updates the positions of the
        snake per game loop. Function also checks
        if game over condition has been reached.
        :return: None
        """

        ############## WRITE BELOW ###############
        lst = [seg.pos() for seg in self.turtles]
        head_ = lst[0]
        lst = lst[2:]

        if head_ in lst:
            self.GAME_OVER = True

        if not self.GAME_OVER:
            for index in range(len(self.turtles) - 1, 0, -1):
                x = self.turtles[index - 1].xcor()
                y = self.turtles[index - 1].ycor()
                self.turtles[index].goto(x, y)
                self.turtles[index].setheading(self.turtles[index - 1].heading())
            if self.head.direction != 'stop':
                self.head.setheading(self.mapper[self.head.direction])
            self.head.forward(20)



        ##########################################
