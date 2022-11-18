from hermite import Hermite

polynom = None
sampling_points = []
hermiteVar = False

i = 0
while True:
    if i != 0:
        abbruch = input("möchten Sie eine " + str(i+1) + "te Stützstelle eingeben bitte Enter drücken, andernfalls geben sie n ein: ")
        if abbruch == "n":
            break
    stuetzstelle = (int(input("Bitte X-wert der " + str(i+1) + "ten Stützstelle eingeben: ")), int(input("Bitte Y-wert der " + str(i+1) + "ten Stützstelle eingeben: ")))
    stuetzstellenListe.append(stuetzstelle)
    i += 1

for Xn in range(len(stuetzstellenListe)-1):
    print(Xn)
    xy1 = stuetzstellenListe[Xn]
    xy2 = stuetzstellenListe[Xn+1]
    if xy2[0] == xy1[0]:
        hermiteVar = True
        print("wir machen Hermit")
        #polynom = Hermite()
        #polynom.polynomErstellen(stuetzstellenListe)
        break
    elif hermiteVar == False and Xn == len(stuetzstellenListe)-2:
        print("wir machen Newton und Lagrange")

print(stuetzstellenListe)