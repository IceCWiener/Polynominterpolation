import math
from coordinate import Coordinate


class Hermite:
    def __init__(self, sampling_points_list):
        self.sampling_points_list = sampling_points_list
        self.coordinates_list = []

    def determine_derivative_order(self, list_of_points):
        derivative_order = 0
        for i in range(len(list_of_points)-1):
            if self.is_same_x_value_tuple(list_of_points[i], list_of_points[i+1]):
                derivative_order += 1

        return derivative_order

    def get_multipliers(self):
        multipliers = []
        self.set_coordinates_list()

        for i in range(len(self.sampling_points_list)-1):
            if i == 0:
                multipliers.append(float(self.coordinates_list[0].get_y()))
            multipliers.append(self.get_multiplier(self.coordinates_list[i], self.coordinates_list[i - 1]))

        return multipliers

    def get_multiplier(self, coordinate1, coordinate2):
        # TODO: pyramiden system: wir müssen bis zum äußersten punkt gehen für die dividierte differenz
        if self.is_same_x_value(coordinate1, coordinate2):
            derivative_value = coordinate1.get_derivatives()[0]
            derivative_order = coordinate1.get_derivatives()[1]
            return derivative_value / math.factorial(derivative_order)
        return (coordinate2.get_y() - coordinate1.get_y()) / (coordinate2.get_x() - coordinate1.get_x())

    def set_coordinates_list(self):
        for i in range(len(self.sampling_points_list)):
            coordinate = Coordinate(self.sampling_points_list[i][0], self.sampling_points_list[i][1])
            self.coordinates_list.append(coordinate)

            if self.is_same_x_value(self.coordinates_list[i-1], self.coordinates_list[i]):
                same_x_value_list = []
                same_x_value_list.append(self.sampling_points_list[i])
                #todo break falls 2 verschiedene listen mit gleichen x werten

                coordinate.set_x(self.coordinates_list[i-1].get_x())
                coordinate.set_y(self.coordinates_list[i-1].get_y())
                #TODO: 2. Ableitung und y wert des ersten Koordinaten, bzw ... 3. Ableitung...
                # coordinatenliste übergeben, funktion die zählt wie viele gleiche Werte eingegeben wurden, und positionen in der liste an denen die tupel sind
                # [(2,4) (2,5) (2,8)] => return 2, und pos von (2,4), also hier pos = 0
                derivative_order = self.determine_derivative_order(same_x_value_list)

                coordinate.set_derivatives(self.sampling_points_list[i][1], derivative_order)
                self.coordinates_list[i-1].set_derivatives(self.sampling_points_list[i][1], derivative_order)

    def get_coordinates_list_as_list_of_tuples(self):
        tuple_list = []
        for coordinate in self.coordinates_list:
            tuple_list.append(coordinate.get_coordinate_tuple())
        return tuple_list

    def get_coordinates_list(self):
        return self.coordinates_list

    ## funktion ausmultiplizieren @mali

    def is_same_x_value_tuple(self, tuple1, tuple2):
        return (tuple2[0] - tuple1[0]) == 0

    def is_same_x_value(self, coordinate1, coordinate2):
        return coordinate1.get_x() == coordinate2.get_x()

    def create_polynom(self):
        #self.divided_differences()
        # multipliers = self.get_multipliers()
        return " "
