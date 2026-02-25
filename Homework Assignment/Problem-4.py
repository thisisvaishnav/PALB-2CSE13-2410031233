def union_arrays(a, b):
    result = []
    for x in a:
        if x not in result:
            result.append(x)
    for x in b:
        if x not in result:
            result.append(x)
    result.sort()
    return result


a = list(map(int, input("Enter first array: ").split()))
b = list(map(int, input("Enter second array: ").split()))
print("Union:", union_arrays(a, b))
