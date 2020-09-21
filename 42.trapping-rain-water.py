from typing import *

#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        stack = []
        low = float("inf")
        for i in range(len(height)):
            while stack and height[stack[-1]] <= height[i]:
                j = stack.pop()
                result += (i - j) * min(0, 1)
            else:
                stack.append(i)
        return result


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().trap([0, 1, 2]))
    print(0 == Solution().trap([2, 1, 0]))
    print(0 == Solution().trap([0, 1, 0]))
    print(1 == Solution().trap([1, 0, 1]))
    print(6 == Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(16 == Solution().trap([5, 4, 3, 1, 2, 3, 2, 4, 5]))
    print(16 == Solution().trap([5, 4, 3, 2, 1, 3, 2, 4, 5]))
    print(9 == Solution().trap([1, 4, 3, 2, 1, 3, 2, 4, 5]))
    print(9 == Solution().trap([1, 4, 3, 2, 1, 3, 2, 4, 1]))
    print(8 == Solution().trap([1, 4, 3, 2, 2, 3, 2, 4, 1]))
