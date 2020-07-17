#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nums = self.merge(nums1, nums2)
        n = len(nums)
        if n % 2 == 1:
            return nums[n // 2]
        else:
            return (nums[n // 2 - 1] + nums[n // 2]) / 2

    def merge(self, nums1, nums2):
        i = j = 0
        m = len(nums1)
        n = len(nums2)
        result = []
        while i < m and j < n:
            a = nums1[i]
            b = nums2[j]
            if a <= b:
                result.append(a)
                i += 1
            else:
                result.append(b)
                j += 1
        result.extend(nums1[i:])
        result.extend(nums2[j:])
        return result


# @lc code=end

if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([1, 3], [2]))
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
