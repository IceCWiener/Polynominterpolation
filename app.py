from hermite import Hermite
from newton import Newton
from Lagrange_komplett import Lagrange
from utility import Utility


def collect_xy_values():
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

    # xy_values = [(1, 1), (1, 4), (2, 3), (2, 1), (2, 2)] #Hermite
    # xy_values = [(1, 1), (3, 4), (2, 3), (5, 1), (8, 2)]  # Else
    # Newton Test -> (11 x^3)/72 - (145 x^2)/72 + (85 x)/12 - 3
    xy_values = [(0, -3), (6, 0), (8, 3), (9, 9)]

    return xy_values


def create_polynom(xy_values):
    x_values = util.get_x_values(xy_values)
    y_values = util.get_y_values(xy_values)

    for x_n in range(len(xy_values) - 1):
        xy1 = xy_values[x_n]
        xy2 = xy_values[x_n + 1]

        if xy2[0] == xy1[0]:
            hermite_var = True
            print("wir machen Hermit")
            hermite_polynom = Hermite()
            herm_coef = hermite_polynom.get_coefficients(xy_values)
            standard_form_polynom_coef = util.generate_polynom_coefficients(
                hermite_polynom.coefficients, x_values)
            pretty_polynom = util.transform_coefficients_to_pretty_polynom(
                standard_form_polynom_coef)
            print(pretty_polynom)
            return hermite_polynom

        if x_n == len(xy_values) - 2:
            print("wir machen Newton und Lagrange")
            nt = Newton()

            # Lagrange
            lagrange_polynom = Lagrange()
            w_function = lagrange_polynom.create_wfunction(x_values)
            li_function = lagrange_polynom.create_li_function(
                x_values, w_function)
            Li_function = lagrange_polynom.create_Li_function(
                len(xy1), li_function[0], li_function[1])
            polynom = lagrange_polynom.calculate_polynom(
                len(xy1), y_values, Li_function)
            norm_poly = lagrange_polynom.normalform_poly(len(xy1), polynom)
            ausgabe = lagrange_polynom.ausgabe_poly(len(xy1), norm_poly)

            # Newton
            newt_coeffs = nt.newton_div_diff(x_values, y_values)
            newt_coeffs = util.round_list(newt_coeffs, 3)
            poly_coeffs = util.generate_polynom_coefficients(
                newt_coeffs, x_values)
            poly_coeffs = util.round_list(poly_coeffs, 3)
            pretty_newt = util.create_string_polynomial(
                poly_coeffs)
            print("\n\nNewton's Polynome: " + pretty_newt)

            return nt, lagrange_polynom


if __name__ == '__main__':
    util = Utility()

    xy_values = collect_xy_values()
    print(f'Stützstellen: {xy_values}')
    polynom = create_polynom(xy_values)
