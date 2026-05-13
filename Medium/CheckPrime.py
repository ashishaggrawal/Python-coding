# Given a number n, print "Prime" if it is a prime number, otherwise "Not Prime".
# Input: n = 7
# Output: Prime
# Input: n = 10
# Output: Not Prime

n = int(input("Enter a number: "))

is_prime = n > 1
i = 2
while i * i <= n:
    if n % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print("Prime")
else:
    print("Not Prime")
