# Given an array of numbers, print the rightmost non-zero digit of their product.
# If the product is 0, print -1.
# Input: 3 23 30 45
# Output: 5   (3 * 23 * 30 * 45 = 93150)
# Input: 5 8 3 7 8
# Output: 2   (5 * 8 * 3 * 7 * 8 = 6720)

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Factors of 2 and 5 pair up to make trailing zeros, so count them separately
# and keep only the last digit of everything else (the product can be huge).
twos = 0
fives = 0
last = 1
for num in numbers:
    if num == 0:
        last = -1
        break
    while num % 2 == 0:
        num //= 2
        twos += 1
    while num % 5 == 0:
        num //= 5
        fives += 1
    last = (last * num) % 10

if last == -1:
    print(-1)
else:
    # Multiply back the 2s or 5s that did not get paired into a zero.
    pairs = min(twos, fives)
    for i in range(twos - pairs):
        last = (last * 2) % 10
    for i in range(fives - pairs):
        last = (last * 5) % 10
    print(last)
