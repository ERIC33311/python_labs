def check_matrix(m):
    c = len(m[0])
    for i in range(len(m)):
        if len(m[i]) != c:
            raise ValueError

# === 1 ===
def transpose(m):
    if len(m) == 0:
        return []
    check_matrix(m)
    t = []
    num_rows = len(m)
    num_cols = len(m[0])
    for j in range(num_cols):
        new_row = []
        for i in range(num_rows):
            new_row.append(m[i][j])
        t.append(new_row)
    return t

# Тест-кейсы
try:
    print("transpose([[1, 2, 3]]) ->", transpose([[1, 2, 3]]))
except ValueError:
    print("transpose([[1, 2, 3]]) -> ValueError")

try:
    print("transpose([[1], [2], [3]]) ->", transpose([[1], [2], [3]]))
except ValueError:
    print("transpose([[1], [2], [3]]) -> ValueError")

try:
    print("transpose([[1, 2], [3, 4]]) ->", transpose([[1, 2], [3, 4]]))
except ValueError:
    print("transpose([[1, 2], [3, 4]]) -> ValueError")

try:
    print("transpose([]) ->", transpose([]))
except ValueError:
    print("transpose([]) -> ValueError")

try:
    print("transpose([[1, 2], [3]]) ->", transpose([[1, 2], [3]]))
except ValueError:
    print("transpose([[1, 2], [3]]) -> ValueError")


# === 2 ===
def row_sums(m):
    check_matrix(m)
    result = []
    for i in range(len(m)):
        result.append(sum(m[i]))
    return result

# Тест-кейсы
try:
    print("row_sums([[1, 2, 3], [4, 5, 6]]) ->", row_sums([[1, 2, 3], [4, 5, 6]]))
except ValueError:
    print("row_sums([[1, 2, 3], [4, 5, 6]]) -> ValueError")
try:
    print("row_sums([[-1, 1], [10, -10]]) ->", row_sums([[-1, 1], [10, -10]]))
except ValueError:
    print("row_sums([[-1, 1], [10, -10]]) -> ValueError")
try:
    print("row_sums([[0, 0], [0, 0]]) ->", row_sums([[0, 0], [0, 0]]))
except ValueError:
    print("row_sums([[0, 0], [0, 0]]) -> ValueError")
try:
    print("row_sums([[1, 2], [3]]) ->", row_sums([[1, 2], [3]]))
except ValueError:
    print("row_sums([[1, 2], [3]]) -> ValueError")


# === 3 ===
def col_sums(m):
    check_matrix(m)
    result = []
    for j in range(len(m[0])):
        sum_col = 0
        for i in range(len(m)):
            sum_col += m[i][j]
        result.append(sum_col)
    return result

# Тест-кейсы
try:
    print("col_sums([[1, 2, 3], [4, 5, 6]]) ->", col_sums([[1, 2, 3], [4, 5, 6]]))
except ValueError:
    print("col_sums([[1, 2, 3], [4, 5, 6]]) -> ValueError")

try:
    print("col_sums([[-1, 1], [10, -10]]) ->", col_sums([[-1, 1], [10, -10]]))
except ValueError:
    print("col_sums([[-1, 1], [10, -10]]) -> ValueError")

try:
    print("col_sums([[0, 0], [0, 0]]) ->", col_sums([[0, 0], [0, 0]]))
except ValueError:
    print("col_sums([[0, 0], [0, 0]]) -> ValueError")

try:
    print("col_sums([[1, 2], [3]]) ->", col_sums([[1, 2], [3]]))
except ValueError:
    print("col_sums([[1, 2], [3]]) -> ValueError")