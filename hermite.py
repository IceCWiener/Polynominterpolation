from coordinate_list import CoordinateList

class Hermite:
    def __init__(self, sampling_points_list):
        self.sampling_points_list = sampling_points_list

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

        for i in range(len(self.sampling_points_list)):
            multipliers.append(self.get_multiplier(self.sampling_points_list[i], self.sampling_points_list[i - 1]))

        return multipliers

    def get_multiplier(self, tuple1, tuple2):
        if self.would_divide_by_zero(tuple1, tuple2):
            return 4.0
        return (tuple2[1] - tuple1[1]) / (tuple2[0] - tuple1[0])

    def generate_coordinate_list(self):
        coordinate_list = CoordinateList(self.sampling_points_list)
        return coordinate_list.get_coordinates()

    ## funktion ausmultiplizieren @mali

    def would_divide_by_zero(self, tuple1, tuple2):
        return (tuple2[0] - tuple1[0]) == 0

    def create_polynom(self):
        #self.divided_differences()
        return "polynom"
