class Newton:
    # Erstellen von Newtons "Pyramide" um Koeffizienten/Multiplikatoren des Polynoms zu berechnen
    def divided_differences(self, x_values, y_values):
        n = len(y_values) # n-1 = Grad des Polynoms

        # Erstelle eine mit Nullern gefüllte Matrix
        pyramid_matrix = []

        for i in range(n):
            pyramid_matrix.append([])
            
            for j in range(n):
                pyramid_matrix[i].append(0.)
        
        # erste Spalte der Pyramide wird mit y-Werten gefüllt
        for i in range(n):
            pyramid_matrix[i][0] = float(y_values[i])

        print(pyramid_matrix)
        
        for j in range(1,n):
            for i in range(n-j):
                # Spalten werden nacheinander von berechneten Koeffizienten gefüllt
                pyramid_matrix[i][j] = (pyramid_matrix[i+1][j-1] - pyramid_matrix[i][j-1]) / (x_values[i+j] - x_values[i])
        #print(pyramid_matrix)
        
        return pyramid_matrix[0] # erste Reihe wird zurückgegeben

    # TODO: Funktionalität für Int-Polynom erstellen (zum Ausrechnen)
    def create_string_polynomial(self, coefficients):
        str_poly = ""
        degree = len(coefficients) - 1
        coefficients =  self.flip_array(coefficients)

        for i in coefficients:
            if degree > 1:
                str_poly = str_poly + "(" + str(i) + ")*x**" + str(degree) + " + "
            elif degree == 1:
                str_poly = str_poly + "(" + str(i) + ")*x "
            else:
                str_poly = str_poly + " + (" + str(i) + ")"
            
            degree = degree - 1
        return str_poly

    def flip_array(self, arr):
        result = []
        
        for i in range(len(arr) - 1, -1, -1):
            result.append(arr[i])
        
        return result

x_vals = [-1, 0, 1, 2]
y_vals = [1, 1, 2, 0]
nt = Newton()
div_diff = nt.divided_differences(x_vals, y_vals)
#print(div_diff)
string_poly = nt.create_string_polynomial(div_diff)
#print(string_poly)
