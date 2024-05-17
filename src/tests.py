import unittest

from maze import Maze
from drawing import Point


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_single_cell(self):
        num_rows = 1
        num_cols = 1
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(len(m1._cells[0]), num_rows)

    def test_maze_create_many_cells(self):
        num_rows = 100
        num_cols = 80
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)

        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(len(m1._cells[0]), num_rows)


if __name__ == "__main__":
    unittest.main()
