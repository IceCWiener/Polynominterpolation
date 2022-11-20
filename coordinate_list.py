from coordinate import Coordinate


class CoordinateList:
    def __init__(self, sampling_points_list):
        self.sampling_points_list = sampling_points_list
        self.coordinates_list = []

    def get_coordinates(self):
        self.set_coordinates()
        return self.get_coordinates_as_list_of_coordinate()

    def get_coordinates_as_list_of_coordinate(self):
        tuple_list = []
        for coordinate in self.coordinates_list:
            tuple_list.append(coordinate.get_coordinate_tuple())

        return tuple_list

    def is_same_x_value(self, coordinate1, coordinate2):
        return coordinate1.get_x() == coordinate2.get_x()

    def set_coordinates(self):
        for i in range(len(self.sampling_points_list)):
            coordinate = Coordinate(self.sampling_points_list[i][0], self.sampling_points_list[i][1])
            self.coordinates_list.append(coordinate)
            if self.is_same_x_value(self.coordinates_list[i], self.coordinates_list[i-1]):
                coordinate.set_x(self.coordinates_list[i-1].get_x())
                coordinate.set_y(self.coordinates_list[i-1].get_y())
                coordinate.set_derivative(self.sampling_points_list[i][1], 1)



