def row_with_max_ones(arr):
    n = len(arr)
    m = len(arr[0])
    
    max_ones = 0
    result_index = -1
    
    for i in range(n):
        row = arr[i]
        left, right = 0, m - 1
        first_one = m
        
        while left <= right:
            mid = (left + right) // 2
            if row[mid] == 1:
                first_one = mid
                right = mid - 1
            else:
                left = mid + 1
        
        ones_count = m - first_one
        
        if ones_count > max_ones:
            max_ones = ones_count
            result_index = i
    
    return result_index if max_ones > 0 else -1


# Example 1
arr1 = [[0,1,1,1], [0,0,1,1], [1,1,1,1], [0,0,0,0]]
print("Output:", row_with_max_ones(arr1))

# Example 2
arr2 = [[0,0], [1,1]]
print("Output:", row_with_max_ones(arr2))

# Example 3
arr3 = [[0,0], [0,0]]
print("Output:", row_with_max_ones(arr3))