# Lagrange 
import math # brauch man das?
import numpy as np       

stützstellen = []
#stützstellen = [1, 2, 3]
#stützwerte = [5, 0, -4]
stützwerte = []

w_function = []
li_x_wert_teil = 1
li_x_wert = 1
alle_li_x_werte = []
alle_li_function =[]
alle_Li_function = []


# Eingabe der Stützstellen
n = int(input('Wie viele Stützstellen soll es geben?')) 
x = np.zeros ((n))
y = np.zeros ((n))      # Zero soll alle Elemente auf 0 initialisieren

# Durchlauf beliebig vieler Werte + Ausgabe
for i in range (n):   
    print ('Eingabe der x-Werte')
    x = float(input('x [' + str (i) + ']= '))
    stützstellen.append(x)
    print ('Eingabe der y-Werte')
    y = float(input('y [' + str (i) + ']= '))
    stützwerte.append(y)

print("Stützstellen: ", stützstellen)
print("Stützwerte: ", stützwerte)

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

Li_array = np.zeros((n,2,n - 1)) #3, 2, 2 für n=3; (2,2,1) für n=2

# Einfügen der li_function Werte in den Array 
for t in range(n):
    Li_array = np.insert(Li_array, t*(2*(n - 1)), alle_li_function[t]) # t*2 für n=2; t*4 für n=3; t*6 für n=4
#dann ist der restliche Array mit Nullen gefüllt, diese werden aber bei resize ignoriert 

# Einfügen der li_x_werte in den Array 
for u in range(n):
    Li_array = np.insert(Li_array, (u*(2*(n - 1)))+(n-1), alle_li_x_werte[u]) # (u*2)+1 bei n=2; (u*4)+2 bei n=3; (u*6)+3 bei n=4
    Li_array = np.delete(Li_array, [(u*(2*(n - 1)))+n]) # (u*2)+2 bei n=2; (u*4)+3 bei n=3; (u*6)+4 bei n=4

# resize Array 
Li_array = np.resize(Li_array,(n,2,n-1)) #3,2,2 bei n=3
print("fertiger array: ", Li_array)



# Li_array aumultiplizieren nach dem Schema: (x + a)*(x + b) = x^2 + x*(a + b) + a*b

array_ausmult = np.zeros((1,n)) #0,0,0 bei n=3

for d in range(n): 
    for e in range(n -1):
        if n == 2:
            print("durch: ", Li_array[d,e+1,e])
            wert_ausmultipliziert = np.array([[1 / Li_array[d,e+1,e], Li_array[d,e,e] / Li_array[d,e+1,e]]])
            print("Wert ausmultipliziert: ",wert_ausmultipliziert)
            array_ausmult = np.concatenate((array_ausmult, wert_ausmultipliziert))
        elif n == 3:
            wert_ausmultipliziert = np.array([[1 / Li_array[d,e+1,e], (Li_array[d,e,e] + Li_array[d,e,e+1]) / Li_array[d,e+1,e], (Li_array[d,e,e] * Li_array[d,e,e+1]) / Li_array[d,e+1,e]]])
            print("Wert ausmultipliziert: ",wert_ausmultipliziert)
            array_ausmult = np.concatenate((array_ausmult, wert_ausmultipliziert))
        break

print(array_ausmult)

# Polynom berechnen mit Stützwerten * Li Werte 
polynom = []
for f in range(1, len(array_ausmult)):
    for g in range(n):
        polynomteil = stützwerte[f-1] * array_ausmult[f,g]
        polynom.append(polynomteil)
print("Polynom: ",polynom)    

# Polynom sortieren 
polynom_ausgabe = []
for h in range(n):
    polynom_ausgabe_teil = polynom[h] + polynom[h+n] + polynom[h+n*2] # ist nur für n=3 gültig 
    polynom_ausgabe.append(polynom_ausgabe_teil)
print("fertiges Polynom:", polynom_ausgabe)

# Ausgabe des Polynoms
ausgabe = []
ausgabe_teil = str([])
for i in range(len(polynom_ausgabe)):
    ausgabe_teil = polynom_ausgabe[i] , "x^" , len(polynom_ausgabe)-i-1
    ausgabe.append(ausgabe_teil)
    if i < len(polynom_ausgabe)-1:
        ausgabe.append("+")
print("Ausgabe: p(x) =", ausgabe)