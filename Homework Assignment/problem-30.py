def row_with_max_ones(arr):
    max_count = 0
    result = -1
    for i in range(len(arr)):
        count = 0
        for j in range(len(arr[i])):
            if arr[i][j] == 1:
                count += 1
        if count > max_count:
            max_count = count
            result = i
    return result


n = int(input("Enter rows: "))
m = int(input("Enter cols: "))
arr = []
for i in range(n):
    row = list(map(int, input("Enter row: ").split()))
    arr.append(row)
print("Row with max 1s:", row_with_max_ones(arr))
