def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1
    jumps = 0
    farthest = 0
    current_end = 0
    for i in range(n - 1):
        if i + arr[i] > farthest:
            farthest = i + arr[i]
        if i == current_end:
            jumps += 1
            current_end = farthest
            if current_end >= n - 1:
                return jumps
    return -1


arr = list(map(int, input("Enter array elements: ").split()))
print("Minimum jumps:", min_jumps(arr))
