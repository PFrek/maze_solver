from window import Window
from drawing import Line, Point
from maze import Maze


def main():
    win = Window(800, 600)

    maze = Maze(Point(50, 50), 5, 5, 30, 30, win)

    maze.draw()

    win.wait_for_close()


main()
