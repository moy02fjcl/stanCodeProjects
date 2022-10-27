"""
File: sierpinski.py
Name: Tracy Lee
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	The program recursively prints the Sierpinski triangle on GWindow.
	The user will see the Sierpinski Triangle on the GWindow
	that the number of layers is determined by the constant ORDER
	and the side length is the constant LENGTH.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int; The order of the Sierpinski Triangle.
	:param length: int; The length of the order 1 Sierpinski Triangle.
	:param upper_left_x: int; The upper left x coordinate of order 1 Sierpinski Triangle.
	:param upper_left_y: int; The upper left y coordinate of order 1 Sierpinski Triangle.

	This helper function will draw the triangle recursively
	starting from the upper left corner until reaching the target level.
	"""
	if order == 0:
		pass
	else:
		top = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		left = GLine(upper_left_x, upper_left_y, upper_left_x + (length * 0.5), upper_left_y + (length * 0.866))
		right = GLine(upper_left_x + length, upper_left_y, upper_left_x + (length * 0.5), upper_left_y + (length * 0.866))
		window.add(top)
		window.add(left)
		window.add(right)

		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 2, upper_left_y)
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length / 4, upper_left_y + (length * 0.866 / 2))


if __name__ == '__main__':
	main()