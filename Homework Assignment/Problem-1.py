class Solution:
    def rotate(self, arr):
        n = len(arr)
        if n <= 1:
            return

        last = arr[n - 1]
        for i in range(n - 1, 0, -1):
            arr[i] = arr[i - 1]
        arr[0] = last


if __name__ == "__main__":
    sol = Solution()

    arr1 = [1, 2, 3, 4, 5]
    sol.rotate(arr1)
    print(arr1)  # [5, 1, 2, 3, 4]

    arr2 = [9, 8, 7, 6, 4, 2, 1, 3]
    sol.rotate(arr2)
    print(arr2)  # [3, 9, 8, 7, 6, 4, 2, 1]
