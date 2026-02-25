def largest_element(arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest


arr = [10, 5, 20, 8, 25, 3]
print(largest_element(arr))
