# Author KR

"""
https://pythonnumericalmethods.berkeley.edu/notebooks/chapter17.05-Newtons-Polynomial-Interpolation.html
Stützstellen: x0,...,xn (müssen alle unterschiedlich sein)
Stützwerte: y0,...yn
Punkte: P

Newton'sches Interpolationsverfahren
p(x)=a0+a1(x−x0)+a2(x−x0)(x−x1)+...+an(x−x0)(x−x1)(x−x2)⋅...⋅(x−xn−1)
=> p(x)=∑[i=0 n]  ai*ni(x)
mit ni(x)=∏[i−1 j=0]  (x−xj)

y0=a0
y1=a0+a1(x1−x0) -> a1 = y1 - a0/(x1 - x0)
y2=a0+a1(x2−x0)+a2(x2−x0)(x2−x1) -> a2 = 
...
yn=a0+a1(xn−x0)+a2(xn−x0)(xn−x1)+ ... +an(xn−x0)(xn−x1)(xn−x2)⋅ ... ⋅(xn−xn−1)

Beispiel:
P0(1;2), P1(2;3), P2(3;1), P3(4;3)
p(x)=a0+a1(x−1)+a2(x−1)(x−2)+a3(x−1)(x−2)(x−3)
->
2=a0⇒a0=2
3=2+a1(2−1)⇒a1=1
1=2+1(3−1)+a2(3−1)(3−2)⇒a2=−3/2=−1,5
3=2+1(4−1)−1,5(4−1)(4−2)+a3(4−1)(4−2)(4−3)⇒a3=7/6
"""

import numpy as np

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



    # Pyramide anschaulicher machen wie in der Mitschrift der Vorlesung
    # Namen ändern & refactorn

x = np.array([1, 7, 3, 5])
y = np.array([1, 9, 2, 8])
nt = Newton()
div_diff = nt.divided_differences(x, y)
#print(div_diff)
print(nt.create_polynome(div_diff))
