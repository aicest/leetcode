from typing import *

#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree, outdegree = {}, {}
        zero = set(range(numCourses))
        for start, end in prerequisites:
            if start in outdegree:
                outdegree[start].append(end)
            else:
                outdegree[start] = [end]
            if end in indegree:
                indegree[end] = indegree[end] + 1
            else:
                indegree[end] = 1
                zero.remove(end)
        visited = [False] * numCourses
        while zero:
            start = zero.pop()
            visited[start] = True
            if start in outdegree:
                for end in outdegree[start]:
                    indegree[end] -= 1
                    if indegree[end] == 0:
                        zero.add(end)
        return all(visited)

    def v1(self, numCourses, prerequisites):
        ht = {}
        for start, end in prerequisites:
            if start not in ht:
                ht[start] = []
            ht[start].append(end)
        visited, pending = {}, {}
        for i in range(numCourses):
            if not self.dfs(i, ht, visited, pending):
                return False
        return True

    def dfs(self, n, dep, visited, pending):
        if n in visited and visited[n]:
            return True
        if n in pending and pending[n]:
            return False
        if n in dep:
            pending[n] = True
            for pre in dep[n]:
                if not self.dfs(pre, dep, visited, pending):
                    return False
            pending[n] = False
        visited[n] = True
        return True


# @lc code=end

if __name__ == "__main__":
    print(True == Solution().canFinish(2, [[1, 0]]))
    print(True == Solution().canFinish(4, [[3, 0], [0, 1]]))
    print(True == Solution().canFinish(5, [[1, 0], [0, 2], [3, 2], [2, 4]]))
    print(False == Solution().canFinish(5, [[1, 0], [0, 2], [3, 2], [2, 4], [2, 1]]))
    print(False == Solution().canFinish(5, [[1, 0], [0, 2], [3, 2], [2, 4], [0, 1]]))
    print(False == Solution().canFinish(5, [[1, 0], [0, 1], [3, 2], [2, 3]]))
    print(False == Solution().canFinish(5, [[1, 0], [3, 2], [2, 3]]))
    print(False == Solution().canFinish(2, [[1, 0], [0, 1]]))
