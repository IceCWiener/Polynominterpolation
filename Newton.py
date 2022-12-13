from utility import Utility


class Newton:

    def __init__(self):
        #self.coefficients = self.newton_test()
        self.ut = Utility()

    # Erstellen von Newtons "Pyramide" um Koeffizienten/Multiplikatoren des Polynoms zu berechnen
    def newton_div_diff(self, x_values, y_values):
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

        # print(pyramid_matrix)

        for j in range(1, n):
            for i in range(n-j):
                # Spalten werden nacheinander von berechneten Koeffizienten gefüllt
                pyramid_matrix[i][j] = (
                    pyramid_matrix[i+1][j-1] - pyramid_matrix[i][j-1]) / (x_values[i+j] - x_values[i])
        # print(pyramid_matrix)

        return pyramid_matrix[0]  # erste Reihe wird zurückgegeben
