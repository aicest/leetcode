#
# @lc app=leetcode id=658 lang=python3
#
# [658] Find K Closest Elements
#

# @lc code=start
class Solution:
    def findClosestElements(self, arr, k, x):
        pos = self.bs(arr, x, 0, len(arr) - 1)
        return self.tp(arr, x, pos, k)

    def bs(self, arr, x, start, end):
        if start == end:
            return start
        if start + 1 == end:
            if x - arr[start] <= arr[end] - x:
                return start
            else:
                return end
        pivot = (start + end) // 2
        if arr[pivot] == x:
            return pivot
        if x < arr[pivot]:
            if arr[pivot] - x < x - arr[pivot - 1]:
                return pivot
            return self.bs(arr, x, start, pivot - 1)
        else:
            if x - arr[pivot] <= arr[pivot + 1] - x:
                return pivot
            return self.bs(arr, x, pivot + 1, end)

    def tp(self, arr, x, pos, k):
        result = [arr[pos]]
        k -= 1
        i = pos - 1
        j = pos + 1
        n = len(arr)
        while 0 <= i and j < n and k >= 1:
            if x - arr[i] <= arr[j] - x:
                result.insert(0, arr[i])
                k -= 1
                i -= 1
            else:
                result.append(arr[j])
                k -= 1
                j += 1
        if k >= 1:
            if 0 <= i:
                result = arr[i - k + 1 : i + 1] + result
            else:
                result = result + arr[j : j + k]
        return result


# @lc code=end
