"""
File: bouncing_ball
Name:黃稚程 mike
-------------------------
This program uses campy to simulate the process of a bouncing ball.
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
# on_off is the global variable used to decide whether activate the process of bouncing ball or not
on_off = 0
# VY is the global variable which is the velocity of y coordinate
VY = 0
# number is the global variable used to count who many times activating the bouncing ball code
number = 1
window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
ball.filled = True
ball.fill_color = 'black'
window.add(ball)


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    onmouseclicked(game_start)


def game_start(mouse):
    """
    This program simulate the process of bouncing ball but the user cannot activate the code after 3 times.
    """
    global on_off, VY, number
    if number < 4:
        if on_off == 0:
            on_off += 1
            while ball.x <= window.width:
                if VY >= 0:
                    if ball.y <= window.height:
                        ball.move(VX, VY)
                        pause(DELAY)
                        VY += GRAVITY
                    else:
                        VY = (-VY) * REDUCE
                else:
                    ball.move(VX, VY)
                    pause(DELAY)
                    VY += GRAVITY
            window.add(ball, x=START_X, y=START_Y)
            VY = 0
            on_off = 0
            number += 1
    else:
        pass


if __name__ == "__main__":
    main()
