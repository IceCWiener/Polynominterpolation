class Coordinate:
    def __init__(self, x_value, y_value):
        self.x = x_value
        self.y = y_value
        self.derivatives = []

    def set_x(self, value):
        self.x = value

    def set_y(self, value):
        self.y = value

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_derivatives(self, value, order):
        self.derivatives = (value, order)

    def get_derivatives(self):
        return self.derivatives

    def get_coordinate_tuple(self):
        return self.x, self.y
