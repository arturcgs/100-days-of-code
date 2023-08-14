from turtle import Turtle, colormode
import random
INITIAL_Y = [i for i in range(-195, 220, 50)]
colormode(255)


def change_color(car):
    """ This function changes de turtle's color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    car.color((r, g, b))


class CarManager:
    def __init__(self):
        super(CarManager, self).__init__()
        self._cars_list = []
        self.speed = 10

    def create_cars(self):
        """Has a 1 in 6 chance to create a car and append it to the cars_list"""
        if random.randint(1, 5) == 5:
            # creating car
            new_car = Turtle(shape="square")
            new_car.shapesize(stretch_len=2)
            new_car.penup()
            change_color(new_car)

            # setting new_car's initial position
            new_car.goto(300, random.choice(INITIAL_Y))

            # appending new_car to the car list
            self._cars_list.append(new_car)

    def move(self):
        for car in self._cars_list:
            car.backward(self.speed)
            if car.ycor() <= -320:
                self._cars_list.remove(car)

    def has_car_collision(self, player):
        for car in self._cars_list:
            if player.distance(car) <= 15:
                return True
        return False

    def increase_speed(self):
        self.speed += 3
