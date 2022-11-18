import math


class Hermite:
    def __init__(self, sampling_points_list):
        self.sampling_points_list = sampling_points_list
        """self.xWerte = xWerte
        self.yWerte = yWerte
        self.multiplikatoren = []"""

    def ableitungsGradErkennen(self, x):
        ableitungsgrad = 1

        while True:  # mit for element in range(...) umwandeln https://www.youtube.com/watch?v=pQh5Idw2sKM&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB&index=17
            if x == 1:
                break
            else:
                while self.xWerte[x] == self.xWerte[x - 1]:
                    ableitungsgrad += 1
                    x - 1
        return ableitungsgrad

    def divided_differences(self):
        multipliers = []

        multipliers.append(self.sampling_points_list[0][1])
        k = 0
        # liste der x werte (1. wert des tupels)
        # liste der y werte (2. wert des tupels)
            # wird durch null geteilt? -> wenn x wert an stelle k = x wert an stelle k-1,
            # ja: dann in y liste der funktios-wert nicht ableitung, der eingegeben wurde
            # und wir brauchen die Ordnung der Ableitung

        for i in range(len(self.sampling_points_list)-1):
            if self.would_divide_by_zero([self.sampling_points_list[i], self.sampling_points_list[i + 1]]):
                print(1)
                 #multipliers.append(y_liste[k + 1] / math.factorial(self.ableitungsGradErkennen(len(x_list[0:k + 1]))))
            else:
                print(1)
                #generate_multiplier()
                #multipliers.append((y_liste[k + 1] - y_liste[k]) / (x_list[k + 1] - x_list[k]))

            #k += 1

        return multipliers

    def generate_multiplier(self, tuple1, tuple2):
        return (tuple2[1] - tuple1[1]) / (tuple2[0] - tuple1[0])

    def generate_coordinates_list(self, sampling_points_list):
        #@nina
        coordinates_list = []
        for i in range(len(self.sampling_points_list)-1):
            print("we are awesome")
            # vegleiche x wert an stelle i+1 mit x wert an stelle i
            # wenn identisch, packe in koordinatenliste den x wert + y wert an stelle i
        return []


    ## funktion ausmultiplizieren @mali

    def would_divide_by_zero(self, sampling_points):
        return (sampling_points[1][0] - sampling_points[0][0]) == 0

    def create_polynom(self):
        #self.divided_differences()
        return "polynom"