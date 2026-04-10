# Given a number n, replace every 0 digit in it with 5.
# Input: n = 1004
# Output: 1554
# Input: n = 121
# Output: 121

n = int(input("Enter a number: "))

if n == 0:
    result = 5
else:
    result = 0
    place = 1
    while n > 0:
        digit = n % 10
        if digit == 0:
            digit = 5
        result += digit * place
        place *= 10
        n //= 10

print(result)
