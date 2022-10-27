"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:
    """
    This class will create a new window and draw the basic configuration of breakout.py,
    including bricks, boards, and a ball.
    """

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle_offset = paddle_offset
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2,
                        y=self.window.height-(self.paddle_offset+self.paddle.height))

        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2,
                        y=(self.window.height-self.ball.height)/2)

        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED

        # Initialize our mouse listeners
        self.__switch = False
        onmousemoved(self.paddle_move)
        onmouseclicked(self.start)

        # Draw bricks
        brick_spacing = (self.window.width - brick_width * brick_cols) / (brick_cols-1)
        for i in range(brick_rows):
            for j in range(brick_cols):
                brick = GRect(brick_width, brick_height)
                self.window.add(brick, x=brick.x, y=brick_offset)
                brick.x = (brick_spacing + brick_width) * j
                brick.y += (brick_spacing + brick_height) * i
                brick.filled = True
                if i < 2:
                    brick.color = "lightcyan"
                    brick.fill_color = "lightcyan"
                elif i < 4:
                    brick.color = "paleturquoise"
                    brick.fill_color = "paleturquoise"
                elif i < 6:
                    brick.color = "darkturquoise"
                    brick.fill_color = "darkturquoise"
                elif i < 8:
                    brick.color = "lightseagreen"
                    brick.fill_color = "lightseagreen"
                elif i < 10:
                    brick.color = "darkcyan"
                    brick.fill_color = "darkcyan"
                else:
                    brick.color = "darkslategrey"
                    brick.fill_color = "darkslategrey"

        self._num_of_bricks = brick_rows * brick_cols
        self.paddle_or_brick = None

    def paddle_move(self, event):
        """
        Move the paddle according to the position of the mouse.
        The position indicated by the mouse is the center of the paddle.

        The height of the paddle does not change
        and does not extend beyond the viewing window.

        :param event: mouse.x
        :return: paddle.x
        """
        if self.paddle.width / 2 <= event.x <= self.window.width - self.paddle.width / 2:
            self.paddle.x = event.x-self.paddle.width/2
            self.paddle.y = self.window.height-(self.paddle_offset+self.paddle.height)

    def start(self, click):
        """
        Turn on the switch to ensure the user clicks to start the game.

        :return: bool; Turn on the switch.
        """
        self.__switch = True

    def turn_off(self):
        """
        Turn off the switch to ensure the user clicks again to enter the game.

        :return: bool; Turn off the switch.
        """
        self.__switch = False

    @property
    def dx(self):
        """
        A getter function that allows the user to get the default value of x.

        :return: int; a random number with a minimum value of 1
                      and a maximum value of the constant "MAX_X_SPEED",
                      with a half chance of making dx the opposite.
        """
        return self.__dx

    @dx.setter
    def dx(self, new_dx):
        """
        A setter function that resets the default value of x.

        :param new_dx: int; a new default value of x.
        """
        self.__dx = new_dx

    @property
    def dy(self):
        """
        A getter function that allows the user to get the default value of y.

        :return: int; a fixed number determined by the constant "INITIAL_Y_SPEED".
        """
        return self.__dy

    @dy.setter
    def dy(self, new_dy):
        """
        A setter function that resets the default value of y.

        :param new_dy: int; a new default value of y.
        """
        self.__dy = new_dy

    def get_switch(self):
        """
        A getter function that allows the user to use the switch.

        :return: bool; It's "False" before the user click.
        """
        return self.__switch

    def get_num_of_bricks(self):
        """
        A getter function that allows the user to get the default value of the bricks.

        :return: int; Multiply the columns of bricks by the rows to get the number of the bricks.
        """
        return self._num_of_bricks

    def meet(self):
        """
        This program sets the four corners of the ball as decision points.

        When any decision point hits an object,
        pass the hit object to "paddle_or_brick" and return True.

        If none of the four decision points hit the object, return False.

        :return: bool; Determine if the ball has hit an object.
        """
        left_top_x = self.ball.x
        left_top_y = self.ball.y

        right_top_x = self.ball.x + self.ball.width
        right_top_y = self.ball.y

        left_bottom_x = self.ball.x
        left_bottom_y = self.ball.y + self.ball.height

        right_bottom_x = self.ball.x + self.ball.width
        right_bottom_y = self.ball.y + self.ball.height

        maybe_left_top = self.window.get_object_at(left_top_x, left_top_y)
        maybe_right_top = self.window.get_object_at(right_top_x, right_top_y)
        maybe_left_bottom = self.window.get_object_at(left_bottom_x, left_bottom_y)
        maybe_right_bottom = self.window.get_object_at(right_bottom_x, right_bottom_y)

        if maybe_left_top is not None:
            self.paddle_or_brick = maybe_left_top
            return True
        elif maybe_right_top is not None:
            self.paddle_or_brick = maybe_right_top
            return True
        elif maybe_left_bottom is not None:
            self.paddle_or_brick = maybe_left_bottom
            return True
        elif maybe_right_bottom is not None:
            self.paddle_or_brick = maybe_right_bottom
            return True
        else:
            return False

    def remove(self):
        """
        This program will determine whether the hit object is a paddle.

        If it is not, it means that the hit object is a brick, then it will be eliminated.
        If it is a paddle, return True.

        :return: bool; Indicates that the hit object is a paddle.
        """
        if self.paddle_or_brick is not self.paddle:
            self.window.remove(self.paddle_or_brick)
        else:
            return True

    def reset(self):
        """
        The ball will return to its original position
        when the user loses a life or ends the game.
        """
        self.window.add(self.ball, x=(self.window.width - self.ball.width) / 2,
                        y=(self.window.height - self.ball.height) / 2)
        self.__dx = random.randint(1, MAX_X_SPEED)
        if random.random() > 0.5:
            self.__dx = -self.__dx
        self.__dy = INITIAL_Y_SPEED
