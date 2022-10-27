"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    """
    This program is a game, and the user clicks on the screen to start the game.

    If the ball hits the top, left, and right side of the window, the paddle will bounce;
    hitting a brick will eliminate the brick and bounce;
    if the ball falls below the window, the number of lives will be reduced by one.

    The number of lives of the user is determined by the constant "NUM_LIVES",
    the game is over if the lives are exhausted or all the bricks are eliminated.
    """
    graphics = BreakoutGraphics()

    life = NUM_LIVES
    num_of_bricks = graphics.get_num_of_bricks()

    # Add the animation loop here!
    while True:
        pause(FRAME_RATE)
        dx = graphics.dx
        dy = graphics.dy
        while graphics.get_switch():
            if life > 0:
                if num_of_bricks > 0:
                    graphics.ball.move(dx, dy)
                    if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                        graphics.dx = -dx
                        dx = graphics.dx
                    if graphics.ball.y <= 0:
                        graphics.dy = -dy
                        dy = graphics.dy
                    if graphics.ball.y >= graphics.window.height:
                        life -= 1
                        graphics.reset()
                        graphics.turn_off()
                        break
                    if graphics.meet():
                        dy = -dy
                        graphics.remove()
                        if graphics.paddle_or_brick is not graphics.paddle:
                            num_of_bricks -= 1
                        if graphics.remove():
                            # Avoid bouncing the ball repeatedly inside the board as it hits the board.
                            if dy > 0:
                                dy = -dy
                else:
                    graphics.reset()
                    graphics.turn_off()
                    break
            else:
                break
            pause(FRAME_RATE)


if __name__ == '__main__':
    main()
