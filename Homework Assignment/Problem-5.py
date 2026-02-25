def largest_element(arr):
    largest = arr[0]
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest


arr = list(map(int, input("Enter array elements: ").split()))
print("Largest element:", largest_element(arr))
