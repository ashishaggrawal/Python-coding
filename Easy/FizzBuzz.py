# Given a number n, print numbers from 1 to n. For multiples of 3 print "Fizz",
# for multiples of 5 print "Buzz", and for multiples of both print "FizzBuzz".
# Input: n = 15
# Output: 1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz

n = int(input("Enter a number: "))

for i in range(1, n + 1):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")

print()
