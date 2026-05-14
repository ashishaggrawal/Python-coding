# Given a number n, print the smallest prime number strictly greater than n.
# Input: n = 10
# Output: 11
# Input: n = 13
# Output: 17

n = int(input("Enter a number: "))

candidate = n + 1
while True:
    is_prime = candidate > 1
    i = 2
    while i * i <= candidate:
        if candidate % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        break
    candidate += 1

print(candidate)
