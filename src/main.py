from window import Window
from drawing import Line, Point
from maze import Cell


def main():
    win = Window(800, 600)

    cell_info = [
        ((10, 10), (30, 30)),
        ((40, 10), (60, 30)),
        ((70, 10), (90, 30)),
        ((100, 10), (120, 30)),
        ((130, 10), (150, 30)),
    ]

    cells = []
    for info in cell_info:
        cells.append(
            Cell(Point(info[0][0], info[0][1]), Point(info[1][0], info[1][1]), win)
        )

    for i in range(len(cells)):
        cells[i].draw()
        if i + 1 < len(cells):
            cells[i].draw_move(cells[i + 1], i % 2 == 0)

    win.wait_for_close()


main()
