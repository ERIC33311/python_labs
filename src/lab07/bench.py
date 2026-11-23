import csv
from pathlib import Path
import random
import timeit

from src.lab04.io_txt_csv import write_csv
from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def get_numbers(n: int) -> list[int]:
    sample_path = Path(f"data/samples/lab07/numbers_{n}.csv")
    if sample_path.exists():
        with sample_path.open(encoding="utf-8") as f:
            return [int(row["value"]) for row in csv.DictReader(f)]
    return [random.randint(-100_000, 100_000) for _ in range(n)]


def bench_sorts(n: int) -> list[tuple]:
    data = get_numbers(n)
    rows = []

    t_sorted = timeit.timeit(lambda: sorted(data), number=1)
    rows.append(("sort", n, "sorted", f"{t_sorted:.6f}"))

    algos = [
        ("bubble_sort", bubble_sort),
        ("insertion_sort", insertion_sort),
        ("selection_sort", selection_sort),
    ]

    for name, fn in algos:
        if n >= 100_000:
            rows.append(("sort", n, name, "> 60 s"))
        else:
            t = timeit.timeit(lambda f=fn: f(data), number=1)
            rows.append(("sort", n, name, f"{t:.6f}"))

    return rows


def bench_search() -> list[tuple]:
    n = 100_000
    queries_count = 10_000
    data = get_numbers(n)
    queries = [
        random.choice(data) if i % 2 == 0 else random.randint(-200_000, 200_000)
        for i in range(queries_count)
    ]

    rows = []
    t_lin = timeit.timeit(lambda: [linear_search(data, q) for q in queries], number=1)
    rows.append(("search_10k", n, "linear_search", f"{t_lin:.6f}"))

    t_prep = timeit.timeit(lambda: sorted(data), number=1)
    sorted_data = sorted(data)
    rows.append(("search_10k", n, "binary_sort_prep", f"{t_prep:.6f}"))

    t_bin = timeit.timeit(lambda: [binary_search(sorted_data, q) for q in queries], number=1)
    rows.append(("search_10k", n, "binary_search", f"{t_bin:.6f}"))

    return rows


def bench_two_sum(n: int) -> list[tuple]:
    data = get_numbers(n)
    target = data[0] + data[-1]
    rows = []

    t_brute = timeit.timeit(lambda: two_sum_brute(data, target), number=1)
    rows.append(("two_sum", n, "two_sum_brute", f"{t_brute:.6f}"))

    t_fast = timeit.timeit(lambda: two_sum_fast(data, target), number=1)
    rows.append(("two_sum", n, "two_sum_fast", f"{t_fast:.6f}"))

    return rows


def main() -> None:
    random.seed(42)
    all_rows: list[tuple] = []

    for n in (1_000, 10_000, 100_000):
        all_rows.extend(bench_sorts(n))

    all_rows.extend(bench_search())

    for n in (1_000, 10_000):
        all_rows.extend(bench_two_sum(n))

    header = ("task", "n", "impl", "seconds")
    print(f"{header[0]:<12} | {header[1]:>8} | {header[2]:<18} | {header[3]:>10}")
    print("-" * 57)
    for task, n, impl, sec in all_rows:
        print(f"{task:<12} | {n:>8} | {impl:<18} | {sec:>10}")

    out_path = Path("data/lab07/bench.csv")
    write_csv(all_rows, out_path, header=header)


if __name__ == "__main__":
    main()
