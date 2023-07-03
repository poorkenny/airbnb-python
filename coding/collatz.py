step_map = {}


def find_steps(num):
    if num <= 1:
        return 1
    if num in step_map:
        return step_map[num]
    if num % 2 == 0:
        return 1 + find_steps(num // 2)
    return 1 + find_steps(3 * num + 1)


def find_longest_steps(num):
    if num < 1:
        return 0
    res = 0
    for i in range(1, num + 1):
        t = find_steps(i)
        step_map[i] = t
        res = max(res, t)
    return res


def main():
    test_cases = [10, 20, 50, 100, 200]  # Example test cases

    for num in test_cases:
        longest_steps = find_longest_steps(num)
        print(f"The number {num} has the longest steps of {longest_steps}.")


if __name__ == "__main__":
    main()
