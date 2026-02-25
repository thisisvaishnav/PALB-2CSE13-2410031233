def merge_sorted(a, b):
    n = len(a)
    m = len(b)
    for i in range(n - 1, -1, -1):
        if a[i] > b[0]:
            a[i], b[0] = b[0], a[i]
            b.sort()
    return a, b


a = list(map(int, input("Enter first sorted array: ").split()))
b = list(map(int, input("Enter second sorted array: ").split()))
a, b = merge_sorted(a, b)
print("First array:", a)
print("Second array:", b)
