def chocolate_distribution(arr, m):
    arr.sort()
    min_diff = arr[m - 1] - arr[0]
    for i in range(1, len(arr) - m + 1):
        diff = arr[i + m - 1] - arr[i]
        if diff < min_diff:
            min_diff = diff
    return min_diff


arr = list(map(int, input("Enter chocolates in packets: ").split()))
m = int(input("Enter number of students: "))
print("Minimum difference:", chocolate_distribution(arr, m))
