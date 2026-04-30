class solution:
    def findUnion(self, a, b):
        Union_set = set(a) | set(b)
        return list(Union_set)
    
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]

obj = solution()
ans = obj.findUnion(a, b)

print(*sorted(ans))