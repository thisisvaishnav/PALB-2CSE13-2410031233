def combination_sum2(candidates, target):
    result = []

    def solve(start, current, total):
        if total == target:
            result.append(list(current))
            return
        if total > target:
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            current.append(candidates[i])
            solve(i + 1, current, total + candidates[i])
            current.pop()

    candidates.sort()
    solve(0, [], 0)
    return result


candidates = list(map(int, input("Enter candidates: ").split()))
target = int(input("Enter target: "))
print("Combinations:", combination_sum2(candidates, target))
