#
# @lc app=leetcode id=1434 lang=python3
#
# [1434] Number of Ways to Wear Different Hats to Each Other
#

# @lc code=start
class Solution:
    def numberWays(self, hats):
        return self.dfs(hats, 0, [], len(hats), 0)

    def dfs(self, arr, i, path, n, result):
        for j in range(len(arr[i])):
            if arr[i][j] not in path:
                curr = path + [arr[i][j]]
                if i + 1 == n:
                    result += 1
                else:
                    result = self.dfs(arr, i + 1, curr, n, result)
        return result


# @lc code=end

if __name__ == "__main__":
    print(Solution().numberWays([[3, 4], [4, 5], [5]]))
    print(Solution().numberWays([[3, 5, 1], [3, 5]]))
    # fmt: off
    print(Solution().numberWays([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]]))
    print(Solution().numberWays([[1, 2, 3], [2, 3, 5, 6], [1, 3, 7, 9], [1, 8, 9], [2, 5, 7]]))
    # fmt: on
