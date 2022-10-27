"""
File: my_drawing.py
Name: Tracy Lee
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel, GArc, GPolygon
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Why it doesn't work...?

    This is what I look like when the program doesn't work. (TAT)
    """
    window = GWindow(300, 300, title="Why it doesn't work?")
    bg = GRect(310, 310, x=-5, y=-5)
    window.add(bg)

    table = GRect(310, 75, x=-5, y=230)
    table.filled = True
    table.fill_color = "burlywood"
    window.add(table)

    laptop1 = GPolygon()
    laptop1.add_vertex((280, 190))
    laptop1.add_vertex((200, 200))
    laptop1.add_vertex((190, 270))
    laptop1.add_vertex((270, 260))
    laptop1.filled = True
    laptop1.fill_color = "dimgray"
    window.add(laptop1)

    laptop2 = GPolygon()
    laptop2.add_vertex((155, 240))
    laptop2.add_vertex((190, 270))
    laptop2.add_vertex((195, 235))
    laptop2.filled = True
    laptop2.fill_color = "dimgray"
    window.add(laptop2)

    face = GOval(80, 50)
    face.filled = True
    face.fill_color = "white"
    window.add(face, x=70, y=180)

    body = GArc(80, 60, 0, 90)
    body.filled = True
    body.fill_color = "white"
    body.color = "white"
    window.add(body, x=100, y=214)

    body_line = GArc(80, 60, 0, 50)
    window.add(body_line, x=126, y=216)

    face_on_table = GArc(55, 35, 80, 260)
    face_on_table.filled = True
    face_on_table.fill_color = "white"
    face_on_table.color = "white"
    window.add(face_on_table, x=60, y=200)

    face_on_table_line = GArc(55, 35, 110, 210)
    window.add(face_on_table_line, x=62, y=201)

    r_ear = GOval(23, 8)
    r_ear.filled = True
    r_ear.fill_color = "white"
    window.add(r_ear, x=85, y=177)

    l_ear = GArc(23, 9, 0, 270)
    l_ear.filled = True
    l_ear.color = "white"
    l_ear.fill_color = "white"
    window.add(l_ear, x=95, y=176)

    l_ear_line = GArc(23, 8, -30, 300)
    window.add(l_ear_line, x=95, y=175)

    r_eye = GOval(3, 3)
    r_eye.filled = True
    window.add(r_eye, x=92, y=200)

    l_eye = GOval(3, 3)
    l_eye.filled = True
    window.add(l_eye, x=113, y=195)

    nose = GOval(2, 1)
    nose.filled = True
    window.add(nose, x=103, y=201)

    mouth = GPolygon()
    mouth.add_vertex((99, 205))
    mouth.add_vertex((112, 202))
    mouth.add_vertex((108, 213))
    mouth.filled = True
    window.add(mouth)

    teeth = GPolygon()
    teeth.add_vertex((98, 205))
    teeth.add_vertex((102, 208))
    teeth.add_vertex((111, 206))
    teeth.add_vertex((111, 202))
    teeth.filled = True
    teeth.fill_color = "white"
    window.add(teeth)

    cheek = GArc(56, 40, 0, 100)
    window.add(cheek, x=76, y=205)

    confused_top = GArc(46, 20, -60, 240)
    window.add(confused_top, x=38, y=113)

    confused1 = GOval(40, 15)
    window.add(confused1, x=40, y=120)

    confused2 = GOval(36, 12)
    window.add(confused2, x=42, y=128)

    confused3 = GOval(31, 9)
    window.add(confused3, x=44, y=131)

    confused4 = GOval(28, 7)
    window.add(confused4, x=47, y=138)

    confused5 = GOval(23, 5)
    window.add(confused5, x=49, y=144)

    confused6 = GOval(18, 4)
    window.add(confused6, x=51, y=149)

    confused_bottom = GArc(15, 9, -90, 230)
    window.add(confused_bottom, x=53, y=149)

    think = GLabel("Why....", x=140, y=170)
    think.font = "Indie Flower-20-bold"
    window.add(think)


if __name__ == '__main__':
    main()
