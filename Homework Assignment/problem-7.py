def max_subarray_sum(arr):
    current_sum = arr[0]
    max_sum = arr[0]
    for i in range(1, len(arr)):
        if current_sum + arr[i] > arr[i]:
            current_sum = current_sum + arr[i]
        else:
            current_sum = arr[i]
        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum


arr = list(map(int, input("Enter array elements: ").split()))
print("Maximum subarray sum:", max_subarray_sum(arr))
