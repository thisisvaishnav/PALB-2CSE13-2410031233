def min_swaps(arr, k):
    n = len(arr)
    count = 0
    for x in arr:
        if x <= k:
            count += 1
    bad = 0
    for i in range(count):
        if arr[i] > k:
            bad += 1
    min_bad = bad
    for i in range(count, n):
        if arr[i] > k:
            bad += 1
        if arr[i - count] > k:
            bad -= 1
        if bad < min_bad:
            min_bad = bad
    return min_bad


arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))
print("Minimum swaps:", min_swaps(arr, k))
