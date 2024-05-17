from drawing import Line, Point


class Cell:
    def __init__(self, point_a, point_b, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

        self.__top_left = point_a
        self.__bottom_right = point_b
        self.__win = window

    def draw(self):
        if self.has_left_wall:
            self.__win.draw_line(
                self.__get_left_wall(),
                "black",
            )

        if self.has_top_wall:
            self.__win.draw_line(
                self.__get_top_wall(),
                "black",
            )

        if self.has_right_wall:
            self.__win.draw_line(
                self.__get_right_wall(),
                "black",
            )

        if self.has_bottom_wall:
            self.__win.draw_line(
                self.__get_bottom_wall(),
                "black",
            )

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"

        self.__win.draw_line(Line(self.__get_center(), to_cell.__get_center()), color)

    def __get_center(self):
        width = self.__bottom_right.x - self.__top_left.x
        height = self.__bottom_right.y - self.__top_left.y

        return Point(self.__top_left.x + (width / 2), self.__top_left.y + (height / 2))

    def __get_left_wall(self):
        return Line(
            self.__top_left,
            Point(self.__top_left.x, self.__bottom_right.y),
        )

    def __get_top_wall(self):
        return Line(
            self.__top_left,
            Point(self.__bottom_right.x, self.__top_left.y),
        )

    def __get_right_wall(self):
        return Line(
            Point(self.__bottom_right.x, self.__top_left.y),
            self.__bottom_right,
        )

    def __get_bottom_wall(self):
        return Line(
            Point(self.__top_left.x, self.__bottom_right.y),
            self.__bottom_right,
        )
