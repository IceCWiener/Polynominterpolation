import os

polynom = None
sampling_points = []
hermite_var = False


def menu():
    i = 0
    while True:
        if i != 0:
            cancel = input("möchten Sie eine " + str(
                i + 1) + "te Stützstelle eingeben bitte Enter drücken, andernfalls geben sie n ein: ")
            if cancel == "n":
                break
        sampling_point = (int(input("Bitte X-wert der " + str(i + 1) + "ten Stützstelle eingeben: ")),
                        int(input("Bitte Y-wert der " + str(i + 1) + "ten Stützstelle eingeben: ")))
        sampling_points_list.append(sampling_point)
        i += 1

    for Xn in range(len(sampling_points_list) - 1):
        print(Xn)
        xy1 = sampling_points_list[Xn]
        xy2 = sampling_points_list[Xn + 1]
        if xy2[0] == xy1[0]:
            hermite_var = True
            print("wir machen Hermit")
            # polynom = Hermite()
            # polynom.create_polynom(sampling_points_list)
            break
        elif hermite_var == False and Xn == len(sampling_points_list) - 2:
            print("wir machen Newton und Lagrange")

    print(stuetzstellenListe)

if __name__ == '__main__':
    menu()



