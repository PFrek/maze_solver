from window import Window
from drawing import Line, Point
from maze import Maze, MazeBuilder


def main():
    win = Window(800, 600)

    maze = (
        MazeBuilder()
        .origin(Point(50, 50))
        .num_rows(10)
        .num_cols(10)
        .cell_width(30)
        .cell_height(30)
        .window(win)
        .seed(0)
        .build()
    )

    maze.draw()
    maze._break_entrance_and_exit()
    maze._break_walls_r(0, 0)

    win.wait_for_close()


main()
