# Take a name and an age from the user and print them.
# input() always returns a string, so the age is converted with int().
# Input: name = Ashish, age = 25
# Output: Hello Ashish, next year you will be 26

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Hello " + name + ", next year you will be", age + 1)
