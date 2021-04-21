# игры с матрицами

class Matrix:
    def __init__(self, matrix):
        self.matrix = list(matrix)

    def __str__(self):
        string_matrix = ""
        for line in self.matrix:
            string_matrix += str(line) + "\n"
        return string_matrix

    def __add__(self, other_matrix):
        result = self.matrix
        if isinstance(other_matrix, Matrix) and len(self.matrix) == len(other_matrix.matrix) \
                and len(self.matrix[0]) == len(other_matrix.matrix[0]):
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[0])):
                    result[i][j] += other_matrix.matrix[i][j]
            return Matrix(result)
        else:
            print("Ошибка! Матрицы не соразмерны")
            pass


a = [
    [1, 6, 4, 3],
    [4, 2, 1, 9],
    [3, 7, 1, 5]
]

b = [
    [1, 6, 4, 3, 1],
    [4, 2, 1, 9, 5],
    [3, 7, 1, 5, 3],
]

c = [
    [1, 6, 4, 3],
    [4, 2, 1, 9],
    [3, 7, 1, 5],
    [2, 2, 2, 2]
]

first = Matrix(a)
second = Matrix(c)

third = first + second
print(third)
