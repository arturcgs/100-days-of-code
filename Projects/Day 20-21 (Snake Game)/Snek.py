from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snek:
    def __init__(self):
        self._segments = []
        self.create_snake()
        self.head = self._segments[0]

    def create_snake(self):
        """creates a 3 segments snake, in the center of the screen"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """adds 1 segment to the snake"""
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self._segments.append(new_segment)

    def extend(self):
        """extending the snake by 1 square"""
        self.add_segment(self._segments[-1].position())

    def move(self):
        """moving the snake forward"""
        for seg_index, seg in reversed(list(enumerate(self._segments))[1:]):
            new_x = self._segments[seg_index - 1].xcor()
            new_y = self._segments[seg_index - 1].ycor()
            seg.goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def has_collision(self):
        """Returns true if the snake collides with itself"""
        for segment in self._segments[1:]:
            if self.head.distance(segment) < 10:
                return True
        return False

    def loop_screen(self):
        # loop right
        if self.head.xcor() > 280:
            x = -300
            y = self.head.ycor()
            self.head.goto(x, y)
        # loop left
        elif self.head.xcor() < -300:
            x = 280
            y = self.head.ycor()
            self.head.goto(x, y)
        # loop up
        elif self.head.ycor() > 300:
            x = self.head.xcor()
            y = -280
            self.head.goto(x, y)
        # loop down
        elif self.head.ycor() < -280:
            x = self.head.xcor()
            y = 300
            self.head.goto(x, y)

    # control movement functions
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
