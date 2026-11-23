# Chapter 4: Repetition Structures

## Key Concepts

### Why Repetition Structures?

- Copying the same code over and over makes a program long, slow to write, and hard to fix (a change has to be made in every copy).
- A **repetition structure** (a **loop**) runs a block of statements as many times as needed. The code is written once.
- Two kinds of loops:
  - **Condition-controlled**: repeats while a condition is true (`while` loop).
  - **Count-controlled**: repeats a set number of times (`for` loop).

### The `while` Loop (Condition-Controlled)

- Runs its block **as long as** the condition is `True`.
- The condition is tested **before** each pass, so `while` is a **pretest loop**. If the condition is `False` at the start, the block never runs.
- Each pass through the block is one **iteration**.
- Like `if`, the header ends with a colon `:` and the block must be indented.
- Something inside the loop must eventually make the condition `False`, otherwise the loop never stops.

### Infinite Loops

- An **infinite loop** never ends because nothing in the block changes the condition.
- Usually a bug, e.g. forgetting to update the variable the condition tests.
- Press **Ctrl+C** to stop a program stuck in an infinite loop.

### The `for` Loop (Count-Controlled)

- Runs once for **each item** in a sequence (a list, a string, a `range`, …).
- The **target variable** is assigned the next item at the start of each iteration.
- The number of iterations is known before the loop starts: it equals the number of items.
- The target variable can be used inside the loop, but changing it does not affect which item comes next.

### The `range` Function

- `range` creates a sequence of integers, mostly used with `for` loops.
- Arguments work like this:

  | Call               | Values produced       | Notes                         |
  |--------------------|-----------------------|-------------------------------|
  | `range(5)`         | 0, 1, 2, 3, 4         | starts at 0, stops **before** 5 |
  | `range(1, 6)`      | 1, 2, 3, 4, 5         | start, stop                   |
  | `range(0, 11, 2)`  | 0, 2, 4, 6, 8, 10     | start, stop, step             |
  | `range(10, 0, -1)` | 10, 9, 8, … 1         | negative step counts down     |

- The **stop** value is never included.
- The user's input can set the number of iterations: `range(int(input(...)))`.

### Calculating a Running Total

- A **running total** adds up numbers as the loop goes.
- Uses an **accumulator** variable, which must be set to `0` **before** the loop. Setting it inside the loop would reset it every iteration.
- Each iteration adds the next value to the accumulator.

### Augmented Assignment Operators

- Shorthand for updating a variable using its own value:

  | Operator | Example    | Same as        |
  |----------|------------|----------------|
  | `+=`     | `x += 5`   | `x = x + 5`    |
  | `-=`     | `x -= 2`   | `x = x - 2`    |
  | `*=`     | `x *= 10`  | `x = x * 10`   |
  | `/=`     | `x /= 2`   | `x = x / 2`    |
  | `%=`     | `x %= 4`   | `x = x % 4`    |
  | `//=`    | `x //= 3`  | `x = x // 3`   |
  | `**=`    | `x **= 2`  | `x = x ** 2`   |

### Sentinels

- A **sentinel** is a special value that marks the end of a list of input, used when the number of items isn't known ahead of time.
- The loop keeps going until the user enters the sentinel.
- The sentinel must be a value that could never be real data (e.g. `0` or `-1` for a property value, an empty string for a name).

### Input Validation Loops

- **GIGO**: "garbage in, garbage out". A program can't give correct output from bad input.
- An **input validation loop** keeps asking until the user enters valid data.
- Pattern:
  1. Get the input once before the loop (the **priming read**).
  2. `while` the input is invalid: show an error and ask again.
- An error trap can check ranges, types, or specific allowed values, often with logical operators from Chapter 3.

### Nested Loops

- A **nested loop** is a loop inside another loop.
- The inner loop runs **all** of its iterations for **each** iteration of the outer loop.
- Total iterations = outer iterations × inner iterations.
- Classic example: a clock — the seconds loop runs 60 times for every minute, the minutes loop runs 60 times for every hour.
- Useful for rows and columns (tables, patterns of characters).

### Turtle Graphics: Using Loops to Draw Designs

- Loops make repeated shapes easy: a square is "forward, turn 90°" four times.
- For a regular polygon with `n` sides, turn `360 / n` degrees each time.
- Repeating a shape while turning a little each time creates circular designs (e.g. 36 circles, turning 10° between each).

## Syntax to Remember

### `while` Loop

```python
keep_going = 'y'

while keep_going == 'y':
    sales = float(input('Enter the amount of sales: '))
    commission = sales * 0.10
    print(f'The commission is ${commission:,.2f}')
    keep_going = input('Another one? (y = yes): ')   # updates the condition
```

### Infinite Loop (Bug)

```python
count = 1
while count <= 5:
    print(count)
    # forgot: count += 1  -> prints 1 forever (Ctrl+C to stop)
```

### `for` Loop

```python
# Over a list
for num in [1, 2, 3, 4, 5]:
    print(num)

# Over a string: one character at a time
for ch in 'Hi!':
    print(ch)          # H, i, !
```

### `range`

```python
for x in range(5):
    print(x, end=' ')            # 0 1 2 3 4

for x in range(1, 6):
    print(x, end=' ')            # 1 2 3 4 5

for x in range(0, 11, 2):
    print(x, end=' ')            # 0 2 4 6 8 10

for x in range(10, 0, -1):
    print(x, end=' ')            # 10 9 8 7 6 5 4 3 2 1

# Table of squares
print('Number\tSquare')
for number in range(1, 6):
    print(f'{number}\t{number ** 2}')

# User decides how many times
times = int(input('How many times? '))
for i in range(times):
    print('Hello')
```

### Running Total with an Accumulator

```python
MAX = 5
total = 0.0                    # accumulator starts at 0, BEFORE the loop

for counter in range(MAX):
    number = float(input('Enter a number: '))
    total += number            # same as total = total + number

print(f'The total is {total}')
```

### Sentinel

```python
total_tax = 0.0

lot = int(input('Enter the lot number (0 to quit): '))   # priming read
while lot != 0:                                          # 0 is the sentinel
    value = float(input('Enter the property value: '))
    tax = value * 0.0065
    total_tax += tax
    lot = int(input('Enter the next lot number (0 to quit): '))

print(f'Total property tax: ${total_tax:,.2f}')
```

### Input Validation Loop

```python
score = int(input('Enter a test score (0-100): '))   # priming read

while score < 0 or score > 100:                      # invalid -> ask again
    print('ERROR: The score must be between 0 and 100.')
    score = int(input('Enter a test score (0-100): '))

print(f'Valid score: {score}')
```

### Nested Loops

```python
# Clock: inner loop finishes completely for each outer iteration
for hours in range(24):
    for minutes in range(60):
        for seconds in range(60):
            print(f'{hours:02}:{minutes:02}:{seconds:02}')

# Rectangle of asterisks: rows x columns
rows = 3
cols = 6
for r in range(rows):
    for c in range(cols):
        print('*', end='')
    print()                    # new line after each row

# Right triangle
for r in range(5):
    for c in range(r + 1):
        print('*', end='')
    print()
```

### Turtle Loops

```python
import turtle

# Square
for x in range(4):
    turtle.forward(100)
    turtle.right(90)

# Regular polygon with n sides
sides = 6
for x in range(sides):
    turtle.forward(80)
    turtle.left(360 / sides)

# Circular design: 36 circles, turning 10 degrees each time
for x in range(36):
    turtle.circle(50)
    turtle.left(10)
```

## Questions / To Review

-
