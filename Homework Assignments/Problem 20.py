def trap_rain_water(arr):
    n = len(arr)
    if n == 0:
        return 0

    left = 0
    right = n - 1
    left_max = 0
    right_max = 0
    water = 0

    while left < right:
        if arr[left] < arr[right]:
            if arr[left] >= left_max:
                left_max = arr[left]
            else:
                water += left_max - arr[left]
            left += 1
        else:
            if arr[right] >= right_max:
                right_max = arr[right]
            else:
                water += right_max - arr[right]
            right -= 1

    return water

arr1 = [3, 0, 1, 0, 4, 0, 2]
arr2 = [3, 0, 2, 0, 4]
arr3 = [1, 2, 3, 4]
arr4 = [2, 1, 5, 3, 1, 0, 4]

print("Input:", arr1)
print("Output:", trap_rain_water(arr1))

print("\nInput:", arr2)
print("Output:", trap_rain_water(arr2))

print("\nInput:", arr3)
print("Output:", trap_rain_water(arr3))

print("\nInput:", arr4)
print("Output:", trap_rain_water(arr4))