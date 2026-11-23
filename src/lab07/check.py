import random
from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials: int = 100) -> int:
    checks = 0
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)
        result = fn(nums)
        assert result == sorted(nums), f"{fn.__name__} ошиблась на {nums}: {result}"
        assert nums == original, f"{fn.__name__} изменила исходный список"
        checks += 1
    return checks


def check_search(trials: int = 100) -> int:
    checks = 0
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]
        candidates = nums + [-999, 999, 0]

        for x in candidates:
            expected_lin = nums.index(x) if x in nums else -1
            got_lin = linear_search(nums, x)
            assert got_lin == expected_lin, f"linear_search({nums}, {x}) -> {got_lin}, ждали {expected_lin}"
            checks += 1

        s_nums = sorted(nums)
        for x in candidates:
            got_bin = binary_search(s_nums, x)
            if x in s_nums:
                assert 0 <= got_bin < len(s_nums) and s_nums[got_bin] == x, (
                    f"binary_search({s_nums}, {x}) вернул неверный индекс {got_bin}"
                )
            else:
                assert got_bin == -1, f"binary_search({s_nums}, {x}) -> {got_bin}, ждали -1"
            checks += 1
    return checks


def check_two_sum(trials: int = 100) -> int:
    checks = 0
    for _ in range(trials):
        n = random.randint(0, 30)
        nums = [random.randint(-50, 50) for _ in range(n)]
        targets = [-200, 0, 200]
        if n >= 2:
            i, j = random.sample(range(n), 2)
            targets.append(nums[i] + nums[j])

        for target in targets:
            res_brute = two_sum_brute(nums, target)
            res_fast = two_sum_fast(nums, target)

            if res_brute is None:
                assert res_fast is None, f"two_sum разошлись на {nums}, target={target}: brute=None, fast={res_fast}"
            else:
                assert res_fast is not None, f"two_sum разошлись на {nums}, target={target}: brute={res_brute}, fast=None"
                i, j = res_fast
                assert 0 <= i < j < n and nums[i] + nums[j] == target, (
                    f"two_sum_fast вернула неверную пару {res_fast} на {nums}, target={target}"
                )
            checks += 1
    return checks


if __name__ == "__main__":
    random.seed(42)
    total = 0
    for fn in (bubble_sort, insertion_sort, selection_sort):
        total += check_sorting(fn)
    total += check_search()
    total += check_two_sum()
    print(f"OK: {total} проверок")
