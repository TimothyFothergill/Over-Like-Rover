valid_directions = ["N", "E", "S", "W"]


class MyRover:

    """Create your very own Mars Rover 1. We salute you, Mars Rover 1. There's only one Mars Rover 1, until
    you make more of them, I guess.
    Define your Mars Rover 1 with:

    MyRover(
        starting_point = [list],

        starting_direction = string ("N/E/S/W")

        mars_grid = SurfaceOfMars

        )"""

    def __init__(self, starting_point, starting_direction, mars_grid):
        self.mars = mars_grid

        print("The chances of anything coming from Mars is a million to one, they said.")
        print("So we calculated that Mars has a grid of: " + str(self.mars.x) + " on the x axis and " +
              str(self.mars.y) + " on the y axis.")
        print("We await your safe return, Mars Rover 1, the only of its kind. Failure is not an option...")

        # We want to check for if the first variable is a list. If it isn't, abort the mission, we've failed.
        self.coordinate = starting_point
        if not isinstance(self.coordinate, list):
            print("Negative starting points received. Aborting mission, over.")
            MyRover.abort_mission(self)
        else:
            print("Mar Rover 1 starting co-ordinates are: " + str(self.coordinate))

        self.direction = starting_direction
        if self.direction in valid_directions:
            print("\nMars Rover 1 is facing " + self.direction + "\n")
        else:
            print("\nDanger, danger Will Robinson! Aborting mission, over.\n")
            MyRover.abort_mission(self)

        # MyRover.await_commands(self)

    def get_commands(self):
        """The get_commands function listens for user input and reacts based on user input until quit is entered.
        USAGE: MyRover.get_commands"""
        cmd = input("F = Forward, B = Backward, L = Turn Left, R = Turn Right. String multiple letters together for "
                    "one large command (eg: ffflfrf goes forward three times, turns left, goes forward, turns right"
                    "then goes forward one more time: ")

        pass

    def move_x_axis(self, moving):
        """
        :param moving: a string of f's/b's which is converted to a list.
        :return: +1 or -1 to x axis
        """
        moving = moving.upper()
        if moving == "FORWARD":
            moving = "F"
        if moving == "BACKWARD" or moving == "BACK":
            moving = "B"

        char = []
        for i in range(len(moving)):
            char += moving[i]
        print(char)

        for i in range(len(char)):
            if char[i] == "F":
                print("Moving forward!")
                if self.coordinate[0] == self.mars.x:
                    self.coordinate[0] = 0
                else:
                    self.coordinate[0] += 1
                print("New coordinates are: " + str(self.coordinate))
                return self.coordinate[0]
            elif char[i] == "B":
                print("Moving backwards!")
                if self.coordinate[0] == 0:
                    self.coordinate[0] = self.mars.x
                else:
                    self.coordinate[0] -= 1
                print("New coordinates are: " + str(self.coordinate))
                # return self.coordinate[0]
            else:
                print("Mayday! Mayday! Incorrect movement command provided...")
                return self.coordinate[0]

    def move_y_axis(self, moving):
        moving = moving.upper()
        if moving == "RIGHT" or moving == "R":
            print("Moving right!")
            if self.coordinate[1] == 0:
                self.coordinate[1] = self.mars.y
            else:
                self.coordinate[1] += 1
            print("New coordinates are: " + str(self.coordinate))
            return self.coordinate[0]
        elif moving == str("back").upper() or moving == str("b").upper():
            print("Moving backwards!")
            self.coordinate[0] -= 1
            return self.coordinate[0]
        else:
            print("Mayday! Mayday! Incorrect movement command provided...")
            return self.coordinate[0]

    def turn_left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "W":
            self.direction = "S"
        return self.direction

    def turn_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "W":
            self.direction = "N"
        return self.direction

    def await_commands(self):
        return 100

    def abort_mission(self):
        """Call abort_mission when an unexpected value is predicted.
        The mission was a complete failure... Abort the mission, go home, you're drunk."""
        console_status = -1
        return console_status


class SurfaceOfMars:
    """SurfaceOfMars is called to define a grid for Mars. Just how big is Mars?!"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.x_obstacle = 4
        self.y_obstacle = 7
        self.obstacle_list = [[], []]
        SurfaceOfMars.plant_obstacles(self)

    def plant_obstacles(self):
        i = 0
        i2 = 0
        while i < self.x:
            self.obstacle_list[0].append(0)
            i += 1
        while i2 < self.y:
            self.obstacle_list[1].append(0)
            i2 += 1

        for i in self.obstacle_list[0]:
            if i % self.x_obstacle == 0:
                print("Ooh adding a rock")


    def confirm_mars(self):
        print("We confirm that Mars is: " + str(self.x) + " on the x axis and " + str(self.y) + " on the y axis.")
        return self.x, self.y
