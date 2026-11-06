# Chapter 1: Introduction to Computers and Programming

## Key Concepts

### Hardware and Software

- **Hardware** = the physical parts of a computer. Main components:
  - **CPU** (Central Processing Unit): the part that actually runs programs.
  - **Main memory (RAM)**: fast, temporary storage for programs and data while they run. Erased when the power is off (volatile).
  - **Secondary storage**: keeps data long term even without power (hard drives, SSDs, USB drives).
  - **Input devices**: collect data from the user (keyboard, mouse, microphone).
  - **Output devices**: send data out (screen, printer, speakers).
- **Software** = programs. Two main types:
  - **System software**: operating systems (Windows, macOS, Linux), utility programs, and software development tools (compilers, interpreters).
  - **Application software**: programs people use for everyday tasks (browsers, games, word processors).

### How Computers Store Data

- Memory is divided into **bytes**. One byte = **8 bits**.
- A **bit** is a single on/off switch: `1` (on) or `0` (off).
- **Binary** (base 2) is the number system computers use. Each position is a power of 2:

  | Bit position | 7   | 6  | 5  | 4  | 3 | 2 | 1 | 0 |
  |--------------|-----|----|----|----|---|---|---|---|
  | Value        | 128 | 64 | 32 | 16 | 8 | 4 | 2 | 1 |

  Example: `10011101` = 128 + 16 + 8 + 4 + 1 = **157**
- One byte can hold numbers from **0 to 255** (all bits on = 255). Bigger numbers use more bytes.
- **Characters** are stored as number codes:
  - **ASCII**: 128 codes for English letters, digits and symbols. `'A'` = 65, `'a'` = 97, `'0'` = 48.
  - **Unicode**: a much larger set that covers almost every language. Its first 128 codes match ASCII.
- **Negative numbers** use a method called *two's complement*. **Real numbers** (decimals) use *floating-point* notation.
- **Images, sound, video** are also just numbers. An image is a grid of **pixels**, and each pixel's colour is stored as a number.
- This is called **digital** data: everything is stored as binary numbers.

### How a Program Works

- The CPU only understands **machine language**: instructions written as 1s and 0s.
- The CPU repeats the **fetch-decode-execute cycle**:
  1. **Fetch** the next instruction from memory.
  2. **Decode** it to work out what operation to do.
  3. **Execute** the operation.
- **Assembly language** uses short words (mnemonics) like `add`, `mul`, `mov` instead of binary. An **assembler** turns it into machine language. Still low-level and hard to write.
- **High-level languages** (Python, C++, Java) let you write programs in words close to English. One line can replace many machine instructions.
- Parts of a high-level language:
  - **Keywords** (reserved words): words with special meaning that can't be used for anything else, e.g. `if`, `while`, `def`, `True`, `None`.
  - **Operators**: symbols that do operations on data, e.g. `+`, `-`, `*`, `/`.
  - **Syntax**: the rules for how code must be written. Breaking them gives a **syntax error**.
  - **Statements**: individual instructions in a program.
- **Source code** = the code the programmer writes. It must be translated to machine language:
  - **Compiler**: translates the whole program into a separate machine-language file, which is then run.
  - **Interpreter**: translates and runs **one instruction at a time**. No separate file is made. **Python uses an interpreter.**

### Using Python

- **Interactive mode**: type a statement at the `>>>` prompt and Python runs it straight away. Good for testing small ideas.
- **Script mode**: save statements in a `.py` file and run the whole file. Used for real programs.
- **IDLE** is the editor that comes with Python. It has an interactive shell and a script editor (run with **F5**).
- Python is **case-sensitive**: `print` works, `Print` gives an error.

## Syntax to Remember

```python
# Interactive mode
>>> print('Python programming is fun!')
Python programming is fun!
```

```python
# Script mode: save as hello.py, then run with:  python hello.py
print('Nudge nudge')
print('Wink wink')
print('Know what I mean?')
```

```python
# Built-in helpers for checking number systems and character codes
print(bin(157))         # 0b10011101  -> decimal to binary
print(int('10011101', 2))  # 157      -> binary to decimal
print(ord('A'))         # 65          -> character to its code
print(chr(65))          # A           -> code to character
```

## Mistakes I Made

-

## Questions / To Review

-
