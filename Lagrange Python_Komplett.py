# Lagrange 
# Eingabe der Stützstellen
import math
import numpy as np       

n = int(input('Anzahl der Stützstellen x, y eingeben:'))
x = np.zeros ((n))
y = np.zeros ((n))      # Zero soll alle Elemente auf 0 initialisieren


for i in range (n):   # Durchlauf beliebig vieler Werte + ausgabe
print ('Eingabe der x-Werte')
x[i] = float(input('x ['str (i) + ']= '))
print ('Eingabe der y-Werte')               #eingabe der Stützwerte: P
y[i] = float(input('y [' + str (i) + ']= '))





