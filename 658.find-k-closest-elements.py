#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr, k, x):
        pos = self.bs(arr, x, k, 0, len(arr) - k)
        return arr[pos : pos + k]

    def bs(self, arr, x, k, start, end):
        if start == end:
            return start
        pivot = (start + end) // 2
        a = arr[pivot]
        b = arr[pivot + k]
        if a == x and x == b:
            return pivot
        if x - a <= b - x:
            return self.bs(arr, x, k, start, pivot)
        else:
            return self.bs(arr, x, k, pivot + 1, end)


# @lc code=end


if __name__ == "__main__":
    print(Solution().findClosestElements([2, 2, 6, 6], 2, 4))
    print(Solution().findClosestElements([1, 2, 5], 1, 3))
    print(Solution().findClosestElements([1, 2, 5], 1, 4))
    print(Solution().findClosestElements([1, 2, 5, 7, 7, 7, 7], 1, 4))
