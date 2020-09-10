#
# @lc app=leetcode id=96 lang=python3
#
# [96] Unique Binary Search Trees
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        # F[n] = sum{F[i] * F[n-1-i]}
        dp = [1]  # 0! = 1
        for i in range(1, n + 1):
            acc = 0
            for j in range(i):
                acc += dp[j] * dp[i - 1 - j]
            dp.append(acc)
        return dp[-1]


# @lc code=end

if __name__ == "__main__":
    print(1 == Solution().numTrees(1))
    print(2 == Solution().numTrees(2))
    print(5 == Solution().numTrees(3))
    print(14 == Solution().numTrees(4))
    print(42 == Solution().numTrees(5))
    print(1767263190 == Solution().numTrees(19))
