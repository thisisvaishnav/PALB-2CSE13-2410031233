def minDifference(arr, m):
    n = len(arr)
    if m==0 or n==0:
        return 0;

    if m > n:
        return -1

    arr.sort()

    min_diff = float('inf')

    for i in range(n - m + 1):
        diff = arr[i + m - 1] - arr[i]
        min_diff = min(min_diff, diff)

    return min_diff


arr = [7, 3, 2, 4, 9, 12, 56]
m = 3

print(minDifference(arr, m))
