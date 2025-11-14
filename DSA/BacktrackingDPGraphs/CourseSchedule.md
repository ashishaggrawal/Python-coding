# Course Schedule

There are numCourses courses labelled 0 to numCourses - 1. prerequisites[i] = [a, b] means course b must be taken before course a. Return True if all courses can be finished.

```
Input: numCourses = 2, prerequisites = [[1, 0]]
Output: True
Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
Output: False   (the two courses depend on each other)
```

## Explanation

**Approach 1 (Kahn's algorithm):** repeatedly take courses that have no remaining prerequisites. If every course gets taken, there is no cycle.

**Approach 2 (DFS):** colour nodes unvisited / visiting / done. Reaching a "visiting" node again means the graph has a cycle.

## Complexity

- **Time:** O(V + E)
- **Space:** O(V + E)

## Output

Running `python CourseSchedule.py` executes these examples:

```python
print(can_finish(2, [[1, 0]]))                          # True
print(can_finish(2, [[1, 0], [0, 1]]))                  # False
print(can_finish_dfs(4, [[1, 0], [2, 1], [3, 2]]))      # True
print(can_finish_dfs(3, [[1, 0], [2, 1], [0, 2]]))      # False
```

Output:

```
True
False
True
False
```
