# Chapter 2: Input, Processing, and Output

## Key Concepts

- Learned how to use format specifiers in f-strings to control how numbers are printed.
- Format specifiers go after a colon inside the braces: `{value:specifier}`.

## Syntax to Remember

```python
num = 1234567.891
discount = 0.25

print(f'{num:,}')        # 1,234,567.891  -> comma as thousands separator
print(f'{discount:.0%}') # 25%            -> percentage with 0 decimal places
print(f'{num:.2e}')      # 1.23e+06       -> scientific notation, 2 decimal places
```

### Minimum Field Width

A number before the type sets the minimum number of spaces the value takes up.
Numbers are right-aligned by default, so extra space is padded on the left.
If the value is wider than the field, the field grows to fit it.

```python
print(f'{42:10}')           # '        42'  -> 10 wide, right-aligned
print(f'{3.14159:10.2f}')   # '      3.14'  -> 10 wide, 2 decimal places
print(f'{1234567:12,}')     # '   1,234,567' -> 12 wide with comma separator
print(f'{0.25:8.0%}')       # '     25%'   -> 8 wide percentage
print(f'{123456:3}')        # '123456'      -> value wider than field, not cut off

# Useful for lining up columns
print(f'{1.5:8.2f}{22.75:8.2f}')     # '    1.50   22.75'
print(f'{100.0:8.2f}{3.333:8.2f}')   # '  100.00    3.33'
```

### Aligning Values (Alignment Designators)

By default, numbers are right-aligned and strings are left-aligned in a field.
An alignment designator placed before the width changes this:

| Designator | Meaning      |
|------------|--------------|
| `<`        | Left-align   |
| `>`        | Right-align  |
| `^`        | Center-align |

```python
print(f'{42:<10}')        # '42        '  -> left-aligned
print(f'{42:>10}')        # '        42'  -> right-aligned
print(f'{42:^10}')        # '    42    '  -> centered

print(f'{"Hi":10}')       # 'Hi        '  -> strings are left-aligned by default
print(f'{"Hi":>10}')      # '        Hi'  -> right-aligned string

# Combine with other specifiers: alignment, width, then precision/type
print(f'{3.14159:^10.2f}')   # '   3.14   '
print(f'{1234567:<12,}')     # '1,234,567   '

# Lining up a small table
print(f'{"Item":<10}{"Price":>8}')     # 'Item         Price'
print(f'{"Apple":<10}{1.5:>8.2f}')     # 'Apple         1.50'
print(f'{"Banana":<10}{22.75:>8.2f}')  # 'Banana       22.75'
```

### Order of Designators

When using several designators together, they must be written in this order:

```
{value:[alignment][width][,][.precision][type]}
```

Each part is optional, but the ones you use must stay in this order.

```python
num = 1234.5678

print(f'{num:>12,.2f}')   # '    1,234.57'  -> right, width 12, comma, 2 decimals, float
print(f'{num:<12,.1f}')   # '1,234.6     '  -> left, width 12, comma, 1 decimal, float
print(f'{num:^12.0f}')    # '    1235    '  -> centered, width 12, 0 decimals
print(f'{0.256:>8.1%}')   # '   25.6%'      -> right, width 8, 1 decimal, percent

# Wrong order gives an error:
# print(f'{num:.2f>12}')  # ValueError: Invalid format specifier '.2f>12'
```

### Concatenating f-strings

**With the `+` operator** — joins f-strings into one string:

```python
name = 'Ashish'
age = 30

message = f'Name: {name}. ' + f'Age: {age}.'
print(message)   # Name: Ashish. Age: 30.
```

**Implicit concatenation** — string literals placed next to each other are joined automatically.
Wrapping them in parentheses lets one long f-string be split across several lines:

```python
price = 1234.5
discount = 0.15

print(f'Price: ${price:,.2f}  '
      f'Discount: {discount:.0%}  '
      f'Total: ${price * (1 - discount):,.2f}')
# Price: $1,234.50  Discount: 15%  Total: $1,049.33
```

Each piece that contains `{}` needs its own `f` prefix. Without it, the braces are printed as plain text:

```python
print(f'Name: {name}, '
      'Age: {age}')     # Name: Ashish, Age: {age}   <- second part is missing the f
```

## Mistakes I Made

-

## Questions / To Review

-
