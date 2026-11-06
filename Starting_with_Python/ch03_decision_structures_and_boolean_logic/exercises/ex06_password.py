# This program checks if the password entered by user matches with password stored
# String comparison
PASSWD_STORED = "prospero"

password = input("Enter your password: ")

if password == PASSWD_STORED:
    print("Access Granted")
else:
    print("Access Denied")


# Conditional expression: Alternate way of writing if-else statements

print("Access Granted") if password == PASSWD_STORED else print("Access Denied")

# Walrus operator := is used to assign a value to a variable and return the value

print(test :=27)

# Example 2:


print("Full Time") if (hours := int(input("Enter your hours: "))) >35 else print("Part Time")
