def search_matrix(mat, target):
    m = len(mat)
    n = len(mat[0])
    low = 0
    high = m * n - 1
    while low <= high:
        mid = (low + high) // 2
        row = mid // n
        col = mid % n
        if mat[row][col] == target:
            return True
        elif mat[row][col] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False


n = int(input("Enter rows: "))
m = int(input("Enter cols: "))
mat = []
for i in range(n):
    row = list(map(int, input("Enter row: ").split()))
    mat.append(row)
target = int(input("Enter target: "))
print(search_matrix(mat, target))
