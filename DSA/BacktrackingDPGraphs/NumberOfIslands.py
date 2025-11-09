# Given an m x n grid of "1" (land) and "0" (water), return the number of islands.
# An island is land connected horizontally or vertically.
# Input: grid = [["1","1","0","0","0"],
#                ["1","1","0","0","0"],
#                ["0","0","1","0","0"],
#                ["0","0","0","1","1"]]
# Output: 3

# Approach: scan the grid. Each unvisited "1" starts a new island; flood-fill it (BFS
# here) to mark every connected land cell as visited so it is not counted again.
# BFS is used instead of recursive DFS to avoid hitting the recursion limit on large grids.
# Time: O(m * n)  Space: O(min(m, n)) for the BFS queue

from collections import deque


def num_islands(grid):
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    islands = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != "1":
                continue
            islands += 1
            grid[r][c] = "0"
            queue = deque([(r, c)])
            while queue:
                cr, cc = queue.popleft()
                for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    nr, nc = cr + dr, cc + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
                        grid[nr][nc] = "0"
                        queue.append((nr, nc))
    return islands


if __name__ == "__main__":
    print(num_islands([["1", "1", "1", "1", "0"],
                       ["1", "1", "0", "1", "0"],
                       ["1", "1", "0", "0", "0"],
                       ["0", "0", "0", "0", "0"]]))  # 1
    print(num_islands([["1", "1", "0", "0", "0"],
                       ["1", "1", "0", "0", "0"],
                       ["0", "0", "1", "0", "0"],
                       ["0", "0", "0", "1", "1"]]))  # 3
