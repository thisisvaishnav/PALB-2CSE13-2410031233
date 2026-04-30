def min_swaps(arr, k):
    n = len(arr)
    good = sum(1 for x in arr if x <= k)
    bad = sum(1 for i in range(good) if arr[i] > k)
    ans = bad
    i = 0
    j = good
    
    while j < n:
        
        if arr[i] > k:
            bad -= 1
        
        if arr[j] > k:
            bad += 1
        
        ans = min(ans, bad)
        i += 1
        j += 1
    
    return ans


# Example 1
arr1 = [2, 1, 5, 6, 3]
k1 = 3
print("Output:", min_swaps(arr1, k1))

# Example 2
arr2 = [2, 7, 9, 5, 8, 7, 4]
k2 = 6
print("Output:", min_swaps(arr2, k2))

# Example 3
arr3 = [2, 4, 5, 3, 6, 1, 8]
k3 = 6
print("Output:", min_swaps(arr3, k3))