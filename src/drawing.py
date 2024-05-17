class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, point_a, point_b):
        self.a = point_a
        self.b = point_b

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=3
        )
