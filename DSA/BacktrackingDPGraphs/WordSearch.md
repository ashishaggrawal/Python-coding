# Word Search

Given an m x n grid of characters and a word, return True if the word can be formed from letters of horizontally or vertically adjacent cells. A cell may be used only once.

```
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: True
Input: same board, word = "ABCB"
Output: False
```

## Explanation

DFS from every cell. Mark a cell as visited in place by overwriting it with "#", explore its four neighbours, then restore the letter when backtracking. This avoids a separate visited set. Space: O(L) recursion depth

## Complexity

- Time: O(m * n * 3^L) (L = word length; each step has at most 3 new directions)

## Output

Running `python WordSearch.py` executes these examples:

```python
board = [["A", "B", "C", "E"],
         ["S", "F", "C", "S"],
         ["A", "D", "E", "E"]]
print(exist(board, "ABCCED"))  # True
print(exist(board, "SEE"))     # True
print(exist(board, "ABCB"))    # False
```

Output:

```
True
True
False
```
