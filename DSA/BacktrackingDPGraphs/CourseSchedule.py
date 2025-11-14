# There are numCourses courses labelled 0 to numCourses - 1. prerequisites[i] = [a, b]
# means course b must be taken before course a. Return True if all courses can be finished.
# Input: numCourses = 2, prerequisites = [[1, 0]]
# Output: True
# Input: numCourses = 2, prerequisites = [[1, 0], [0, 1]]
# Output: False   (the two courses depend on each other)

# Approach 1 (Kahn's algorithm): repeatedly take courses that have no remaining
# prerequisites. If every course gets taken, there is no cycle.
# Approach 2 (DFS): colour nodes unvisited / visiting / done. Reaching a "visiting" node
# again means the graph has a cycle.
# Time: O(V + E)  Space: O(V + E)

from collections import deque


def can_finish(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1

    queue = deque(c for c in range(num_courses) if indegree[c] == 0)
    taken = 0
    while queue:
        c = queue.popleft()
        taken += 1
        for nxt in graph[c]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return taken == num_courses


def can_finish_dfs(num_courses, prerequisites):
    graph = [[] for _ in range(num_courses)]
    for course, prereq in prerequisites:
        graph[prereq].append(course)

    UNVISITED, VISITING, DONE = 0, 1, 2
    state = [UNVISITED] * num_courses

    def has_cycle(c):
        if state[c] == VISITING:
            return True
        if state[c] == DONE:
            return False
        state[c] = VISITING
        if any(has_cycle(nxt) for nxt in graph[c]):
            return True
        state[c] = DONE
        return False

    return not any(has_cycle(c) for c in range(num_courses))


if __name__ == "__main__":
    print(can_finish(2, [[1, 0]]))                          # True
    print(can_finish(2, [[1, 0], [0, 1]]))                  # False
    print(can_finish_dfs(4, [[1, 0], [2, 1], [3, 2]]))      # True
    print(can_finish_dfs(3, [[1, 0], [2, 1], [0, 2]]))      # False
