import numpy as np

# funktioniert bis jetzt nur für 3 Stützstellen/Stützwerte 

stützstellen = [1, 2, 3]
stützwerte = [5, 0, -4]

w_function = []
li_x_wert_teil = 1
li_x_wert = 1
alle_li_x_werte = []
alle_li_function =[]
alle_Li_function = []

# Stützstellen mit negativem Vorzeichen erzeugen
for a in range(len(stützstellen)):
    w_function.append(-stützstellen[a])
print(w_function)  

# li Funktion erstellen
for b in range(len(stützstellen)):
    li_function = w_function.copy()
    li_function.pop(b)
    print("l",b,"function =",li_function)
    alle_li_function.append(li_function)

    # xi werte in Funktion einsetzten 
    for s in range(len(li_function)):
        li_x_wert_teil = (stützstellen[b] + li_function[s]) 
        #print("li_x_wert_teil: ",li_x_wert_teil)
        li_x_wert = li_x_wert * li_x_wert_teil
    #print("li_x_wert: ",li_x_wert)  
    alle_li_x_werte.append(li_x_wert)
    li_x_wert = 1

print("\nli_x_Werte", alle_li_x_werte, "mit li_function", alle_li_function, "\n")

# Li Funktion erstellen 
for c in range(len(alle_li_function)):
    Li_function = []
    Li_function.append(alle_li_function[c])
    Li_function.append(alle_li_x_werte[c])
    print(Li_function)
    alle_Li_function.append(Li_function)

print("alle Li Funktionen: ", alle_Li_function)

# Li Funktion aumultiplizieren nach dem Schema: (x + a)*(x + b) = x^2 + x*(a + b) + a*b

# alle_Li_function in einen numpy array bringen 
# diesen dann gleich skalierene [[[2,3],[2,0], ...]] 
# dann das Element aufrufen mit name[0,3] -> erste Spalte viertes Element 

beispiel_array = np.array([[[-2,-3], [2,0]], 
                          [[-1,-3], [-1,0]], 
                          [[-1,-2], [2,0]]])

array_ausmult = np.array([[0, 0, 0]])
#ausmultipliziert = [[1, beispiel_array[0,0,0] + beispiel_array[0,0,1], beispiel_array[0,0,0] * beispiel_array[0,0,1]]]
for d in range(3):
    for e in range(2):
        wert_ausmultipliziert = [[1 / beispiel_array[d,e+1,e], (beispiel_array[d,e,e] + beispiel_array[d,e,e+1]) / beispiel_array[d,e+1,e], (beispiel_array[d,e,e] * beispiel_array[d,e,e+1]) / beispiel_array[d,e+1,e]]]
        #print(wert_ausmultipliziert)
        array_ausmult = np.concatenate((array_ausmult, wert_ausmultipliziert))
        #array_ausmult.append(wert_ausmultipliziert)
        break

print(array_ausmult)

# Polynom berechnen mit Stützwerten * Li Werte 
polynom = []
for f in range(1, len(array_ausmult)):
    for g in range(3):
        polynomteil = stützwerte[f-1] * array_ausmult[f,g]
        polynom.append(polynomteil)
print(polynom)    

# Polynom sortieren und ausgeben
polynom_ausgabe = []
for h in range(3):
    polynom_ausgabe_teil = polynom[h] + polynom[h+3] + polynom[h+6]
    polynom_ausgabe.append(polynom_ausgabe_teil)
print("Ausgabe: p(x) =", polynom_ausgabe[0], "x^2 +", polynom_ausgabe[1], "x +", polynom_ausgabe[2])