import numpy as np
import math

class Newton:
    # Erstellen von Newtons "Pyramide" um Koeffizienten des Polynoms zu berechnen
    def divided_differences(self, x, y):
        n = len(y) # n-1 = Grad des Polynoms
        pyramid_matrix = np.zeros([n, n]) # n mal n Array gefüllt mit nullen
        pyramid_matrix[::,0] = y # erste Spalte wird mit y-Werten gefüllt
        for j in range(1,n):
            for i in range(n-j):
                # Spalten werden nacheinander von berechneten Koeffizienten gefüllt
                pyramid_matrix[i][j] = (pyramid_matrix[i+1][j-1] - pyramid_matrix[i][j-1]) / (x[i+j] - x[i])
        #print(pyramid_matrix)
        
        return pyramid_matrix[0] # erste Reihe wird zurückgegeben

    # TODO: Falsche Methodik durch korrekte Rechnung ersetzen
    def create_polynome(self, coefficients):
        poly = ""
        degree = len(coefficients) - 1
        coefficients =  self.flip_array(coefficients)

        for i in coefficients:
            if degree > 1:
                poly = poly + "(" + str(i) + ")x" + str(degree) + " + "
            elif degree == 1:
                poly = poly + "(" + str(i) + ")x "
            else:
                poly = poly + " + (" + str(i) + ")"
            
            degree = degree - 1
        return poly

    def flip_array(self, arr):
        result = []
        
        for i in range(len(arr) - 1, -1, -1):
            result.append(arr[i])
        
        return result

    # Methode zum testen der Stellen schreiben
    def poly_test(self, x, y, coef):
        print((-0.208*math.pow(7, 3))+(0.208*pow(7, 2))+(1.333*7)+1)

#x = np.array([1, 7, 3, 5])
#y = np.array([1, 9, 2, 8])
x = np.array([-1, 0, 1, 2])
y = np.array([1, 1, 2, 0])
nt = Newton()
div_diff = nt.divided_differences(x, y)
#print(div_diff)
print(nt.create_polynome(div_diff))

