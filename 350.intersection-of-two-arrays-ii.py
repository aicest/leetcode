from typing import *

#
# @lc app=leetcode id=350 lang=python3
#
# [350] Intersection of Two Arrays II
#

# @lc code=start
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        ht = {}
        for x in nums2:
            if x in ht:
                ht[x] += 1
            else:
                ht[x] = 1
        for x in nums1:
            if x in ht and ht[x]:
                ht[x] -= 1
                result.append(x)
        return result


# @lc code=end

if __name__ == "__main__":
    print([] == Solution().intersect([], []))
    print([] == Solution().intersect([1, 1], []))
    print([] == Solution().intersect([1, 1], [2, 2]))
    print([1] == Solution().intersect([1], [1]))
    print([2, 2] == Solution().intersect([1, 2, 2, 1], [2, 2]))
    print([1, 2, 2] == Solution().intersect([1, 2, 2, 3], [2, 2, 1]))
    print([4, 9] == Solution().intersect([4, 9, 5], [9, 4, 9, 8, 4]))
