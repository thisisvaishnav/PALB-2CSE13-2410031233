def matrix_median(mat):
    n = len(mat)
    m = len(mat[0])
    all_elements = []
    for i in range(n):
        for j in range(m):
            all_elements.append(mat[i][j])
    all_elements.sort()
    return all_elements[(n * m) // 2]


n = int(input("Enter rows: "))
m = int(input("Enter cols: "))
mat = []
for i in range(n):
    row = list(map(int, input("Enter row: ").split()))
    mat.append(row)
print("Median:", matrix_median(mat))
