def spiral_order(mat):
    result = []
    top = 0
    bottom = len(mat) - 1
    left = 0
    right = len(mat[0]) - 1
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(mat[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(mat[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1
    return result


n = int(input("Enter rows: "))
m = int(input("Enter cols: "))
mat = []
for i in range(n):
    row = list(map(int, input("Enter row: ").split()))
    mat.append(row)
print("Spiral order:", spiral_order(mat))
