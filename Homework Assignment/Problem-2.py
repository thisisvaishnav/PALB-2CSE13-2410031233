def find_min_max(arr):
    minimum = arr[0]
    maximum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < minimum:
            minimum = arr[i]
        if arr[i] > maximum:
            maximum = arr[i]
    return minimum, maximum


arr = list(map(int, input("Enter array elements: ").split()))
mn, mx = find_min_max(arr)
print("Minimum:", mn)
print("Maximum:", mx)
