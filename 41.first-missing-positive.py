from typing import *

#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        missing = 1
        ht = {}
        for a in nums:
            ht[a] = True
            while missing in ht:
                missing += 1
        return missing


# @lc code=end

if __name__ == "__main__":
    print(1 == Solution().firstMissingPositive([]))
    print(1 == Solution().firstMissingPositive([-1]))
    print(1 == Solution().firstMissingPositive([0]))
    print(2 == Solution().firstMissingPositive([1]))
    print(4 == Solution().firstMissingPositive([3, 2, 1]))
    print(3 == Solution().firstMissingPositive([1, 2, 0]))
    print(2 == Solution().firstMissingPositive([3, 4, -1, 1]))
    print(1 == Solution().firstMissingPositive([7, 8, 9, 11, 12]))
