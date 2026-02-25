def set_zeroes(matrix):
    m = len(matrix)
    n = len(matrix[0])
    zero_rows = []
    zero_cols = []
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                zero_rows.append(i)
                zero_cols.append(j)
    for i in zero_rows:
        for j in range(n):
            matrix[i][j] = 0
    for j in zero_cols:
        for i in range(m):
            matrix[i][j] = 0
    return matrix


m = int(input("Enter rows: "))
n = int(input("Enter cols: "))
matrix = []
for i in range(m):
    row = list(map(int, input("Enter row: ").split()))
    matrix.append(row)
result = set_zeroes(matrix)
print("Result:")
for row in result:
    print(row)
