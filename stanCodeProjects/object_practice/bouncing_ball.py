"""
File: bouncing_ball.py
Name: Tracy Lee
-------------------------
This program simulates a bouncing ball at (START_X, START_Y)
that has VX as x velocity and 0 as y velocity. Each bounce reduces
y velocity to REDUCE of itself.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)

switch = False  # Check if the ball is falling
count = 0  # Count the number of drops
vy = 0  # The speed at which the ball falls


def main():
    """
    This program will first generate a window, and generate a ball.
    The size of the window is determined by the global variable "window".
    The size of the ball is determined by the constant "SIZE",
    and the created coordinates are determined by the constants "START_X" and "START_Y".

    When the user clicks, the ball falls to the right,
    and when it hits the bottom of the screen, it bounces until it leaves the window.

    It stops working after leaving the screen three times.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(start)


def start(fall):
    """
    When the user clicks,
    the ball will start falling to the right, and the "switch" is turned on.

    When the ball leaves the screen,
    the "switch" is closed, the variable "count" plus 1,
    and a new ball is created at the initial position.

    The falling speed of the ball is controlled by the variable "vy",
    and the constant "GRAVITY" will continue to be added
    during the falling process to accelerate the falling downward.

    When it falls to the bottom of the window,
    it will bounce up and be multiplied by the constant "REDUCE"
    to simulate the reduction of energy after the ball bounces.

    When the ball is falling,
    the user clicking on the screen will not affect the falling process,
    and the variable "count" will not increase.
    """
    global vy, switch, count, ball
    switch = True
    while switch:
        if count < 3:
            vy += GRAVITY
            ball.move(VX, vy)
            pause(DELAY)
            if ball.y + ball.height >= window.height:
                if vy > 0:
                    vy *= -REDUCE
            if ball.x > window.width:
                switch = False
                count += 1
                window.remove(ball)
                break
        else:
            break
    window.add(ball, x=START_X, y=START_Y)


if __name__ == "__main__":
    main()
