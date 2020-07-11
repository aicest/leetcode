#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0

        while i < m and j < n:
            a = nums1[i]
            b = nums2[j]

            if a <= b:
                i += 1
            else:
                nums1.insert(i, b)
                nums1.pop()
                j += 1
                i += 1
                m += 1

        if j < n:
            nums1[i:] = nums2[j:]


# @lc code=end
