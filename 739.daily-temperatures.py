from typing import *

#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#

# @lc code=start
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        n = len(T)
        result = [0] * n
        stack = []
        for i in range(n):
            while stack and T[stack[-1]] < T[i]:
                j = stack.pop()
                result[j] = i - j
            else:
                stack.append(i)
        return result


# @lc code=end

if __name__ == "__main__":
    print([0, 0] == Solution().dailyTemperatures([73, 73]))
    print(
        [1, 1, 4, 2, 1, 1, 0, 0]
        == Solution().dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])
    )
