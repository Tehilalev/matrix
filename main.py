def get_co_factor(m, i, j):
    return [row[: j] + row[j+1:] for row in (m[: i] + m[i+1:])]


def determinant_of_matrix(matrix):
    """
    The function calculates the determinant of the matrix
    :param matrix: the matrix
    :return: the determinant
    """
    if len(matrix) == 2:
        value = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return value
    _sum = 0
    for col in range(len(matrix)):
        sign = (-1) ** col
        sub_det = determinant_of_matrix(get_co_factor(matrix, 0, col))
        _sum += (sign * matrix[0][col] * sub_det)
    return _sum


def make_matrix(row, column):
    """
    The function make unit matrix
    :param row: number of rows
    :param column: number of columns
    :return: unit matrix
    """
    matrix = []
    for j in range(1, row + 1):
        _list = []
        for y in range(1, column + 1):
            if j == y:
                _list.append(1)
            else:
                _list.append(0)
        matrix.append(_list)
    return matrix


def mul_two_matrix(m1, m2):
    """
    The function mul two matrix
    :param m1: matrix 1
    :param m2: matrix 2
    :return: the solution matrix
    """
    v = []
    new = []
    index = 0
    for row in m1:
        vector = []
        for j in range(0, len(row)):
            temp = []
            for r in m2:
                temp.append(r[j])
                v = []
            for i in range(0, len(row)):
                v.append((row[i]) * (temp[i]))
            vector.append(sum(v))
        new.append(vector)
        index += 1
    return new


def mul_matrix_vector(matrix, vector):
    """
    The function mul matrix with vector
    :param matrix: the matrix
    :param vector: the vector
    :return: the new matrix
    """
    new_matrix = []
    index = 0
    for row in matrix:
        v = []
        for i in range(0, len(row)):
            v.append((row[i]) * (vector[i]))
        new_matrix.append(sum(v))
        index += 1
    return new_matrix


def print_matrix(matrix):
    """
    The function gets a matrix and print it like a table
    :param matrix: matrix
    :return: there is no return value
    """
    for i in range(len(matrix)):
        print("(", end=" ")
        print_row(matrix[i])  # call the function that prints a row in matrix
        print(")")
    print()
    print()


def print_row(row):
    """
    The function gets a row in matrix and prints it
    :param row: row in matrix
    :return: there is no return value
    """
    for k in range(len(row)):
        print(f'{row[k]:.2f}', end="  ")  # prints the number with two digits after the point


def print_format(el_matrix, matrix, solution_matrix):
    """
    The function gets three matrix and prints it in table like exercise
    :param el_matrix: the elementary matrix
    :param matrix: the matrix
    :param solution_matrix: the solution matrix
    :return: there is no return value
    """
    for i in range(len(matrix)):
        print("(", end=" ")
        print_row(el_matrix[i])  # call the function that prints a row in matrix
        print(")", end=" ")
        print("(", end=" ")
        print_row(matrix[i])  # call the function that prints a row in matrix
        if (i + 1) == (len(matrix) // 2) or (i - 1) == (len(matrix) // 2):
            print(")", end="     ")
        else:
            print(")", end="   ")

        if i == (len(matrix) // 2):
            print("=", end=" ")
        print("(", end=" ")
        print_row(solution_matrix[i])  # call the function that prints a row in matrix
        print(")")
    print()
    print()


def print_solution(x_vector):
    """
    The function prints the solution of the system of linear equations like a vector
    :param x_vector: the vector
    :return: there is no return value
    """
    print("The solution is:")
    for i in range(len(x_vector)):
        print("(", f'{x_vector[i]:.2f}', ")")


def find(matrix, vector_b):
    """
    The function gets a matrix and b vector and calculates and prints the solution
    :param matrix: the matrix
    :param vector_b: the vector
    :return: there is no return value
    """
    e_temp1 = make_matrix(len(matrix), len(matrix))  # Variable to save the multiplication of elementary matrices
    for i in range(len(matrix)):
        _max = abs(matrix[i][i])
        for j in range(i, len(matrix)):  # this loop for replacing rows
            if matrix[j][i] > _max:
                elementary = make_matrix(len(matrix), len(matrix))  # make unit matrix
                row_temp = elementary[i]
                elementary[i] = elementary[j]
                elementary[j] = row_temp
                e_temp1 = mul_two_matrix(elementary, e_temp1)
                save_matrix = matrix
                matrix = mul_two_matrix(elementary, matrix)
                print_format(elementary, save_matrix, matrix)  # Prints the steps of the solution
                _max = abs(matrix[i][i])
        elementary = make_matrix(len(matrix), len(matrix))
        elementary[i][i] = 1 / matrix[i][i]  # to convert the pivot to "1"
        save_matrix = matrix
        matrix = mul_two_matrix(elementary, matrix)
        print_format(elementary, save_matrix, matrix)  # Prints the steps of the solution
        e_temp1 = mul_two_matrix(elementary, e_temp1)
        elementary = make_matrix(len(matrix), len(matrix))

        for k in range(len(matrix)):  # this loop to reset the organs above and below the pivot
            if k != i:
                elementary[k][i] = ((-1) * matrix[k][i]) / matrix[i][i]
                e_temp1 = mul_two_matrix(elementary, e_temp1)
                save_matrix = matrix
                matrix = mul_two_matrix(elementary, matrix)
                print_format(elementary, save_matrix, matrix)  # Prints the steps of the solution
                elementary = make_matrix(len(matrix), len(matrix))
    v = mul_matrix_vector(e_temp1, vector_b)
    print_solution(v)  # prints the solution vector


_matrix = [[2, 1, 0], [3, -1, 0], [1, 4, -2]]
_vector_b = [-3, 1, -5]

print("The source matrix:")
print_matrix(_matrix)
if determinant_of_matrix(_matrix) == 0:
    print("The determinant = ", determinant_of_matrix(_matrix))
else:
    print("The determinant = ", determinant_of_matrix(_matrix))
    print()
    print()
    find(_matrix, _vector_b)
