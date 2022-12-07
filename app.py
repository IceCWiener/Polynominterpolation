from hermite import Hermite
from Newton import Newton

def collect_sampling_points():
    sampling_points_list = []
    hermite_var = False
    i = 0
    while True:
        if i != 0:
            check_if_wants_to_continue = input("möchten Sie eine " + str(i + 1) + "te Stützstelle eingeben bitte Enter drücken, andernfalls geben sie n ein: ")
            if check_if_wants_to_continue == "n":
                break
        sampling_point = (int(input("Bitte X-wert der " + str(i + 1) + "ten Stützstelle eingeben: ")), int(input("Bitte Y-wert der " + str(i + 1) + "ten Stützstelle eingeben: ")))
        sampling_points_list.append(sampling_point)
        i += 1
    return sampling_points_list


def create_polynom(sampling_points_list):
    for x_n in range(len(sampling_points_list) - 1):
        xy1 = sampling_points_list[x_n]
        xy2 = sampling_points_list[x_n + 1]
        if xy2[0] == xy1[0]:
            hermite_var = True
            print("wir machen Hermit")
            hermite_polynom = Hermite()
            hermite_polynom.get_coefficients(sampling_points_list)
            return hermite_polynom

        if x_n == len(sampling_points_list) - 2:
            print("wir machen Newton und Lagrange")
            newton_polynom = Newton()
            return newton_polynom


if __name__ == '__main__':
    new_sampling_points_list = collect_sampling_points()
    print(new_sampling_points_list)
    polynom = create_polynom(new_sampling_points_list)
    try:
        print(polynom.coefficients)
    except AttributeError:
        print("Bitte mehr als eine Stützstelle eingeben")
