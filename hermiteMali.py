import math
import numpy as np


class HermiteMali:
    def get_y_value_list(self, xy_list):
        y_value_list = []
        i = 0

        while i < len(xy_list) - 1:
            if xy_list[i][0] == xy_list[i + 1][0]:
                for j in range(len(xy_list) - 1, i, -1):
                    if xy_list[i][0] == xy_list[j][0]:
                        k = i
                        while i <= j:
                            y_value_list.append(xy_list[k][1])
                            i += 1
            else:
                y_value_list.append(xy_list[i][1])
                i += 1
        y_value_list.append(xy_list[len(xy_list) - 1][1])
        return y_value_list

    def get_x_value_list(self, xy_list):
        x_value_list = []
        for i in range(len(xy_list)):
            x_value_list.append(xy_list[i][0])
        return x_value_list

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
                    print("...")
                    #pyramid_matrix[i][j] = 
                else:
                    pyramid_matrix[i][j] = (pyramid_matrix[i + 1][j - 1] - pyramid_matrix[i][j - 1]) / (x_values[i + j] - x_values[i])
        return pyramid_matrix[0]  # erste Reihe wird zurückgegeben