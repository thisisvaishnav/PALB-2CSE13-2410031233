def search_insert(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return low


arr = list(map(int, input("Enter sorted array: ").split()))
target = int(input("Enter target: "))
print("Index:", search_insert(arr, target))
