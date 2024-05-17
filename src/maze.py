import time
from drawing import Line, Point


class Cell:
    def __init__(self, point_a, point_b, window=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self._top_left = point_a
        self._bottom_right = point_b
        self._win = window

    def draw(self):
        if self.has_left_wall:
            self._win.draw_line(
                self._get_left_wall(),
                "black",
            )

        if self.has_top_wall:
            self._win.draw_line(
                self._get_top_wall(),
                "black",
            )

        if self.has_right_wall:
            self._win.draw_line(
                self._get_right_wall(),
                "black",
            )

        if self.has_bottom_wall:
            self._win.draw_line(
                self._get_bottom_wall(),
                "black",
            )

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"

        self._win.draw_line(Line(self._get_center(), to_cell._get_center()), color)

    def _get_center(self):
        width = self._bottom_right.x - self._top_left.x
        height = self._bottom_right.y - self._top_left.y

        return Point(self._top_left.x + (width / 2), self._top_left.y + (height / 2))

    def _get_left_wall(self):
        return Line(
            self._top_left,
            Point(self._top_left.x, self._bottom_right.y),
        )

    def _get_top_wall(self):
        return Line(
            self._top_left,
            Point(self._bottom_right.x, self._top_left.y),
        )

    def _get_right_wall(self):
        return Line(
            Point(self._bottom_right.x, self._top_left.y),
            self._bottom_right,
        )

    def _get_bottom_wall(self):
        return Line(
            Point(self._top_left.x, self._bottom_right.y),
            self._bottom_right,
        )


class Maze:
    def __init__(self, origin, num_rows, num_cols, cell_width, cell_height, win=None):
        self._origin = origin
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._win = win

        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self._num_cols):
            col = []
            for j in range(self._num_rows):
                top_left = Point(
                    self._origin.x + (self._cell_width * i),
                    self._origin.y + (self._cell_height * j),
                )

                bottom_right = Point(
                    top_left.x + self._cell_width,
                    top_left.y + self._cell_height,
                )

                cell = Cell(top_left, bottom_right, self._win)
                col.append(cell)
            self._cells.append(col)

    def _draw_cell(self, i, j):
        if i < 0 or i >= len(self._cells):
            raise ValueError("draw_cell: i coordinate out of bounds")

        if j < 0 or j >= len(self._cells[i]):
            raise ValueError("draw_cell: j coordinate out of bounds")

        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        self._win.redraw()
        time.sleep(0.05)
