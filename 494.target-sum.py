from typing import *

#
# @lc app=leetcode id=494 lang=python3
#
# [494] Target Sum
#

# @lc code=start
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        # 优化：使用 dict 极大减少遍历次数
        # F[n] = {F[n-1][i]+A[j], F[n-1][i]-A[j]}
        dp = {0: 1}
        for b in nums:
            obj = {}
            for a, c in dp.items():
                if a + b not in obj:
                    obj[a + b] = c
                else:
                    obj[a + b] += c
                if a - b not in obj:
                    obj[a - b] = c
                else:
                    obj[a - b] += c
            dp = obj
        return dp[S] if S in dp else 0


# @lc code=end

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(2 == Solution().findTargetSumWays([0], 0))
    print(0 == Solution().findTargetSumWays([1], 0))
    print(5 == Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
    # fmt: off
    print(2760 == Solution().findTargetSumWays([2, 3, 2, 1, 6, 2, 5, 2, 1, 5, 2, 6, 7, 4, 3, 1], 10))
    print(6606 == Solution().findTargetSumWays([10, 9, 6, 4, 19, 0, 41, 30, 27, 15, 14, 39, 33, 7, 34, 17, 24, 46, 2, 46], 45))
    print(6008 == Solution().findTargetSumWays([1, 1, 31, 18, 39, 33, 33, 15, 36, 50, 8, 47, 21, 29, 24, 39, 23, 44, 22, 33], 11))
    # fmt: on
    end = time.perf_counter()
    print(end - start)
