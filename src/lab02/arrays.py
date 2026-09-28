# === 1 ===
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """Возвращает (минимум, максимум) списка m. Пустой список -> ValueError."""
    if not nums:
        raise ValueError("список пуст")
    low = high = nums[0]
    for x in nums:
        if x < low:
            low = x
        if x > high:
            high = x
    return low, high

# Тест-кейсы
try:
    print("min_max([3, -1, 5, 5, 0]) ->", min_max([3, -1, 5, 5, 0]))
except ValueError:
    print("min_max([3, -1, 5, 5, 0]) -> ValueError (список пуст)")

try:
    print("min_max([42]) ->", min_max([42]))
except ValueError:
    print("min_max([42]) -> ValueError (список пуст)")

try:
    print("min_max([-5, -2, -9]) ->", min_max([-5, -2, -9]))
except ValueError:
    print("min_max([-5, -2, -9]) -> ValueError (список пуст)")

try:
    print("min_max([]) ->", min_max([]))
except ValueError:
    print("min_max([]) -> ValueError (список пуст)")

try:
    print("min_max([1.5, 2, 2.0, -3.1]) ->", min_max([1.5, 2, 2.0, -3.1]))
except ValueError:
    print("min_max([1.5, 2, 2.0, -3.1]) -> ValueError (список пуст)")


# === 2 ===
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """Возвращает отсортированный по возрастанию список уникальных значений m."""
    m = list(set(nums))
    result = []
    a = m[:]
    for _ in range(len(a)):
        min_sym = m[0]
        for i in m:
            if i < min_sym: 
                min_sym = i
        result.append(min_sym)
        m.remove(min_sym)
    return result

# Тест-кейсы
print("unique_sorted([3, 1, 2, 1, 3]) ->", unique_sorted([3, 1, 2, 1, 3]))
print("unique_sorted([]) ->", unique_sorted([]))
print("unique_sorted([-1, -1, 0, 2, 2]) ->", unique_sorted([-1, -1, 0, 2, 2]))
print("unique_sorted([1.0, 1, 2.5, 2.5, 0]) ->", unique_sorted([1.0, 1, 2.5, 2.5, 0]))


# === 3 ===
def check_matrix(mat):
    """Проверяет, что каждый элемент m — список или кортеж. Иначе -> TypeError."""
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError("строка не является списком/кортежем")

def flatten(mat: list[list | tuple]) -> list:
    """Расплющивает список списков/кортежей в один плоский список (по строкам)."""
    if not isinstance(mat, list):
        raise TypeError("строка/элемент не является списком/кортежем")
    
    check_matrix(mat)
    result = []
    for row in mat:
        for x in row:
            result.append(x)
    return result

# Тест-кейсы
try:
    print("flatten([[1, 2], [3, 4]]) ->", flatten([[1, 2], [3, 4]]))
except TypeError:
    print("flatten([[1, 2], [3, 4]]) -> TypeError (строка/элемент не является списком/кортежем)")

try:
    print("flatten([[1, 2], (3, 4, 5)]) ->", flatten([[1, 2], (3, 4, 5)]))
except TypeError:
    print("flatten([[1, 2], (3, 4, 5)]) -> TypeError (строка/элемент не является списком/кортежем)")

try:
    print("flatten([[1], [], [2, 3]]) ->", flatten([[1], [], [2, 3]]))
except TypeError:
    print("flatten([[1], [], [2, 3]]) -> TypeError (строка/элемент не является списком/кортежем)")

try:
    print("flatten([[1, 2], 'ab']) ->", flatten([[1, 2], "ab"]))
except TypeError:
    print("flatten([[1, 2], 'ab']) -> TypeError (строка/элемент не является списком/кортежем)")