# Chapter 3: Decision Structures and Boolean Logic

## Key Concepts

### Control Structures

- A **control structure** decides the order in which statements run.
- **Sequence structure**: statements run one after another, top to bottom (everything in Chapters 1–2).
- **Decision structure** (selection structure): runs some statements **only if** a condition is true. Lets a program take different paths.

### The `if` Statement

- Runs a block of code only when a condition is `True`.
- The line starting with `if` is the **clause header** and must end with a colon `:`.
- The statements under it form a **block** and must be **indented** the same amount (4 spaces by convention). Indentation is how Python knows where the block ends.
- If the condition is `False`, the block is skipped and the program carries on after it.

### Boolean Expressions and Relational Operators

- A **Boolean expression** evaluates to either `True` or `False`.
- **Relational operators** compare two values:

  | Operator | Meaning                  | Example  | Result  |
  |----------|--------------------------|----------|---------|
  | `>`      | Greater than             | `5 > 3`  | `True`  |
  | `<`      | Less than                | `5 < 3`  | `False` |
  | `>=`     | Greater than or equal to | `5 >= 5` | `True`  |
  | `<=`     | Less than or equal to    | `4 <= 3` | `False` |
  | `==`     | Equal to                 | `5 == 5` | `True`  |
  | `!=`     | Not equal to             | `5 != 3` | `True`  |

- `=` **assigns** a value. `==` **compares** two values. Mixing them up is a common bug.

### The `if-else` Statement

- A **dual-alternative** decision: one block runs if the condition is true, the other block runs if it is false. Exactly one of the two always runs.
- `if` and `else` must line up at the same indentation level.

### Comparing Strings

- Strings can be compared with all the relational operators.
- `==` is **case-sensitive**: `'Mary' == 'mary'` is `False`.
- `<` and `>` compare strings **character by character** using their character codes (ASCII/Unicode, see Chapter 1).
  - Uppercase letters (`'A'` = 65 … `'Z'` = 90) come **before** lowercase letters (`'a'` = 97 … `'z'` = 122).
  - The first pair of characters that differ decides the result: `'Mary' < 'Mark'` is `False` because `'y'` (121) > `'k'` (107).
  - If one string is the start of the other, the shorter one is smaller: `'Hi' < 'High'` is `True`.

### Nested Decision Structures and `if-elif-else`

- A **nested decision** is an `if` inside another `if` or `else` block. Used when a second condition should only be checked after the first one passes.
- Each nested level must be indented further.
- Long chains of nested `if-else` get deeply indented and hard to read. **`elif`** ("else if") flattens them:
  - Conditions are tested **top to bottom**.
  - The block for the **first** true condition runs, and the rest are skipped.
  - The final `else` is optional and runs only if no condition was true.
- Order matters: put the most specific (or highest) condition first, or a broader one will catch the value too early.

### Logical Operators

- Combine or reverse Boolean expressions:

  | Operator | Result is `True` when…           |
  |----------|----------------------------------|
  | `and`    | **both** sides are true          |
  | `or`     | **at least one** side is true    |
  | `not`    | the expression is false (flips it) |

- Truth table:

  | `a`     | `b`     | `a and b` | `a or b` | `not a` |
  |---------|---------|-----------|----------|---------|
  | `True`  | `True`  | `True`    | `True`   | `False` |
  | `True`  | `False` | `False`   | `True`   | `False` |
  | `False` | `True`  | `False`   | `True`   | `True`  |
  | `False` | `False` | `False`   | `False`  | `True`  |

- **Short-circuit evaluation**: Python stops as soon as it knows the answer.
  - `and`: if the left side is `False`, the right side is **not** checked.
  - `or`: if the left side is `True`, the right side is **not** checked.
- **Precedence**: `not` is evaluated first, then `and`, then `or`. Relational operators (`<`, `==`, …) are evaluated before all three. Use parentheses when in doubt.

### Checking Numeric Ranges

- **Inside a range**: use `and` — the value must be above the low end **and** below the high end.
- **Outside a range**: use `or` — the value is below the low end **or** above the high end.
- Python also allows **chained comparisons**: `10 <= x <= 20` means the same as `10 <= x and x <= 20`.

### Boolean Variables

- A **Boolean variable** holds `True` or `False` (type `bool`). Note the capital letters.
- Often used as a **flag**: a variable that signals whether some condition exists in the program.
- A flag can be tested directly — no need to write `== True`.

### Turtle Graphics: Checking the Turtle's State

- The turtle module has functions that return information, so they can be used in `if` statements:
  - `turtle.xcor()`, `turtle.ycor()` — current X and Y position.
  - `turtle.heading()` — current direction in degrees.
  - `turtle.isdown()` — `True` if the pen is down.
  - `turtle.isvisible()` — `True` if the turtle is showing.
  - `turtle.pencolor()`, `turtle.fillcolor()`, `turtle.bgcolor()` — current colours.
  - `turtle.pensize()`, `turtle.speed()` — current pen width and animation speed.

## Syntax to Remember

### `if`, `if-else`, `if-elif-else`

```python
sales = float(input('Enter your sales: '))

# if: runs only when the condition is true
if sales > 50000:
    print('You earned a bonus!')

# if-else: one of the two blocks always runs
if sales > 50000:
    bonus = 500.0
else:
    bonus = 0.0

# if-elif-else: first true condition wins
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'      # 85 lands here; the checks below are skipped
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'F'
print(f'Grade: {grade}')   # Grade: B
```

### Nested Decision

```python
salary = 35000
years_on_job = 3

if salary >= 30000:
    if years_on_job >= 2:
        print('You qualify for the loan.')
    else:
        print('You must have been on the job at least 2 years.')
else:
    print('You must earn at least $30,000 per year.')
```

### Comparing Strings

```python
print('Mary' == 'mary')   # False -> case-sensitive
print('a' > 'B')          # True  -> 'a' is 97, 'B' is 66
print('Mary' < 'Mark')    # False -> 'y' (121) > 'k' (107)
print('Hi' < 'High')      # True  -> shorter prefix is smaller

# Case-insensitive comparison: convert both sides first
answer = input('Continue? (y/n): ')
if answer.lower() == 'y':
    print('Continuing...')
```

### Logical Operators and Ranges

```python
temperature = 15

# and: both must be true
if temperature > 10 and temperature < 25:
    print('Nice weather')

# or: at least one must be true
if temperature < 0 or temperature > 35:
    print('Extreme weather')

# not: flips the result
if not (temperature > 30):
    print('Not too hot')

# Inside a range
x = 15
if x >= 10 and x <= 20:
    print('In range')
if 10 <= x <= 20:          # same thing, chained comparison
    print('In range')

# Outside a range
if x < 10 or x > 20:
    print('Out of range')

# Short-circuit: the division is never evaluated when count is 0
count = 0
total = 100
if count != 0 and total / count > 10:
    print('High average')
```

### Boolean Variables (Flags)

```python
sales_quota = 50000
sales = 62000

sales_quota_met = sales >= sales_quota   # stores True or False

if sales_quota_met:          # no need for '== True'
    print('You met your sales quota!')

if not sales_quota_met:
    print('Keep going.')
```

### Turtle State

```python
import turtle

if turtle.isdown():
    turtle.penup()

if turtle.heading() == 0:     # facing east
    turtle.left(90)

if turtle.xcor() > 100 or turtle.ycor() > 100:
    turtle.goto(0, 0)
```

## Questions / To Review

-
