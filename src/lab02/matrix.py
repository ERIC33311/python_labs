def check_matrix(mat):
    """Проверяет, что матрица прямоугольная (все строки одной длины). Иначе -> ValueError."""
    c = len(mat[0])
    for i in range(len(mat)):
        if len(mat[i]) != c:
            raise ValueError("матрица «рваная»")

# === 1 ===
def transpose(mat: list[list[float | int]]) -> list[list]:
    """Транспонирует матрицу (меняет строки и столбцы местами). Пустая матрица -> []."""
    if len(mat) == 0:
        return []
    check_matrix(mat)
    t = []
    num_rows = len(mat)
    num_cols = len(mat[0])
    for j in range(num_cols):
        new_row = []
        for i in range(num_rows):
            new_row.append(mat[i][j])
        t.append(new_row)
    return t

# Тест-кейсы
try:
    print("transpose([[1, 2, 3]]) ->", transpose([[1, 2, 3]]))
except ValueError:
    print("transpose([[1, 2, 3]]) -> ValueError (матрица «рваная»)")

try:
    print("transpose([[1], [2], [3]]) ->", transpose([[1], [2], [3]]))
except ValueError:
    print("transpose([[1], [2], [3]]) -> ValueError (матрица «рваная»)")

try:
    print("transpose([[1, 2], [3, 4]]) ->", transpose([[1, 2], [3, 4]]))
except ValueError:
    print("transpose([[1, 2], [3, 4]]) -> ValueError (матрица «рваная»)")

try:
    print("transpose([]) ->", transpose([]))
except ValueError:
    print("transpose([]) -> ValueError (матрица «рваная»)")

try:
    print("transpose([[1, 2], [3]]) ->", transpose([[1, 2], [3]]))
except ValueError:
    print("transpose([[1, 2], [3]]) -> ValueError (матрица «рваная»)")


# === 2 ===
def row_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает список сумм по каждой строке матрицы m."""
    check_matrix(mat)
    result = []
    for i in range(len(mat)):
        result.append(sum(mat[i]))
    return result

# Тест-кейсы
try:
    print("row_sums([[1, 2, 3], [4, 5, 6]]) ->", row_sums([[1, 2, 3], [4, 5, 6]]))
except ValueError:
    print("row_sums([[1, 2, 3], [4, 5, 6]]) -> ValueError (матрица «рваная»)")
try:
    print("row_sums([[-1, 1], [10, -10]]) ->", row_sums([[-1, 1], [10, -10]]))
except ValueError:
    print("row_sums([[-1, 1], [10, -10]]) -> ValueError (матрица «рваная»)")
try:
    print("row_sums([[0, 0], [0, 0]]) ->", row_sums([[0, 0], [0, 0]]))
except ValueError:
    print("row_sums([[0, 0], [0, 0]]) -> ValueError (матрица «рваная»)")
try:
    print("row_sums([[1, 2], [3]]) ->", row_sums([[1, 2], [3]]))
except ValueError:
    print("row_sums([[1, 2], [3]]) -> ValueError (матрица «рваная»)")


# === 3 ===
def col_sums(mat: list[list[float | int]]) -> list[float]:
    """Возвращает список сумм по каждому столбцу матрицы m."""
    check_matrix(mat)
    result = []
    for j in range(len(mat[0])):
        sum_col = 0
        for i in range(len(mat)):
            sum_col += mat[i][j]
        result.append(sum_col)
    return result

# Тест-кейсы
try:
    print("col_sums([[1, 2, 3], [4, 5, 6]]) ->", col_sums([[1, 2, 3], [4, 5, 6]]))
except ValueError:
    print("col_sums([[1, 2, 3], [4, 5, 6]]) -> ValueError (матрица «рваная»)")

try:
    print("col_sums([[-1, 1], [10, -10]]) ->", col_sums([[-1, 1], [10, -10]]))
except ValueError:
    print("col_sums([[-1, 1], [10, -10]]) -> ValueError (матрица «рваная»)")

try:
    print("col_sums([[0, 0], [0, 0]]) ->", col_sums([[0, 0], [0, 0]]))
except ValueError:
    print("col_sums([[0, 0], [0, 0]]) -> ValueError (матрица «рваная»)")

try:
    print("col_sums([[1, 2], [3]]) ->", col_sums([[1, 2], [3]]))
except ValueError:
    print("col_sums([[1, 2], [3]]) -> ValueError (матрица «рваная»)")