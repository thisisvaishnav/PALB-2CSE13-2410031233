def is_subset(a, b):
    freq = {}
    for x in a:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    for x in b:
        if x not in freq or freq[x] == 0:
            return False
        freq[x] -= 1
    return True


a = [1, 2, 3, 4, 5, 6]
b = [1, 2, 4]
print(is_subset(a, b))

a = [10, 5, 2, 23, 19]
b = [19, 5, 3]
print(is_subset(a, b))
