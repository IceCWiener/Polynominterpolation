class Utility:
    def __init__(self):
        pass

    def generate_polynom_coefficients(self, coefficients, x_values):
        final_pol = []
        n = len(coefficients)

        for i in range(n):
            p = [1.]
            for j in range(i):
                p_temp = [-x_values[j], 1.] # (x - x_j)
                p = self.multiply_polynoms(p, p_temp)
            p = self.multiply_each_element_of_polynom(p, coefficients[i])
            final_pol = self.add_polynoms(final_pol, p)

        return final_pol

    def multiply_polynoms(self, pol1, pol2):
        multiplied_pol = [0]*(len(pol1) + len(pol2)-1)
        for o1, i1 in enumerate(pol1):
            for o2, i2 in enumerate(pol2):
                multiplied_pol[o1+o2] += i1*i2
        return multiplied_pol

    def multiply_each_element_of_polynom(self, polynom, factor):
        for i in range(len(polynom)):
            polynom[i] = polynom[i]*factor
        return polynom

    def add_polynoms(self, pol1, pol2):
        if len(pol1) == 0:
            return pol2

        if len(pol2) == 0:
            return pol2

        max_length = max(len(pol1), len(pol2))
        result = [0] * max_length

        if (len(pol1)>=len(pol2)):
            longer_pol = pol1
            short_pol = pol2
        else:
            longer_pol = pol2
            short_pol = pol1

        for i in range(len(longer_pol)):
            result[i] = longer_pol[i]

        for j in range(len(short_pol)):
            result[j] += short_pol[j]

        return result

    def get_x_values(self, xy_list):
        x_values = []
        for i in range(len(xy_list)):
            x_values.append(xy_list[i][0])
        self.x_values = x_values
        return x_values

    def get_y_values(self, xy_list):
        y_values = []
        i = 0

        while i < len(xy_list) - 1:
            if xy_list[i][0] == xy_list[i + 1][0]:
                for j in range(len(xy_list) - 1, i, -1):
                        if i >= len(xy_list):
                            return y_values
                        if xy_list[i][0] == xy_list[j][0]:
                            k = i
                            while i <= j:
                                y_values.append(xy_list[k][1])
                                i += 1
            else:
                y_values.append(xy_list[i][1])
                i += 1

        y_values.append(xy_list[len(xy_list) - 1][1])
        self.y_values = y_values
        return y_values

    def generate_polynom_with_brackets(self, pyramid_matrix, x_values):
        coefficients = pyramid_matrix[0]
        bracket_polynom = f'{coefficients[0]}'
        linear_factor = ""
        for i in range(len(pyramid_matrix[0])-1):
            linear_factor += f'(x-{x_values[i]})'
            summand = f'{coefficients[i+1]}{linear_factor}'
            bracket_polynom = bracket_polynom + " + " + summand
        return bracket_polynom

    def map_ndarray_to_array(self, ndarray):
        result_pol = []
        for i in range(len(ndarray[0].coef)):
            result_pol.append(ndarray[0].coef[int(i)])
        return result_pol

    def transform_coefficients_to_pretty_polynom(self, coefficients):
        standard_form_polynom = "p(x) = "
        for i in range(len(coefficients)-1, -1, -1):
            standard_form_polynom += f'{coefficients[i]} x^{i} + '
        return standard_form_polynom