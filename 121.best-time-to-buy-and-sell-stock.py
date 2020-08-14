from typing import *

#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best, low = 0, float("inf")
        for p in prices:
            best = max(best, p - low)
            low = min(low, p)
        return best


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().maxProfit([]))
    print(0 == Solution().maxProfit([1]))
    print(1 == Solution().maxProfit([1, 2]))
    print(5 == Solution().maxProfit([7, 1, 5, 3, 6, 4]))
    print(0 == Solution().maxProfit([7, 6, 4, 3, 1]))
