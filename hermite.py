import math
from utility import Utility


class Hermite:

    def __init__(self):
        self.coefficients = None
        self.pyramid_matrix = []
        self.x_values = []
        self.y_values = []

        self.ut = Utility()

    def get_coefficients(self, xy_list):
        y_values = self.ut.get_y_values(xy_list)
        x_values = self.ut.get_x_values(xy_list)
        self.coefficients = self.hermite_divided_differences(
            x_values, y_values, xy_list)
        return self.coefficients

    def hermite_divided_differences(self, x_values, y_values, xy_list):
        n = len(y_values)  # n-1 = Grad des Polynoms

        # Erstelle eine mit Nullern gefüllte Matrix
        pyramid_matrix = []

        for i in range(n):
            pyramid_matrix.append([])
            for j in range(n):
                pyramid_matrix[i].append(0.)

        # erste Spalte der Pyramide wird mit y-Werten gefüllt
        for i in range(n):
            pyramid_matrix[i][0] = float(y_values[i])

        for j in range(1, n):
            for i in range(n - j):
                # Spalten werden nacheinander von berechneten Koeffizienten gefüllt
                if(i + j) < len(x_values):
                    if (x_values[i + j] - x_values[i]) == 0:
                        pyramid_matrix[i][j] = self.get_derivation_value(
                            xy_list, x_values[i], j) / math.factorial(j)
                    else:
                        pyramid_matrix[i][j] = (
                            pyramid_matrix[i + 1][j - 1] - pyramid_matrix[i][j - 1]) / (x_values[i + j] - x_values[i])
        self.pyramid_matrix = pyramid_matrix
        return pyramid_matrix[0]  # erste Reihe wird zurückgegeben

    def get_derivation_value(self, xy_list, x_values, step):
        derivation_value = 0
        for i in range(len(xy_list) - 1):
            if xy_list[i][0] == x_values:
                derivation_value = xy_list[i + step][1]
                break
        return derivation_value
