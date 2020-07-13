#
# @lc app=leetcode id=997 lang=python3
#
# [997] Find the Town Judge
#

# @lc code=start
class Solution:
    def findJudge(self, N, trust):
        degree = [0] * (N + 1)

        for i, j in trust:
            degree[i] -= 1
            degree[j] += 1

        try:
            return degree.index(N - 1, 1)
        except:
            return -1


# @lc code=end

if __name__ == "__main__":
    print(Solution().findJudge(1, []))
    print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]))
    print(Solution().findJudge(2, [[1, 2]]))
    print(Solution().findJudge(3, [[1, 3], [2, 3]]))
    print(Solution().findJudge(3, [[1, 3], [2, 3], [3, 1]]))
    print(Solution().findJudge(3, [[1, 2], [2, 3]]))
    print(Solution().findJudge(4, [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]))
