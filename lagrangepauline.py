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
        li_x_wert = li_x_wert * li_x_wert_teil
    alle_li_x_werte.append(li_x_wert)
    li_x_wert = 1

print("\nli_x_Werte", alle_li_x_werte, "mit li_function", alle_li_function, "\n")



#Erstellen des Arrays, der alle Werte der li funktionen und lix werte beinhaltet

Li_array = np.zeros((len(alle_li_x_werte),2,len(alle_li_x_werte) - 1)) #3, 2, 2

# Einfügen der li_function Werte in den Array 
for t in range(len(alle_li_x_werte)):
    Li_array = np.insert(Li_array, t*4, alle_li_function[t])
#dann ist der restliche Array mit Nullen gefüllt, diese werden aber bei resize ignoriert 

# Einfügen der li_x_werte in den Array 
for u in range(len(alle_li_x_werte)):
    Li_array = np.insert(Li_array, (u*4)+2, alle_li_x_werte[u])
    Li_array = np.delete(Li_array, [(u*4)+3], None) 

# resize Array 
Li_array = np.resize(Li_array,(len(alle_li_x_werte),2,len(alle_li_x_werte)-1)) #3,2,2
print("fertiger array: ", Li_array)



# Li_array aumultiplizieren nach dem Schema: (x + a)*(x + b) = x^2 + x*(a + b) + a*b

array_ausmult = np.zeros((1,len(alle_li_x_werte))) #0,0,0
print(array_ausmult)
for d in range(len(alle_li_x_werte)): # shape, size 
    for e in range(len(alle_li_x_werte) -1):
        wert_ausmultipliziert = np.array([[1 / Li_array[d,e+1,e], (Li_array[d,e,e] + Li_array[d,e,e+1]) / Li_array[d,e+1,e], (Li_array[d,e,e] * Li_array[d,e,e+1]) / Li_array[d,e+1,e]]])
        print("Wert ausmultipliziert: ",wert_ausmultipliziert)
        array_ausmult = np.concatenate((array_ausmult, wert_ausmultipliziert)) # geht auch nur mit + ? 
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