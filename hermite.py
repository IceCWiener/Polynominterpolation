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
        self.set_coordinates_list()

        for i in range(len(self.coordinates_list)):
            if i == 0:
                multipliers.append(self.coordinates_list[0].get_y())
            multipliers.append(self.get_multiplier(self.coordinates_list[i], self.coordinates_list[i - 1]))

        return multipliers

    def get_multiplier(self, tuple1, tuple2):
        if self.is_same_x_value(tuple1, tuple2):
            return 4.0
        return (tuple2[1] - tuple1[1]) / (tuple2[0] - tuple1[0])

    def set_coordinates_list(self):
        for i in range(len(self.sampling_points_list)):
            coordinate = Coordinate(self.sampling_points_list[i][0], self.sampling_points_list[i][1])
            self.coordinates_list.append(coordinate)
            if self.is_same_x_value(self.coordinates_list[i], self.coordinates_list[i-1]):
                coordinate.set_x(self.coordinates_list[i-1].get_x())
                coordinate.set_y(self.coordinates_list[i-1].get_y())
                coordinate.set_derivative(self.sampling_points_list[i][1], 1)

    def get_coordinates_list_as_list_of_tuples(self):
        self.set_coordinates_list()
        tuple_list = []
        for coordinate in self.coordinates_list:
            tuple_list.append(coordinate.get_coordinate_tuple())
        return tuple_list

    def get_coordinates_list(self):
        self.set_coordinates_list()
        return self.coordinates_list

    ## funktion ausmultiplizieren @mali

    def is_same_x_value_2(self, tuple1, tuple2):
        return (tuple2[0] - tuple1[0]) == 0

    def is_same_x_value(self, coordinate1, coordinate2):
        return coordinate1.get_x() == coordinate2.get_x()

    def create_polynom(self):
        #self.divided_differences()
        return "polynom"
