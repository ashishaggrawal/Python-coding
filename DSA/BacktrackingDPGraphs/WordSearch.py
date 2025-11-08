# Given an m x n grid of characters and a word, return True if the word can be formed
# from letters of horizontally or vertically adjacent cells. A cell may be used only once.
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: True
# Input: same board, word = "ABCB"
# Output: False

# Approach: DFS from every cell. Mark a cell as visited in place by overwriting it with
# "#", explore its four neighbours, then restore the letter when backtracking. This
# avoids a separate visited set.
# Time: O(m * n * 3^L) (L = word length; each step has at most 3 new directions)
# Space: O(L) recursion depth


def exist(board, word):
    rows, cols = len(board), len(board[0])

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False

        board[r][c] = "#"
        found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                 dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
        board[r][c] = word[i]
        return found

    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))


if __name__ == "__main__":
    board = [["A", "B", "C", "E"],
             ["S", "F", "C", "S"],
             ["A", "D", "E", "E"]]
    print(exist(board, "ABCCED"))  # True
    print(exist(board, "SEE"))     # True
    print(exist(board, "ABCB"))    # False
