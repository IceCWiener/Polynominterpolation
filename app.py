from hermite import Hermite
from Newton import Newton 
from Lagrange_komplett import Lagrange
from utility import Utility



def collect_sampling_points():
    xy_values = []
    hermite_var = False
    i = 0
    # while True:
    #     if i != 0:
    #         check_if_wants_to_continue = input("möchten Sie eine " + str(i + 1) + "te Stützstelle eingeben bitte Enter drücken, andernfalls geben sie n ein: ")
    #         if check_if_wants_to_continue == "n":
    #             break
    #     sampling_point = (int(input("Bitte X-wert der " + str(i + 1) + "ten Stützstelle eingeben: ")), int(input("Bitte Y-wert der " + str(i + 1) + "ten Stützstelle eingeben: ")))
    #     sampling_points_list.append(sampling_point)
    #     i += 1
    xy_values = [(1, 1), (1, 4), (2, 3), (2, 1), (2, 2)]
    return xy_values


def create_polynom(xy_values):
    for x_n in range(len(xy_values) - 1):
        xy1 = xy_values[x_n]
        xy2 = xy_values[x_n + 1]
        x_values = ut.get_x_values(xy_values)
        y_values = ut.get_y_values(xy_values)

        if xy2[0] == xy1[0]:
            hermite_var = True
            print("wir machen Hermit")
            hermite_polynom = Hermite()
            hermite_polynom.get_coefficients(xy_values)
            standard_form_polynom_coef = ut.generate_polynom_coefficients(hermite_polynom.coefficients, hermite_polynom.x_values)
            pretty_polynom = ut.transform_coefficients_to_pretty_polynom(standard_form_polynom_coef)
            print(pretty_polynom)
            return hermite_polynom

        if x_n == len(xy_values) - 2:
            print("wir machen Newton und Lagrange")
            newton_polynom = Newton()
            lagrange_polynom = Lagrange()
            return newton_polynom, lagrange_polynom

if __name__ == '__main__':
    ut = Utility()

    new_sampling_points_list = collect_sampling_points()
    print(f'Stützstellen: {new_sampling_points_list}')
    polynom = create_polynom(new_sampling_points_list)