def plus_one(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        total = digits[i] + carry
        digits[i] = total % 10
        carry = total // 10
    if carry == 1:
        digits.insert(0, 1)
    return digits


digits = list(map(int, input("Enter digits: ").split()))
print("Result:", plus_one(digits))
