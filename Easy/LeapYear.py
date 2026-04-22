# Given a year, print "Leap Year" if it is a leap year, otherwise "Not a Leap Year".
# A year is a leap year if it is divisible by 4 but not by 100, or if it is divisible by 400.
# Input: 2000
# Output: Leap Year
# Input: 1900
# Output: Not a Leap Year

year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap Year")
else:
    print("Not a Leap Year")
