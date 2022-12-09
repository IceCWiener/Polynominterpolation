from hermite import Hermite
from Newton import Newton

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


def generate_multiplied_out_polynom(multipliers):
    multiplied_out_polynom = ''
    for i in range(len(multipliers)-1):
        multiplied_out_polynom += f'{multipliers[len(multipliers)-1]}x + {multipliers[len(multipliers)-2]}'
    return multiplied_out_polynom


def generate_multipliers(pyramid_matrix, x_values):
    coefficients = []
    for i in range(len(pyramid_matrix[0])):
        coefficients.append(pyramid_matrix[0][i])

    coefficients[0] += coefficients[2]*(-1)*x_values[1]*(-1)*x_values[0] + coefficients[1]*(-1)*x_values[0]

    coefficients[1] += coefficients[2]*(-1)*x_values[1] + coefficients[2]*(-1)*x_values[0]

    return coefficients


if __name__ == '__main__':
    new_sampling_points_list = collect_sampling_points()
    print(new_sampling_points_list)
    polynom = create_polynom(new_sampling_points_list)
    try:
        new_polynom_with_brackets = generate_polynom_with_brackets(polynom.pyramid_matrix, polynom.x_values)
        print(polynom.pyramid_matrix)
        print(new_polynom_with_brackets)
        new_multiplied_out_polynom = generate_multiplied_out_polynom(polynom.pyramid_matrix, polynom.x_values)
    except AttributeError:
        print("Bitte mehr als eine Stützstelle eingeben")
