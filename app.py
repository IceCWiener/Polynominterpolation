from hermite import Hermite
from Newton import Newton
import numpy as np

def collect_sampling_points():
    sampling_points_list = []
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
    sampling_points_list = [(1, 1), (1, 4), (2, 3), (2, 1), (2, 2)]
    return sampling_points_list


def create_polynom(sampling_points_list):
    for x_n in range(len(sampling_points_list) - 1):
        xy1 = sampling_points_list[x_n]
        xy2 = sampling_points_list[x_n + 1]
        if xy2[0] == xy1[0]:
            hermite_var = True
            print("wir machen Hermit")
            hermite_polynom = Hermite()
            hermite_polynom.get_x_values(sampling_points_list)
            hermite_polynom.get_coefficients(sampling_points_list)
            new_polynom_with_brackets = generate_polynom_with_brackets(hermite_polynom.pyramid_matrix, hermite_polynom.x_values)
            print(f'p(x) = {new_polynom_with_brackets}')
            return hermite_polynom

        if x_n == len(sampling_points_list) - 2:
            print("wir machen Newton und Lagrange")
            newton_polynom = Newton()
            return newton_polynom


def generate_polynom_with_brackets(pyramid_matrix, x_values):
    coefficients = pyramid_matrix[0]
    bracket_polynom = f'{coefficients[0]}'
    linear_factor = ""
    for i in range(len(pyramid_matrix[0])-1):
        linear_factor += f'(x-{x_values[i]})'
        summand = f'{coefficients[i+1]}{linear_factor}'
        bracket_polynom = bracket_polynom + " + " + summand
    return bracket_polynom


def generate_polynom_coefficients(coefficients, x_values):
    final_pol = []
    n = len(coefficients)

    for i in range(n):
        p = [1.]
        for j in range(i):
            p_temp = [-x_values[j], 1.] # (x - x_j)
            p = multiply_polynoms(p, p_temp)
        p = [j * coefficients[i] for j in p]
        final_pol += np.polyadd(final_pol, p)
        print(777, final_pol)

    result_pol = []
    for i in range(len(final_pol)):
        result_pol.append(final_pol[i])
    return result_pol


def multiply_polynoms(pol1, pol2):
    multiplied_pol = [0]*(len(pol1) + len(pol2)-1)
    for o1, i1 in enumerate(pol1):
        for o2, i2 in enumerate(pol2):
            multiplied_pol[o1+o2] += i1*i2
    return multiplied_pol


if __name__ == '__main__':
    new_sampling_points_list = collect_sampling_points()
    print(f'Stützstellen: {new_sampling_points_list}')
    polynom = create_polynom(new_sampling_points_list)


