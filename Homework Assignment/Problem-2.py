def union_of_arrays(a, b):
    result = set()
    for x in a:
        result.add(x)
    for x in b:
        result.add(x)
    return list(result)


a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print(union_of_arrays(a, b))
