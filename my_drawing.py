"""
File: my_drawing
Name:黃稚程 mike
----------------------
This program uses gobject in campy to draw the python logo.
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    This program will use campy to draw the python logo.
    """
    window = GWindow(1000, 1000)
    arc1 = GArc(200, 100, 0, 180, x=380, y=100)
    arc1.filled = True
    arc1.fill_color = 'dodgerblue'
    arc1.color = 'dodgerblue'
    window.add(arc1)

    rect1 = GRect(200, 50, x=380, y=126)
    rect1.filled = True
    rect1.color = 'dodgerblue'
    rect1.fill_color = 'dodgerblue'
    window.add(rect1)

    rect2 = GRect(100, 100, x=480, y=130)
    rect2.filled = True
    rect2.color = 'dodgerblue'
    rect2.fill_color = 'dodgerblue'
    window.add(rect2)

    rect3 = GRect(280, 50, x=300, y=200)
    rect3.filled = True
    rect3.color = 'dodgerblue'
    rect3.fill_color = 'dodgerblue'
    window.add(rect3)

    rect4 = GRect(280, 200, x=300, y=200)
    rect4.filled = True
    rect4.color = 'dodgerblue'
    rect4.fill_color = 'dodgerblue'
    window.add(rect4)

    arc2 = GArc(230, 200, 90, 180, x=247, y=200)
    arc2.filled = True
    arc2.fill_color = 'dodgerblue'
    arc2.color = 'dodgerblue'
    window.add(arc2)

    oval1 = GOval(300, 150, x=310, y=300)
    oval1.filled = True
    oval1.fill_color = 'white'
    oval1.color = 'white'
    window.add(oval1)

    rect6 = GRect(30, 100, x=300, y=300)
    rect6.filled = True
    rect6.color = 'dodgerblue'
    rect6.fill_color = 'dodgerblue'
    window.add(rect6)

    arc4 = GArc(190, 100, 180, 180, x=380, y=565)
    arc4.filled = True
    arc4.fill_color = 'yellow'
    arc4.color = 'yellow'
    window.add(arc4)

    rect5 = GRect(190, 50, x=380, y=540)
    rect5.filled = True
    rect5.color = 'yellow'
    rect5.fill_color = 'yellow'
    window.add(rect5)

    rect7 = GRect(90, 100, x=380, y=470)
    rect7.filled = True
    rect7.color = 'yellow'
    rect7.fill_color = 'yellow'
    window.add(rect7)

    rect8 = GRect(300, 150, x=380, y=370)
    rect8.filled = True
    rect8.color = 'yellow'
    rect8.fill_color = 'yellow'
    window.add(rect8)

    rect9 = GRect(130, 130, x=560, y=280)
    rect9.filled = True
    rect9.color = 'yellow'
    rect9.fill_color = 'yellow'
    window.add(rect9)

    arc10 = GArc(190, 240, 270, 180, x=630, y=280)
    arc10.filled = True
    arc10.fill_color = 'yellow'
    arc10.color = 'yellow'
    window.add(arc10)

    oval11 = GOval(55, 150, x=590, y=210)
    oval11.filled = True
    oval11.fill_color = 'white'
    oval11.color = 'white'
    window.add(oval11)

    rect12 = GRect(240, 50, x=410, y=320)
    rect12.filled = True
    rect12.color = 'white'
    rect12.fill_color = 'white'
    window.add(rect12)

    rect13 = GRect(250, 50, x=329, y=284)
    rect13.filled = True
    rect13.color = 'dodgerblue'
    rect13.fill_color = 'dodgerblue'
    window.add(rect13)

    rect14 = GRect(50, 213, x=580, y=120)
    rect14.filled = True
    rect14.color = 'white'
    rect14.fill_color = 'white'
    window.add(rect14)

    rect15 = GRect(30, 213, x=550, y=120)
    rect15.filled = True
    rect15.color = 'dodgerblue'
    rect15.fill_color = 'dodgerblue'
    window.add(rect15)

    rect16 = GRect(30, 200, x=639, y=280)
    rect16.filled = True
    rect16.color = 'yellow'
    rect16.fill_color = 'yellow'
    window.add(rect16)

    oval3 = GOval(30, 30, x=415, y=125)
    oval3.filled = True
    oval3.fill_color = 'white'
    oval3.color = 'white'
    window.add(oval3)

    oval4 = GOval(30, 30, x=500, y=555)
    oval4.filled = True
    oval4.fill_color = 'white'
    oval4.color = 'white'
    window.add(oval4)


if __name__ == '__main__':
    main()
