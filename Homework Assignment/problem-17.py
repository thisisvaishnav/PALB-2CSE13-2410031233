def common_elements(a, b, c):
    i = 0
    j = 0
    k = 0
    result = []
    while i < len(a) and j < len(b) and k < len(c):
        if a[i] == b[j] == c[k]:
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])
            i += 1
            j += 1
            k += 1
        elif a[i] < b[j]:
            i += 1
        elif b[j] < c[k]:
            j += 1
        else:
            k += 1
    if len(result) == 0:
        return [-1]
    return result


a = list(map(int, input("Enter first sorted array: ").split()))
b = list(map(int, input("Enter second sorted array: ").split()))
c = list(map(int, input("Enter third sorted array: ").split()))
print("Common elements:", common_elements(a, b, c))
