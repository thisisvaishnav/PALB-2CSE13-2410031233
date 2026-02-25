def kth_smallest(arr, k):
    arr.sort()
    return arr[k - 1]


arr = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter k: "))
print("Kth smallest element:", kth_smallest(arr, k))
