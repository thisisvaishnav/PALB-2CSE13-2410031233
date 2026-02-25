def min_jumps(nums):
    n = len(nums)
    if n <= 1:
        return 0
    jumps = 0
    farthest = 0
    current_end = 0
    for i in range(n - 1):
        if i + nums[i] > farthest:
            farthest = i + nums[i]
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                return jumps
    return jumps


nums = list(map(int, input("Enter array elements: ").split()))
print("Minimum jumps:", min_jumps(nums))
