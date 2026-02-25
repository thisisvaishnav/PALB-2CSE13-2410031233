def is_subset(a, b):
    for x in b:
        count_a = 0
        count_b = 0
        for y in a:
            if y == x:
                count_a += 1
        for y in b:
            if y == x:
                count_b += 1
        if count_b > count_a:
            return False
    return True


a = list(map(int, input("Enter array a: ").split()))
b = list(map(int, input("Enter array b: ").split()))
if is_subset(a, b):
    print("Yes, b is a subset of a")
else:
    print("No, b is not a subset of a")
