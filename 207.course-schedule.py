from typing import *

#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#

# @lc code=start
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        ht = {}
        for a, b in prerequisites:
            if a not in ht:
                ht[a] = []
            ht[a].append(b)
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
