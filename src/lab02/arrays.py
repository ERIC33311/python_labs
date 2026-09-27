# === 1 ===
def min_max(m):
    if not m:
        raise ValueError("")
    low = high = m[0]
    for x in m:
        if x < low:
            low = x
        if x > high:
            high = x
    return low, high

# Тест-кейсы
try:
    print("min_max([3, -1, 5, 5, 0]) ->", min_max([3, -1, 5, 5, 0]))
except ValueError:
    print("min_max([3, -1, 5, 5, 0]) -> ValueError")

try:
    print("min_max([42]) ->", min_max([42]))
except ValueError:
    print("min_max([42]) -> ValueError")

try:
    print("min_max([-5, -2, -9]) ->", min_max([-5, -2, -9]))
except ValueError:
    print("min_max([-5, -2, -9]) -> ValueError")

try:
    print("min_max([]) ->", min_max([]))
except ValueError:
    print("min_max([]) -> ValueError")

try:
    print("min_max([1.5, 2, 2.0, -3.1]) ->", min_max([1.5, 2, 2.0, -3.1]))
except ValueError:
    print("min_max([1.5, 2, 2.0, -3.1]) -> ValueError")


# === 2 ===
def unique_sorted(m):
    m = list(set(m))
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
def check_matrix(m):
    for row in m:
        if not isinstance(row, (list, tuple)):
            raise TypeError

def flatten(m):
    if not isinstance(m, list):
        raise TypeError
    
    check_matrix(m)
    result = []
    for row in m:
        for x in row:
            result.append(x)
    return result

# Тест-кейсы
try:
    print("flatten([[1, 2], [3, 4]]) ->", flatten([[1, 2], [3, 4]]))
except TypeError:
    print("flatten([[1, 2], [3, 4]]) -> TypeError")

try:
    print("flatten([[1, 2], (3, 4, 5)]) ->", flatten([[1, 2], (3, 4, 5)]))
except TypeError:
    print("flatten([[1, 2], (3, 4, 5)]) -> TypeError")

try:
    print("flatten([[1], [], [2, 3]]) ->", flatten([[1], [], [2, 3]]))
except TypeError:
    print("flatten([[1], [], [2, 3]]) -> TypeError")

try:
    print("flatten([[1, 2], 'ab']) ->", flatten([[1, 2], "ab"]))
except TypeError:
    print("flatten([[1, 2], 'ab']) -> TypeError")