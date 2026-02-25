def triplet_sum(arr, target):
    arr.sort()
    n = len(arr)
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == target:
                return True
            elif total < target:
                left += 1
            else:
                right -= 1
    return False


arr = [1, 4, 45, 6, 10, 8]
target = 22
print(triplet_sum(arr, target))
