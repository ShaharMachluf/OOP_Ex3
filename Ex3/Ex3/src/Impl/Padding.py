class Padding:
    # Simple graph to save padding data and working area screen
    def __init__(self, left, top, right, bottom):
        self.left = left
        self.top = top
        self.right = right
        self.bottom = bottom

    def get_width(self, width):
        return width - (self.left + self.right)

    def get_height(self, height):
        return height - (self.top + self.bottom)

    def get_top(self):
        return self.top

    def get_right(self):
        return self.right
