#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
class Solution:
    def maxWidthRamp(self, A):
        best = 0
        arr = [(0, A[0])]
        for i in range(1, len(A)):
            a = A[i]
            if arr[-1][1] > a:
                arr.append((i, a))
            else:
                j, b = self.bs(arr, 0, len(arr), a)
                best = max(best, i - j)
        return best

    def bs(self, arr, start, end, target):
        if start == end:
            return arr[start]
        pivot = (start + end) // 2
        if target == arr[pivot][1]:
            return arr[pivot]
        elif target < arr[pivot][1]:
            return self.bs(arr, pivot + 1, end, target)
        else:
            return self.bs(arr, start, pivot, target)


# @lc code=end

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(4, Solution().maxWidthRamp([6, 0, 8, 2, 1, 5]))
    print(7, Solution().maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))
    print(3, Solution().maxWidthRamp([3, 0, 2, 2, 1]))
    print(1, Solution().maxWidthRamp(list(range(50000, 1, -1)) + [2]))
    print(49998, Solution().maxWidthRamp(list(range(1, 50000))))
    end = time.perf_counter()
    print(end - start)
