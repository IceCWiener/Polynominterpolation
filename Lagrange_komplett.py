import numpy as np    
from utility import Utility

class Lagrange:
    def __init__(self) -> None:
        self.ut = Utility()

    # li Funktion erstellen
    def create_li_function(self, stützstellen):
        alle_li_function = []
        alle_li_x_werte = []
        li_x_wert = 1

        for i in range(len(stützstellen)):
            li_function = stützstellen.copy()
            li_function.pop(i) # (x-1)(x-2)
            multiply_li_function = self.ut.generate_polynom_coefficients(self.ut.create_zeros_end_one_list(len(stützstellen)),li_function)
            for k in multiply_li_function:
                alle_li_function.append(k)

            # xi werte in Funktion einsetzten 
            for j in range(len(li_function)):
                li_x_wert_teil = (stützstellen[i] - li_function[j]) 
                li_x_wert = li_x_wert * li_x_wert_teil
            alle_li_x_werte.append(li_x_wert)
            li_x_wert = 1
        
        return alle_li_function, alle_li_x_werte

    # Li-function erstellen = li_function / li_x_wert
    def create_Li_function(self, n: int, alle_li_function: list[float], alle_li_x_werte: list):
        Li_function = []
        Li_function_teil = 0

        for i in range(n):
            for j in range(n):
                Li_function_teil = alle_li_function[j+(i*n)] / alle_li_x_werte[i]
                Li_function.append(Li_function_teil)
        
        return Li_function

    # Polynom berechnen mit Stützwerten * Li Werte 
    def calculate_polynom(self, n, stützwerte, Li_function):
        polynom = []
        
        for i in range(n):
            for j in range(n):
                polynomteil = stützwerte[i] * Li_function[j+(i*n)] 
                polynom.append(polynomteil)
 
        return polynom  

    # Polynom sortieren/zusammenfassen 
    def normalform_poly(self,n, polynom):
        polynom_result = []

        for i in range(n):
            teil_poly = 0
            teil_poly = polynom[i]
            for j in range(1,n):
                teil_poly = teil_poly + polynom[i+(j*n)]
        
            polynom_result.append(teil_poly)
        
        return polynom_result