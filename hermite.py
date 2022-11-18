import math

class Hermite:
    def __init__(self, stuetzstellen):
        """self.xWerte = xWerte
        self.yWerte = yWerte
        self.multiplikatoren = []"""

    # Funktion die den Ableitungsgrad der Stützstellen erkennt
    def ableitungsGradErkennen(self, x):
        ableitungsgrad = 1

        while True:  # mit for element in range(...) umwandeln https://www.youtube.com/watch?v=pQh5Idw2sKM&list=PL_pqkvxZ6ho3u8PJAsUU-rOAQ74D0TqZB&index=17
            if x == 1:
                break
            else:
                while self.xWerte[x] == self.xWerte[x - 1]:
                    ableitungsgrad += 1
                    x - 1
        return ableitungsgrad


    # Funktion für die Dividirten Differenzen
    def dividierteDifferenzen(self, xListe, yListe):
        multiplikatoren = []

        k = 0
        for element in xListe:
            if xListe[k + 1] - xListe[k] == 0:  # wenn durch 0 geteilt würde
                multiplikatoren.append(yListe[k + 1] / math.factorial(self.ableitungsGradErkennen(len(xListe[0:k + 1]))))
            else:
                multiplikatoren.append((yListe[k + 1] - yListe[k]) / (xListe[k + 1] - xListe[k]))

            k += 1

        """
        while k <= len(xWerte) - 1:
            if xWerte[k + 1] - xWerte[k] == 0:  # wenn durch 0 geteilt würde
                Multiplikatoren.append(yWerte[k + 1] / math.factorial(ableitungsGradErkennen(len(xWerte[0:k + 1]))))
            else:
                Multiplikatoren.append((yWerte[k + 1] - yWerte[k]) / (xWerte[k + 1] - xWerte[k]))

            k += 1
        """
        print(multiplikatoren)
        return multiplikatoren

    def polynomErstellen(self, stuetzstellen):
        polynom = None

        return polynom