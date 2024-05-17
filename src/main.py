from window import Window
from drawing import Line, Point


def main():
    win = Window(800, 600)

    win.draw_line(Line(Point(0, 0), Point(800, 600)), "black")

    win.draw_line(
        Line(
            Point(800, 0),
            Point(0, 600),
        ),
        "red",
    )

    win.wait_for_close()


main()
