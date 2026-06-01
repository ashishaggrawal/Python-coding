# Python Coding Practice

Solutions to 70+ programming problems in Python, in two parts:

- **[Data Structures & Algorithms](#data-structures--algorithms):** 30 classic interview problems covering hashing, two pointers, sliding windows, linked lists, trees, backtracking, dynamic programming and graphs. Each comes with a written explanation, complexity analysis and sample output.
- **[Fundamentals](#fundamentals):** 40+ problems organized by difficulty, from language basics to number theory and pattern printing.

Every solution is a standalone script with the problem statement and worked examples at the top. The fundamentals set is also solved in C: [C-Programming](https://github.com/ashishaggrawal/C-Programming).

## Topics Covered

- **Data structures:** hash maps and sets, heaps, linked lists, binary trees and BSTs, graphs
- **Algorithm patterns:** two pointers, sliding window, prefix/suffix products, BFS/DFS, backtracking, topological sort, dynamic programming, binary search
- **Language fundamentals:** variables, input/output, type conversion, comments
- **Operators:** arithmetic, logical and bitwise
- **Control flow:** `if` / `elif` / `else`, `for` and `while` loops, `break`
- **Nested loops:** star, number and diamond patterns
- **Number theory:** primes, GCD (Euclidean algorithm), LCM, divisors, factorials, Fibonacci
- **Problem solving:** digit manipulation, avoiding overflow in large products, edge-case handling

## Repository Structure

```
├── DSA/
│   ├── ArraysHashing/          Hashing and two-pointer problems
│   ├── SlidingWindow/          Variable-size window problems
│   ├── LinkedListsTrees/       Linked lists, binary trees and BSTs
│   └── BacktrackingDPGraphs/   Backtracking, dynamic programming and graphs
├── Basic/     Language fundamentals and operators
├── Easy/      Conditionals and single loops
├── Medium/    Nested loops, patterns and number theory
├── Hard/      Multi-step algorithmic problems
└── *.py       Standalone practice problems
```

## Data Structures & Algorithms

Each problem has a solution (`.py`) and an explanation (`.md`) covering the approach, time and space complexity, and the program's output. Where two approaches are worth knowing, both are implemented and compared.

### Arrays, Hashing & Two Pointers

| # | Problem | Approach | Time | Explanation |
|---|---------|----------|------|-------------|
| 1 | [Two Sum](DSA/ArraysHashing/TwoSum.py) | Hash map of complements | O(n) | [Read](DSA/ArraysHashing/TwoSum.md) |
| 2 | [Best Time to Buy and Sell Stock](DSA/ArraysHashing/BestTimeToBuyAndSellStock.py) | Track running minimum | O(n) | [Read](DSA/ArraysHashing/BestTimeToBuyAndSellStock.md) |
| 3 | [Contains Duplicate](DSA/ArraysHashing/ContainsDuplicate.py) | Hash set | O(n) | [Read](DSA/ArraysHashing/ContainsDuplicate.md) |
| 4 | [Group Anagrams](DSA/ArraysHashing/GroupAnagrams.py) | Letter-count tuple as key | O(n·k) | [Read](DSA/ArraysHashing/GroupAnagrams.md) |
| 5 | [Top K Frequent Elements](DSA/ArraysHashing/TopKFrequentElements.py) | Bucket sort / heap | O(n) | [Read](DSA/ArraysHashing/TopKFrequentElements.md) |
| 6 | [Product of Array Except Self](DSA/ArraysHashing/ProductOfArrayExceptSelf.py) | Prefix and suffix products | O(n) | [Read](DSA/ArraysHashing/ProductOfArrayExceptSelf.md) |
| 7 | [Valid Palindrome](DSA/ArraysHashing/ValidPalindrome.py) | Two pointers | O(n) | [Read](DSA/ArraysHashing/ValidPalindrome.md) |
| 8 | [3Sum](DSA/ArraysHashing/ThreeSum.py) | Sort + two pointers | O(n²) | [Read](DSA/ArraysHashing/ThreeSum.md) |
| 9 | [Container With Most Water](DSA/ArraysHashing/ContainerWithMostWater.py) | Greedy two pointers | O(n) | [Read](DSA/ArraysHashing/ContainerWithMostWater.md) |
| 10 | [Trapping Rain Water](DSA/ArraysHashing/TrappingRainWater.py) | Two pointers with side maxima | O(n) | [Read](DSA/ArraysHashing/TrappingRainWater.md) |

### Sliding Window

| # | Problem | Approach | Time | Explanation |
|---|---------|----------|------|-------------|
| 1 | [Longest Substring Without Repeating Characters](DSA/SlidingWindow/LongestSubstringWithoutRepeatingCharacters.py) | Window with last-index map | O(n) | [Read](DSA/SlidingWindow/LongestSubstringWithoutRepeatingCharacters.md) |
| 2 | [Longest Repeating Character Replacement](DSA/SlidingWindow/LongestRepeatingCharacterReplacement.py) | Window with max frequency | O(n) | [Read](DSA/SlidingWindow/LongestRepeatingCharacterReplacement.md) |
| 3 | [Minimum Window Substring](DSA/SlidingWindow/MinimumWindowSubstring.py) | Expand/shrink with two count maps | O(n + m) | [Read](DSA/SlidingWindow/MinimumWindowSubstring.md) |

### Linked Lists & Trees

| # | Problem | Approach | Time | Explanation |
|---|---------|----------|------|-------------|
| 1 | [Reverse a Linked List](DSA/LinkedListsTrees/ReverseLinkedList.py) | Iterative pointer reversal | O(n) | [Read](DSA/LinkedListsTrees/ReverseLinkedList.md) |
| 2 | [Merge Two Sorted Lists](DSA/LinkedListsTrees/MergeTwoSortedLists.py) | Dummy head splicing | O(n + m) | [Read](DSA/LinkedListsTrees/MergeTwoSortedLists.md) |
| 3 | [Linked List Cycle](DSA/LinkedListsTrees/LinkedListCycle.py) | Floyd's tortoise and hare | O(n) | [Read](DSA/LinkedListsTrees/LinkedListCycle.md) |
| 4 | [Invert Binary Tree](DSA/LinkedListsTrees/InvertBinaryTree.py) | Recursive / queue-based | O(n) | [Read](DSA/LinkedListsTrees/InvertBinaryTree.md) |
| 5 | [Maximum Depth of Binary Tree](DSA/LinkedListsTrees/MaximumDepthOfBinaryTree.py) | DFS / BFS | O(n) | [Read](DSA/LinkedListsTrees/MaximumDepthOfBinaryTree.md) |
| 6 | [Validate Binary Search Tree](DSA/LinkedListsTrees/ValidateBinarySearchTree.py) | Min/max bounds | O(n) | [Read](DSA/LinkedListsTrees/ValidateBinarySearchTree.md) |
| 7 | [Lowest Common Ancestor of a BST](DSA/LinkedListsTrees/LowestCommonAncestorOfBST.py) | BST value comparison | O(h) | [Read](DSA/LinkedListsTrees/LowestCommonAncestorOfBST.md) |
| 8 | [Binary Tree Level Order Traversal](DSA/LinkedListsTrees/BinaryTreeLevelOrderTraversal.py) | BFS with `deque` | O(n) | [Read](DSA/LinkedListsTrees/BinaryTreeLevelOrderTraversal.md) |
| 9 | [Construct Binary Tree from Preorder and Inorder](DSA/LinkedListsTrees/ConstructBinaryTreeFromPreorderAndInorder.py) | Recursive partitioning with index map | O(n) | [Read](DSA/LinkedListsTrees/ConstructBinaryTreeFromPreorderAndInorder.md) |

### Backtracking, Dynamic Programming & Graphs

| # | Problem | Approach | Time | Explanation |
|---|---------|----------|------|-------------|
| 1 | [Combination Sum](DSA/BacktrackingDPGraphs/CombinationSum.py) | Backtracking with pruning | Exponential | [Read](DSA/BacktrackingDPGraphs/CombinationSum.md) |
| 2 | [Word Search](DSA/BacktrackingDPGraphs/WordSearch.py) | In-place grid DFS | O(m·n·3^L) | [Read](DSA/BacktrackingDPGraphs/WordSearch.md) |
| 3 | [Number of Islands](DSA/BacktrackingDPGraphs/NumberOfIslands.py) | BFS flood fill | O(m·n) | [Read](DSA/BacktrackingDPGraphs/NumberOfIslands.md) |
| 4 | [Clone Graph](DSA/BacktrackingDPGraphs/CloneGraph.py) | DFS with node-to-copy map | O(V + E) | [Read](DSA/BacktrackingDPGraphs/CloneGraph.md) |
| 5 | [Course Schedule](DSA/BacktrackingDPGraphs/CourseSchedule.py) | Kahn's algorithm / DFS cycle check | O(V + E) | [Read](DSA/BacktrackingDPGraphs/CourseSchedule.md) |
| 6 | [Climbing Stairs](DSA/BacktrackingDPGraphs/ClimbingStairs.py) | Fibonacci DP, O(1) space | O(n) | [Read](DSA/BacktrackingDPGraphs/ClimbingStairs.md) |
| 7 | [Coin Change](DSA/BacktrackingDPGraphs/CoinChange.py) | Unbounded knapsack DP | O(n·amount) | [Read](DSA/BacktrackingDPGraphs/CoinChange.md) |
| 8 | [Longest Increasing Subsequence](DSA/BacktrackingDPGraphs/LongestIncreasingSubsequence.py) | DP / patience sorting with `bisect` | O(n log n) | [Read](DSA/BacktrackingDPGraphs/LongestIncreasingSubsequence.md) |

## Fundamentals

### Basic

| # | Problem | Concepts |
|---|---------|----------|
| 1 | [Start Coding](Basic/StartCoding.py) | First program, `print` |
| 2 | [Learn to Comment](Basic/LearnToComment.py) | Single-line and multi-line comments |
| 3 | [Printing](Basic/Printing.py) | `print` with `sep` and `end` |
| 4 | [Int Str](Basic/IntStr.py) | Combining numbers and strings with `str()` |
| 5 | [Input](Basic/Input.py) | Reading user input, `int()` conversion |
| 6 | [Arithmetic Operators](Basic/ArithmeticOperators.py) | `+ - * / // % **` |
| 7 | [Logical Operators](Basic/LogicalOperators.py) | `and`, `or`, `not` |
| 8 | [Bitwise Operators](Basic/BitwiseOperators.py) | `& \| ^ ~ << >>` |
| 9 | [Type Conversion](Basic/TypeConversion.py) | `int`, `float`, `str`, `bool` |
| 10 | [Type Cast and Double It](Basic/TypeCastAndDoubleIt.py) | String to integer casting |
| 11 | [Swap the Numbers](Basic/SwapTheNumbers.py) | Tuple unpacking |
| 12 | [Geometric Progression](Basic/GeometricProgression.py) | Generating a sequence with a loop |
| 13 | [Multi Printing](Basic/MultiPrinting.py) | Repetition with `for` |

### Easy

| # | Problem | Concepts |
|---|---------|----------|
| 1 | [For Loop](Easy/ForLoop.py) | `range` counting up |
| 2 | [For Loop 2](Easy/ForLoop2.py) | `range` with a negative step |
| 3 | [While Loop](Easy/WhileLoop.py) | Reverse multiplication table |
| 4 | [Jumping through While](Easy/JumpingThroughWhile.py) | Custom loop increments |
| 5 | [Zero Converter](Easy/ZeroConverter.py) | Digit extraction with `%` and `//` |
| 6 | [The Else Statement](Easy/TheElseStatement.py) | `if` / `elif` / `else` |
| 7 | [FizzBuzz](Easy/FizzBuzz.py) | Divisibility checks, condition ordering |
| 8 | [Even Odd Game](Easy/EvenOddGame.py) | Parity check |
| 9 | [Greatest of Three](Easy/GreatestOfThree.py) | Compound conditions |
| 10 | [Leap Year](Easy/LeapYear.py) | Calendar rules with `and` / `or` |
| 11 | [Calculator](Easy/Calculator.py) | Operator dispatch, division-by-zero handling |
| 12 | [Even Positioned Characters](EvenPositionedCharacter.py) | String indexing with a step |
| 13 | [Multiplication Table](MultiplicationTable.py) | Single-line output with `end` |

### Medium

| # | Problem | Concepts |
|---|---------|----------|
| 1 | [Table Difference](Medium/TableDifference.py) | Combining two sequences |
| 2 | [Square Wall](Medium/SquareWall.py) | Nested loops |
| 3 | [Right Angle Triangle](Medium/RightAngleTriangle.py) | Star pattern |
| 4 | [Right Angle Triangle 2](Medium/RightAngleTriangle2.py) | Number pattern |
| 5 | [Inverted Right Angle Triangle](Medium/InvertedRightAngleTriangle.py) | Decreasing nested loops |
| 6 | [Factorial](Medium/Factorial.py) | Iterative product |
| 7 | [Divisor](Medium/Divisor.py) | Divisibility |
| 8 | [Check Prime](Medium/CheckPrime.py) | Trial division up to √n |
| 9 | [Next Prime Number](Medium/NextPrimeNumber.py) | Prime search |
| 10 | [Fibonacci Number](Medium/FibonacciNumber.py) | Iterative sequence, O(n) time and O(1) space |
| 11 | [GCD](Medium/GCD.py) | Euclidean algorithm |
| 12 | [LCM](Medium/LCM.py) | LCM from GCD |
| 13 | [Pattern 5](Medium/Pattern5.py) | Inverted number pattern |
| 14 | [Pattern 10](Medium/Pattern10.py) | Grow-and-shrink star pattern |

### Hard

| # | Problem | Concepts |
|---|---------|----------|
| 1 | [Rightmost Non-Zero Digit](Hard/RightmostNonZeroDigit.py) | Factoring out 2s and 5s to find the digit without computing the full product |
| 2 | [Diamond Shape](Hard/DiamondShape.py) | Symmetric pattern with spacing |

## Running the Code

Requires Python 3.

```bash
git clone https://github.com/ashishaggrawal/Python-coding.git
cd Python-coding
python DSA/ArraysHashing/TwoSum.py   # runs the built-in examples
python Medium/CheckPrime.py          # reads input from the keyboard
```

DSA solutions run their examples automatically. Fundamentals scripts read input from the keyboard. Expected input and output are documented at the top of every file.

## Author

**Ashish Aggrawal**: [GitHub](https://github.com/ashishaggrawal)
