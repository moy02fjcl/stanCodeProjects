"""
File: draw_line.py
Name: Tracy Lee
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 20

window = GWindow()
x1 = 0
y1 = 0
x2 = 0
y2 = 0
count = 0
circle = GOval(SIZE, SIZE)


def main():
    """
    The program spawns a new window and reads where the user clicked.

    An odd number of clicks will create a circle.
    The size of the circle is determined by the constant "SIZE".

    Click an even number of times,
    the circle disappears and forms a line with the position of the previous click.
    """
    onmouseclicked(point_line)


def point_line(mouse):
    """
    This program will create a new window
    and use the variable "count" to count the number of clicks by the user.

    When "count" is an even number,
    a circle will be drawn with the user's click position as the center.
    The constant "SIZE" determines the size of the circle.

    When "count" is an odd number,
    the center of the previous circle is used as the starting point of the line segment,
    the user clicks the position to draw a line as the endpoint of the line segment,
    and the created circle is eliminated.
    """
    global x1, y1, x2, y2, count, circle
    if count % 2 == 0:
        x1 = mouse.x
        y1 = mouse.y
        count += 1
        window.add(circle, x=x1-SIZE/2, y=y1-SIZE/2)
    else:
        x2 = mouse.x
        y2 = mouse.y
        count += 1
        connect = GLine(x1, y1, x2, y2)
        window.remove(circle)
        window.add(connect)


if __name__ == "__main__":
    main()
