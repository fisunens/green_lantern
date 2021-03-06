import pytest
from lonely_robot import Robot, Asteroid, MissAsteroidError, RobotFallsError


class TestRobotCreation:
    def test_parameters(self):
        x, y = 10, 15
        asteroid = Asteroid(x + 15, y + 15)
        direction = "N"
        robot = Robot(x, y, asteroid, direction)
        assert robot.x == 10
        assert robot.y == 15
        assert robot.direction == direction
        assert robot.asteroid == asteroid

    @pytest.mark.parametrize(
        "asteroid_size,robot_coordinates",
        (
                ((15, 25), (26, 30)),
                ((15, 25), (26, 24)),
                ((15, 25), (15, 27)),
        )
    )
    def test_check_if_robot_on_asteroid(self, asteroid_size, robot_coordinates):
        with pytest.raises(MissAsteroidError):
            asteroid = Asteroid(*asteroid_size)
            Robot(*robot_coordinates, asteroid, "N")


class TestRobotMove:

    def setup(self):
        self.x, self.y = 10, 15
        self.asteroid = Asteroid(self.x + 15, self.y + 15)

    @pytest.mark.parametrize(
        "current_direction, expected_direction",
        [
            ("E", "N"),
            ("N", "W"),
            ("W", "S"),
            ("S", "E")
        ]
    )
    def test_turn_left(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_left()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "current_direction, expected_direction",
        {
            ("E", "S"),
            ("S", "W"),
            ("W", "N"),
            ("N", "E")
        }
    )
    def test_turn_right(self, current_direction, expected_direction):
        robot = Robot(self.x, self.y, self.asteroid, current_direction)
        robot.turn_right()
        assert robot.direction == expected_direction

    @pytest.mark.parametrize(
        "direction, move_x, move_y",
        [
            ("N", 11, 15),
            ("E", 10, 16),
            ("S", 9, 15),
            ("W", 10, 14)
        ]
    )
    def test_move_forward(self, direction, move_x, move_y):
        robot = Robot(self.x, self.y, self.asteroid, direction)
        robot.move_forward()
        assert robot.x == move_x
        assert robot.y == move_y

    @pytest.mark.parametrize(
        "direction, move_x, move_y",
        [
            ("N", 9, 15),
            ("E", 10, 14),
            ("S", 11, 15),
            ("W", 10, 16)
        ]
    )
    def test_move_backward(self, direction, move_x, move_y):
        robot = Robot(self.x, self.y, self.asteroid, direction)
        robot.move_backward()
        assert robot.x == move_x
        assert robot.y == move_y
