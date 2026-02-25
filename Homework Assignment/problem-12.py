def minimize_height(arr, k):
    n = len(arr)
    arr.sort()
    result = arr[n - 1] - arr[0]
    for i in range(1, n):
        if arr[i] - k < 0:
            continue
        high = max(arr[n - 1] - k, arr[i - 1] + k)
        low = min(arr[0] + k, arr[i] - k)
        result = min(result, high - low)
    return result


arr = list(map(int, input("Enter tower heights: ").split()))
k = int(input("Enter k: "))
print("Minimum difference:", minimize_height(arr, k))
