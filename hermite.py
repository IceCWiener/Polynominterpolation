from coordinate import Coordinate

class Hermite:
    def __init__(self, sampling_points_list):
        self.sampling_points_list = sampling_points_list
        self.coordinates_list = []

    # def ableitungsGradErkennen(self, x):
    #     ableitungsgrad = 1
    #
    #     while True:  # mit for element in range(...) umwandeln https://www.youtube.com/watch?v=pQh5Idw2sKM&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB&index=17
    #         if x == 1:
    #             break
    #         else:
    #             while self.xWerte[x] == self.xWerte[x - 1]:
    #                 ableitungsgrad += 1
    #                 x - 1
    #     return ableitungsgrad

    def get_multipliers(self):
        multipliers = []
        coordinates_list = self.set_coordinates_list()

        for i in range(len(self.coordinates_list)):
            if i == 0:
                multipliers.append(self.coordinates_list[0].get_y())
            multipliers.append(self.get_multiplier(self.coordinates_list[i], self.coordinates_list[i - 1]))

        return multipliers

    def get_multiplier(self, coordinate1, coordinate2):
        if self.would_divide_by_zero(coordinate1, coordinate2):
            return 4.0
        return (coordinate2[1] - coordinate1[1]) / (coordinate2[0] - coordinate1[0])

    def set_coordinates_list(self):
        for i in range(len(self.sampling_points_list)):
            coordinate = Coordinate(self.sampling_points_list[i][0], self.sampling_points_list[i][1])
            self.coordinates_list.append(coordinate)
            if self.is_same_x_value(self.coordinates_list[i], self.coordinates_list[i-1]):
                coordinate.set_x(self.coordinates_list[i-1].get_x())
                coordinate.set_y(self.coordinates_list[i-1].get_y())
                coordinate.set_derivative(self.sampling_points_list[i][1], 1)

    def get_coordinates_as_list_of_tuples(self):
        tuple_list = []
        for coordinate in self.coordinates_list:
            tuple_list.append(coordinate.get_coordinate_tuple())
        return tuple_list

    def get_coordinates_list(self):
        self.set_coordinates_list()
        return self.get_coordinates_as_list_of_tuples()

    ## funktion ausmultiplizieren @mali

    def would_divide_by_zero(self, tuple1, tuple2):
        return (tuple2[0] - tuple1[0]) == 0

    def is_same_x_value(self, coordinate1, coordinate2):
        return coordinate1.get_x() == coordinate2.get_x()

    def create_polynom(self):
        #self.divided_differences()
        return "polynom"
