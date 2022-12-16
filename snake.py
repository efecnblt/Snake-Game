from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.three_turtles = []
        self.create_snake()
        self.head = self.three_turtles[0]
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for turtle_num in range(len(self.three_turtles)-1, 0, -1):
            new_x = self.three_turtles[turtle_num-1].xcor()
            new_y = self.three_turtles[turtle_num-1].ycor()
            self.three_turtles[turtle_num].goto(new_x, new_y)
        self.three_turtles[0].forward(MOVE_DISTANCE)

    def add_segment(self, position):
        turtle = Turtle(shape="square")
        turtle.penup()
        turtle.color("white")
        turtle.goto(position)
        self.three_turtles.append(turtle)
    def reset(self):
        for seg in self.three_turtles:
            seg.goto(1000, 1000)
        self.three_turtles.clear()
        self.create_snake()
        self.head = self.three_turtles[0]

    def extend(self):
        #add a new segment to the snake.
        self.add_segment(self.three_turtles[-1].position())

    def up(self):
        if self.three_turtles[0].heading() != DOWN:
            self.three_turtles[0].setheading(UP)
    def down(self):
        if self.three_turtles[0].heading() != UP:
            self.three_turtles[0].setheading(DOWN)
    def left(self):
        if self.three_turtles[0].heading() != RIGHT:
            self.three_turtles[0].setheading(LEFT)
    def right(self):
        if self.three_turtles[0].heading() != LEFT:
            self.three_turtles[0].setheading(RIGHT)

