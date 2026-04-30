def is_subset(a, b):
    freq = {}
    for num in a:
        freq[num] = freq.get(num, 0) + 1
    
    for num in b:
        if num not in freq or freq[num] == 0:
            return False
        freq[num] -= 1
    
    return True
a1 = [11, 7, 1, 13, 21, 3, 7, 3]
b1 = [11, 3, 7, 1, 7]
print("Output:", is_subset(a1, b1))

a2 = [1, 2, 3, 4, 4, 5, 6]
b2 = [1, 2, 4]
print("Output:", is_subset(a2, b2))

a3 = [10, 5, 2, 23, 19]
b3 = [19, 5, 3]
print("Output:", is_subset(a3, b3))
