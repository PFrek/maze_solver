import time
import random
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

        self.visited = False

    def draw(self):
        if not self._win:
            return

        color = "#d9d9d9"
        if self.has_left_wall:
            color = "black"

        self._win.draw_line(self._get_left_wall(), color)

        color = "#d9d9d9"
        if self.has_top_wall:
            color = "black"

        self._win.draw_line(
            self._get_top_wall(),
            color,
        )

        color = "#d9d9d9"
        if self.has_right_wall:
            color = "black"

        self._win.draw_line(
            self._get_right_wall(),
            color,
        )

        color = "#d9d9d9"
        if self.has_bottom_wall:
            color = "black"

        self._win.draw_line(
            self._get_bottom_wall(),
            color,
        )

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"

        self._win.draw_line(
            Line(self._get_center(), to_cell._get_center()), color)

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


class MazeBuilder:
    def __init__(self):
        self._origin = Point(0, 0)
        self._num_rows = 10
        self._num_cols = 10
        self._cell_width = 10
        self._cell_height = 10
        self._win = None
        self._seed = None

    def origin(self, origin):
        self._origin = origin
        return self

    def num_rows(self, num_rows):
        self._num_rows = num_rows
        return self

    def num_cols(self, num_cols):
        self._num_cols = num_cols
        return self

    def cell_width(self, cell_width):
        self._cell_width = cell_width
        return self

    def cell_height(self, cell_height):
        self._cell_height = cell_height
        return self

    def window(self, window):
        self._win = window
        return self

    def seed(self, seed):
        self._seed = seed
        return self

    def build(self):
        return Maze(
            self._origin,
            self._num_rows,
            self._num_cols,
            self._cell_width,
            self._cell_height,
            self._win,
            self._seed,
        )


class Maze:
    def __init__(
        self, origin, num_rows, num_cols, cell_width, cell_height, win=None, seed=None
    ):
        self._origin = origin
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_width = cell_width
        self._cell_height = cell_height
        self._win = win

        if seed is not None:
            random.seed(seed)

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

    def _in_bounds(self, i, j):
        if i < 0 or i >= len(self._cells):
            return False
        if j < 0 or j >= len(self._cells[i]):
            return False

        return True

    def draw(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)

    def _draw_cell(self, i, j):
        if not self._in_bounds(i, j):
            raise ValueError("draw_cell: coordinate out of bounds")

        self._cells[i][j].draw()
        self._animate()

    def _animate(self):
        if not self._win:
            return

        self._win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        entrance = (0, 0)
        self._cells[entrance[0]][entrance[1]].has_top_wall = False
        self._draw_cell(entrance[0], entrance[1])

        exit = (self._num_cols - 1, self._num_rows - 1)
        self._cells[exit[0]][exit[1]].has_bottom_wall = False
        self._draw_cell(exit[0], exit[1])

    def _get_neighbors(self, i, j):
        neighbors = [
            (i - 1, j),
            (i, j - 1),
            (i + 1, j),
            (i, j + 1),
        ]

        return list(
            sorted(filter(lambda cell: self._in_bounds(
                cell[0], cell[1]), neighbors))
        )

    def _get_direction_to_cell(self, i, j, k, l):
        if k == i - 1 and l == j:
            return "left"

        if k == i and l == j - 1:
            return "top"

        if k == i + 1 and l == j:
            return "right"

        if k == i and l == j + 1:
            return "bottom"

        return None

    def _knock_down_walls(self, i, j, k, l):
        direction = self._get_direction_to_cell(i, j, k, l)

        if direction == "left":
            self._cells[i][j].has_left_wall = False
            self._cells[k][l].has_right_wall = False

        if direction == "right":
            self._cells[i][j].has_right_wall = False
            self._cells[k][l].has_left_wall = False

        if direction == "top":
            self._cells[i][j].has_top_wall = False
            self._cells[k][l].has_bottom_wall = False

        if direction == "bottom":
            self._cells[i][j].has_bottom_wall = False
            self._cells[k][l].has_top_wall = False

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []
            neighbors = self._get_neighbors(i, j)
            for neighbor in neighbors:
                if (
                    neighbor not in to_visit
                    and not self._cells[neighbor[0]][neighbor[1]].visited
                ):
                    to_visit.append(neighbor)

            if len(to_visit) == 0:
                self._draw_cell(i, j)
                return

            other_cell = random.choice(to_visit)
            self._knock_down_walls(i, j, other_cell[0], other_cell[1])

            self._break_walls_r(other_cell[0], other_cell[1])
