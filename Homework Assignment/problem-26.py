def find_median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


arr = list(map(int, input("Enter array elements: ").split()))
print("Median:", find_median(arr))
