multiplikatoren = [1, 3, 9]
xWerte = [4, 3, 7]
yWerte = [1, 6, 2]
polynom = "f(x) = "

i = 0
while i < len(multiplikatoren):
    if i == 0:
        polynom += str(yWerte[0])
    else:
        if multiplikatoren[i] < 0:
            polynom += "-"
        else:
            polynom += "+"

        polynom += + str(multiplikatoren[i]) + "(x-" + str(xWerte[i - 1]) + ")"
    i += 1
print(polynom)