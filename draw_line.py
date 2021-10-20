"""
File: draw_line
Name:黃稚程 mike
-------------------------
This program uses gobject in campy to draw lines on window.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# window is the canvas used to draw line
window = GWindow() 
# SIZE is the constant which is the size of the circle.
SIZE = 20
# circle_x is the global variable used to transmit the information of the x coordinate of the circle
circle_x = -100
# circle_y is the global variable used to transmit the information of the y coordinate of the circle
circle_y = -100
# circle_width is the global variable used to transmit the information of the width of the circle
circle_width = 0
# circle_height is the global variable used to transmit the information of the height of the circle
circle_height = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_circle_or_draw_line)


def draw_circle_or_draw_line(mouse):
    """
    This function will draw a circle according to the information of the mouse when user first click on the window, and
    then draw a line when user second click the mouse.
    """
    global circle_x, circle_y, circle_width, circle_height
    if circle_x == -100 and circle_y == -100:
        circle = GOval(SIZE, SIZE)
        window.add(circle, x=mouse.x-circle.width/2, y=mouse.y-circle.height/2)
        circle_x = circle.x
        circle_y = circle.y
        circle_width = circle.width
        circle_height = circle.height
    else:
        line = GLine(circle_x+circle_width/2, circle_y+circle_height/2, mouse.x, mouse.y)
        circle = window.get_object_at(circle_x+circle_width/2, circle_y+circle_height/2)
        window.remove(circle)
        window.add(line)
        circle_x = -100
        circle_y = -100


if __name__ == "__main__":
    main()
