class Lagrange:

    import numpy as np       

    # Stützstellen mit negativem Vorzeichen erzeugen
    def create_wfunction(self, stützstellen):
        w_function = []

        for i in range(len(stützstellen)):
            w_function.append(-stützstellen[i])
        
        return w_function  

    # li Funktion erstellen
    def create_li_function(self, stützstellen, w_function):
        alle_li_function = []
        alle_li_x_werte = []
        li_x_wert = 1

        for i in range(len(stützstellen)):
            li_function = w_function.copy()
            li_function.pop(i)
            multiply_li_function = Newton().multiply_poly(li_function)
            alle_li_function.append(multiply_li_function)

            # xi werte in Funktion einsetzten 
            for j in range(len(li_function)):
                li_x_wert_teil = (stützstellen[i] + li_function[j]) 
                li_x_wert = li_x_wert * li_x_wert_teil
            alle_li_x_werte.append(li_x_wert)
            li_x_wert = 1
        print("\nli_x_Werte", alle_li_x_werte, "mit li_function", alle_li_function, "\n")
        
        alle_li_function = [1,-5,6,1,-4,3,1,-3,2]
        return alle_li_function, alle_li_x_werte

    # Li-function erstellen = li_function / li_x_wert
    def create_Li_function(self, n, alle_li_function, alle_li_x_werte):
        np = self.np
        Li_function = []
        Li_function_teil = 0

        for i in range(n):
            for j in range(n):
                Li_function_teil = alle_li_function[j+(i*n)] / alle_li_x_werte[i]
                Li_function.append(Li_function_teil)
        
        print("Li_function",Li_function)
        return Li_function

    # Polynom berechnen mit Stützwerten * Li Werte 
    def calculate_polynom(self, n, stützwerte, Li_function):
        polynom = []
        
        for i in range(n):
            for j in range(n):
                polynomteil = stützwerte[i] * Li_function[j+(i*n)] 
                polynom.append(polynomteil)
        print("Polynom: ",polynom)  
        return polynom  

    # Polynom sortieren/zusammenfassen 
    def normalform_poly(self, polynom):
        polynom_result = []
        
        for i in range(n):
            teil_poly = 0
            teil_poly = polynom[i]
            for j in range(1,n):
                teil_poly = teil_poly + polynom[i+(j*n)]
        
            polynom_result.append(teil_poly)
        print("fertiges Polynom:", polynom_result)
        return polynom_result

    # Ausgabe des Polynoms
    def ausgabe_poly(self, polynom_result):    
        ausgabe = []
        ausgabe_teil = 0

        for i in range(n):
           ausgabe_teil = polynom_result[i] , "* x^" , n-i-1
           ausgabe.append(ausgabe_teil)
           if i < n-1:
               ausgabe.append("+")
        print("Ausgabe: p(x) =", ausgabe)
        return ausgabe

n = 3
stützstellen = [1,2,3]
stützwerte = [5,0,-4]
print("Stützstellen: ", stützstellen)
print("Stützwerte: ", stützwerte)
w_function = Lagrange().create_wfunction(stützstellen)
li_function = Lagrange().create_li_function(stützstellen, w_function)
Li_function = Lagrange().create_Li_function(n,li_function[0],li_function[1])
polynom = Lagrange().calculate_polynom(n,stützwerte,Li_function)
norm_poly = Lagrange().normalform_poly(polynom)
ausgabe = Lagrange().ausgabe_poly(norm_poly)