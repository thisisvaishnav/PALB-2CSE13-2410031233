def factorial_digits(n):
    fact = 1
    for i in range(2, n + 1):
        fact = fact * i
    result = []
    for ch in str(fact):
        result.append(int(ch))
    return result


n = int(input("Enter n: "))
print("Factorial digits:", factorial_digits(n))
