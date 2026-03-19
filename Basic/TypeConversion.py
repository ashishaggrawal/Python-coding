# Convert values between int, float, str and bool, and print each result with its type.
# Input: 42
# Output:
# 42 <class 'str'>
# 42 <class 'int'>
# 42.0 <class 'float'>
# True <class 'bool'>

s = input("Enter a number: ")
print(s, type(s))

n = int(s)
print(n, type(n))

f = float(n)
print(f, type(f))

b = bool(n)    # 0 becomes False, every other number becomes True
print(b, type(b))
