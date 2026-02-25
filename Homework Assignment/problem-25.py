def is_palindrome(num):
    s = str(num)
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def all_palindromes(arr):
    for x in arr:
        if not is_palindrome(x):
            return False
    return True


arr = list(map(int, input("Enter array elements: ").split()))
if all_palindromes(arr):
    print("True")
else:
    print("False")
