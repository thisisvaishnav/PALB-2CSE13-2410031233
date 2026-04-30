def has_triplet_sum(arr, target):
    n = len(arr)
    arr.sort()  

    for i in range(n - 2):
        left = i + 1
        right = n - 1
        
        while left < right:
            curr_sum = arr[i] + arr[left] + arr[right]
            
            if curr_sum == target:
                return True
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
                
    return False
arr = [1, 4, 45, 6, 10, 8]
target = 13
print(has_triplet_sum(arr, target))

arr = [1, 2, 4, 3, 6, 7]
target = 10
print(has_triplet_sum(arr, target))

arr = [40, 20, 10, 3, 6, 7]
target = 24
print(has_triplet_sum(arr, target))
