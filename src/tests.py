import unittest

from maze import Maze, MazeBuilder
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

    def test_entrace_and_exit(self):
        num_rows = 10
        num_cols = 12
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)

        m1._break_entrance_and_exit()

        self.assertFalse(m1._cells[0][0].has_top_wall)
        self.assertFalse(m1._cells[11][9].has_bottom_wall)

    def test_in_bounds(self):
        m1 = MazeBuilder().num_rows(5).num_cols(5).build()

        self.assertTrue(m1._in_bounds(0, 0))
        self.assertTrue(m1._in_bounds(4, 4))
        self.assertTrue(m1._in_bounds(0, 4))
        self.assertTrue(m1._in_bounds(4, 0))

        self.assertFalse(m1._in_bounds(-1, 0))
        self.assertFalse(m1._in_bounds(0, -1))
        self.assertFalse(m1._in_bounds(5, 0))
        self.assertFalse(m1._in_bounds(0, 5))
        self.assertFalse(m1._in_bounds(5, 5))

    def test_get_neighbors(self):
        m1 = MazeBuilder().num_rows(5).num_cols(5).build()

        self.assertEqual(m1._get_neighbors(0, 0), [(0, 1), (1, 0)])

        self.assertEqual(m1._get_neighbors(4, 4), [(3, 4), (4, 3)])

        self.assertEqual(m1._get_neighbors(4, 0), [(3, 0), (4, 1)])

        self.assertEqual(m1._get_neighbors(0, 4), [(0, 3), (1, 4)])

        self.assertEqual(
            m1._get_neighbors(3, 3),
            [
                (2, 3),
                (3, 2),
                (3, 4),
                (4, 3),
            ],
        )

    def test_reset_visited(self):
        m1 = MazeBuilder().num_rows(5).num_cols(5).build()

        m1._break_entrance_and_exit()
        m1._break_walls_r(0, 0)

        m1._reset_cells_visited()
        for i in range(len(m1._cells)):
            for j in range(len(m1._cells[i])):
                self.assertFalse(m1._cells[i][j].visited)


if __name__ == "__main__":
    unittest.main()
