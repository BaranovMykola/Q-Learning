class action:

    def __init__(self, name, dx=0, dy=0):
        self.dx = dx
        self.dy = dy
        self.name = name

    def __eq__(self, other):
        return self.dx == other.dx and self.dy == other.dy and self.name == other.name