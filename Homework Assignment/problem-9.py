def merge_without_extra_space(a, b):
    n = len(a)
    m = len(b)
    i = n - 1
    j = 0
    while i >= 0 and j < m:
        if a[i] > b[j]:
            a[i], b[j] = b[j], a[i]
        i -= 1
        j += 1
    a.sort()
    b.sort()


a = [1, 3, 5, 7]
b = [0, 2, 6, 8, 9]
merge_without_extra_space(a, b)
print(a)
print(b)
