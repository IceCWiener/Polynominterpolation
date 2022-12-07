import math
import numpy as np


class Hermite:

    def __init__(self):
        self.coefficients = None
        self.pyramid_matrix = []
        self.x_values = []
        self.y_values = []

    def get_coefficients(self, xy_list):
        y_values = self.get_y_values(xy_list)
        x_values = self.get_x_values(xy_list)
        self.coefficients = self.divided_differences(x_values, y_values, xy_list)
        return self.coefficients

    def get_y_values(self, xy_list):
        y_values = []
        i = 0

        while i < len(xy_list) - 1:
            if xy_list[i][0] == xy_list[i + 1][0]:
                for j in range(len(xy_list) - 1, i, -1):
                        if i >= len(xy_list):
                            return y_values
                        if xy_list[i][0] == xy_list[j][0]:
                            k = i
                            while i <= j:
                                y_values.append(xy_list[k][1])
                                i += 1
            else:
                y_values.append(xy_list[i][1])
                i += 1

        y_values.append(xy_list[len(xy_list) - 1][1])
        self.y_values = y_values
        return y_values

    def get_x_values(self, xy_list):
        x_values = []
        for i in range(len(xy_list)):
            x_values.append(xy_list[i][0])
        self.x_values = x_values
        return x_values

    def divided_differences(self, x_values, y_values, xy_list):
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
                if (x_values[i + j] - x_values[i]) == 0:
                    pyramid_matrix[i][j] = self.get_derivation_value(xy_list, x_values[i], j) / math.factorial(j)
                else:
                    pyramid_matrix[i][j] = (pyramid_matrix[i + 1][j - 1] - pyramid_matrix[i][j - 1]) / (x_values[i + j] - x_values[i])
        self.pyramid_matrix = pyramid_matrix
        # print(pyramid_matrix)
        # for line in pyramid_matrix:
        #     print(line)
        return pyramid_matrix[0]  # erste Reihe wird zurückgegeben

    def get_derivation_value(self, xy_list, x_values, step):
        derivation_value = 0
        for i in range(len(xy_list) - 1):
            if xy_list[i][0] == x_values:
                derivation_value = xy_list[i + step][1]
                break
        return derivation_value
