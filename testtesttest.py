n = 2 # Anzahl der Stützstellen 
function = [1,-1,1,-2] # (1x-1)*(1x-2)
zwischen = [0,0,0,0]
ergebnis = [0,0,0]

for i in range(len(function)-n):
    zwischen[i] = function[i] * function[n]
    print(zwischen)
    for j in range(len(function) - n):
        zwischen[i+j+1] = function[j] * function[n+1]
        print(zwischen)