class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Robot:
    def __init__(self, x, y, asteroid, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.asteroid = asteroid

        if self.x > self.asteroid.x:
            raise MissAsteroidError()
        if self.y > self.asteroid.y:
            raise MissAsteroidError()

    def turn_left(self):
        turns = dict(E="N", N="W", W="S", S="E")
        self.direction = turns[self.direction]

    def turn_right(self):
        turns = dict(E="S", S="W", W="N", N="E")
        self.direction = turns[self.direction]

    def move_forward(self):
        if self.direction == "N":
            self.x += 1
        elif self.direction == "E":
            self.y += 1
        elif self.direction == "S":
            self.x -= 1
        elif self.direction == "W":
            self.y -= 1
        if self.x > self.asteroid.x or self.y > self.asteroid.y:
            raise RobotFallsError()
        else:
            return self.x, self.y

    def move_backward(self):
        if self.direction == "N":
            self.x -= 1
        elif self.direction == "E":
            self.y -= 1
        elif self.direction == "S":
            self.x += 1
        elif self.direction == "W":
            self.y += 1
        if self.x > self.asteroid.x or self.y > self.asteroid.y:
            raise RobotFallsError()
        else:
            return self.x, self.y


class MissAsteroidError(Exception):
    pass


class RobotFallsError(Exception):
    pass
