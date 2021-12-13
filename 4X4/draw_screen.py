import math
from turtle import Turtle, Screen, onscreenclick
from time import sleep

DARK = (60, 60, 60)
DIMENSION = 4  # i.e. 4 = 4 x 4 grid
WINDOW_SIZE = 600
GRID_SIZE = round(WINDOW_SIZE * 6 / 7)  # Leaves an empty border around the outside of the grid
BORDER_LINE_COORD = round(GRID_SIZE / 2)
GRID_LINE_INCREMENT = round(GRID_SIZE / DIMENSION)
PADDING = GRID_LINE_INCREMENT * 0.15
X_TOP_LEFT = BORDER_LINE_COORD - PADDING
X_SIZE = GRID_LINE_INCREMENT - PADDING * 2
O_CENTER_X = BORDER_LINE_COORD - GRID_LINE_INCREMENT / 2
O_START_Y = BORDER_LINE_COORD - GRID_LINE_INCREMENT + PADDING
O_RADIUS = X_SIZE / 2
GRID_OFFSET = BORDER_LINE_COORD - GRID_LINE_INCREMENT


class DrawScreen:
    # Since turtle.Screen() returns a singular object, we cannot inherit from Screen
    def __init__(self):
        self.window = Screen()
        self.tim = Turtle()

    def screen_setup(self):
        """
        Basic window setup

        :return: nothing
        """
        self.window.setup(WINDOW_SIZE, WINDOW_SIZE, 400, 300)
        self.window.colormode(255)
        self.window.bgcolor(DARK)

    def draw_outline(self):
        """
        Draw the game_state grid layout

        :return: nothing
        """

        def draw_border():
            """Draw the border"""
            self.tim.width(4)
            self.tim.pu()
            self.tim.goto(-BORDER_LINE_COORD, BORDER_LINE_COORD)
            self.tim.pd()
            self.tim.goto(-BORDER_LINE_COORD, -BORDER_LINE_COORD)
            self.tim.goto(BORDER_LINE_COORD, -BORDER_LINE_COORD)
            self.tim.goto(BORDER_LINE_COORD, BORDER_LINE_COORD)
            self.tim.goto(-BORDER_LINE_COORD, BORDER_LINE_COORD)

        def draw_gridlines():
            """Draw the grid lines"""
            self.tim.width(2)
            for coord in range(-BORDER_LINE_COORD + GRID_LINE_INCREMENT, BORDER_LINE_COORD, GRID_LINE_INCREMENT):
                # Draw the vertical line
                self.tim.pu()
                self.tim.goto(coord, BORDER_LINE_COORD)
                self.tim.pd()
                self.tim.goto(coord, -BORDER_LINE_COORD)
                # Draw the horizontal line
                self.tim.pu()
                self.tim.goto(-BORDER_LINE_COORD, coord)
                self.tim.pd()
                self.tim.goto(BORDER_LINE_COORD, coord)

        self.window.tracer(0)
        self.tim.hideturtle()
        draw_border()
        draw_gridlines()
        self.window.tracer(1)

    def draw_x(self, row: int, col: int):
        """
        Draw an X on the window

        :param row: x coordinate of the array
        :param col: y coordinate of the array
        :return: nothing
        """
        self.window.tracer(0)
        start_x = col * GRID_LINE_INCREMENT - X_TOP_LEFT
        start_y = X_TOP_LEFT - row * GRID_LINE_INCREMENT
        self.tim.hideturtle()
        self.tim.width(4)
        self.tim.color('white')
        self.tim.pu()
        self.tim.goto(start_x, start_y)
        self.tim.pd()
        self.tim.goto(start_x + X_SIZE, start_y - X_SIZE)
        self.tim.pu()
        self.tim.goto(start_x + X_SIZE, start_y)
        self.tim.pd()
        self.tim.goto(start_x, start_y - X_SIZE)
        self.window.tracer(1)

    def draw_o(self, row, col):
        """
        Draw an O on the window

        :param row: x coordinate of the array
        :param col: y coordinate of the array
        :return: nothing
        """
        self.window.tracer(0)
        start_x = col * GRID_LINE_INCREMENT - O_CENTER_X
        start_y = O_START_Y - row * GRID_LINE_INCREMENT
        self.tim.hideturtle()
        self.tim.width(4)
        self.tim.color('white')
        self.tim.pu()
        self.tim.goto(start_x, start_y)
        self.tim.pd()
        self.tim.circle(O_RADIUS)
        self.window.tracer(1)


# --------------------------------- TEST CODE ---------------------------------
def test_get_mouse_click(x, y):
    global last_drawn
    print(x, y)  # mouse coordinates
    if -BORDER_LINE_COORD < x < BORDER_LINE_COORD and -BORDER_LINE_COORD < y < BORDER_LINE_COORD:
        # Convert mouse coordinates to row, col of the grid
        # Distance from center to first gid line = 100
        row, col = (math.ceil((GRID_OFFSET - y) / GRID_LINE_INCREMENT),
                    math.ceil((GRID_OFFSET + x) / GRID_LINE_INCREMENT))
        print(row, col)
        if last_drawn == "X":
            screen.draw_o(row, col)
            last_drawn = "O"
        else:
            screen.draw_x(row, col)
            last_drawn = "X"
    else:
        print('Outside grid.')


def test():
    # Test drawing the window and using mouse clicks

    screen.screen_setup()
    screen.draw_outline()
    while True:
        sleep(0.5)
        screen.window.update()


if __name__ == '__main__':
    last_drawn = "O"
    screen = DrawScreen()
    onscreenclick(test_get_mouse_click)
    test()
    screen.window.exitonclick()
