def smallest_subarray(arr, x):
    n = len(arr)
    min_len = n + 1
    start = 0
    current_sum = 0
    for end in range(n):
        current_sum += arr[end]
        while current_sum > x:
            length = end - start + 1
            if length < min_len:
                min_len = length
            current_sum -= arr[start]
            start += 1
    if min_len == n + 1:
        return 0
    return min_len


arr = list(map(int, input("Enter array elements: ").split()))
x = int(input("Enter x: "))
print("Smallest subarray length:", smallest_subarray(arr, x))
