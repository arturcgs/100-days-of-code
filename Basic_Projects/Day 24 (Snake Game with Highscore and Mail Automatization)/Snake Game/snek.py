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
        self._head = self._segments[0]

    @property
    def head(self):
        return self._head

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

    def restart_snake(self):
        """Deletes the old snake and creates a new one"""
        # deleting old snake
        for seg in self._segments:
            seg.goto(1000, 1000)
        self._segments.clear()
        # creating new snake
        self.__init__()

    def move(self):
        """moving the snake forward"""
        for seg_index, seg in reversed(list(enumerate(self._segments))[1:]):
            new_x = self._segments[seg_index - 1].xcor()
            new_y = self._segments[seg_index - 1].ycor()
            seg.goto(new_x, new_y)
        self._head.forward(MOVE_DISTANCE)

    def has_collision(self):
        """Returns true if the snake collides with itself"""
        for segment in self._segments[1:]:
            if self._head.distance(segment) < 10:
                return True
        return False

    def loop_screen(self):
        """Creates the looping through the screen effect"""
        # loop right
        if self._head.xcor() > 280:
            x = -300
            y = self._head.ycor()
            self._head.goto(x, y)
        # loop left
        elif self._head.xcor() < -300:
            x = 280
            y = self._head.ycor()
            self._head.goto(x, y)
        # loop up
        elif self._head.ycor() > 300:
            x = self._head.xcor()
            y = -280
            self._head.goto(x, y)
        # loop down
        elif self._head.ycor() < -280:
            x = self._head.xcor()
            y = 300
            self._head.goto(x, y)

    # control movement functions
    def up(self):
        if self._head.heading() != DOWN:
            self._head.setheading(UP)

    def right(self):
        if self._head.heading() != LEFT:
            self._head.setheading(RIGHT)

    def left(self):
        if self._head.heading() != RIGHT:
            self._head.setheading(LEFT)

    def down(self):
        if self._head.heading() != UP:
            self._head.setheading(DOWN)
