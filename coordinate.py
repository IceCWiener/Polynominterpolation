class Coordinate:
    def __init__(self, x_value, y_value):
        self.x = x_value
        self.y = y_value
        self.derivatives = (0, 0)

    def set_x(self, value):
        self.x = value

    def set_y(self, value):
        self.y = value

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_derivative(self, value, order):
        self.derivative = (value, order)

    def get_derivative(self):
        return self.derivative

    def get_coordinate_tuple(self):
        return self.x, self.y
