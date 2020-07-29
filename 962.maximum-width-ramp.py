#
# @lc app=leetcode id=962 lang=python3
#
# [962] Maximum Width Ramp
#

# @lc code=start
class Solution:
    def maxWidthRamp(self, A):
        best = 0
        stack = [(0, A[0])]
        for i in range(1, len(A)):
            a = A[i]
            if stack[-1][1] > a:
                stack.append((i, a))
        for j in range(len(A) - 1, -1, -1):
            b = A[j]
            while stack:
                if stack[-1][1] <= b:
                    i, a = stack.pop()
                    best = max(best, j - i)
                else:
                    break
            else:
                break
        return best


# @lc code=end

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(4, Solution().maxWidthRamp([6, 0, 8, 2, 1, 5]))
    print(7, Solution().maxWidthRamp([9, 8, 1, 0, 1, 9, 4, 0, 4, 1]))
    print(3, Solution().maxWidthRamp([3, 0, 2, 2, 1]))
    print(5, Solution().maxWidthRamp([3, 2, 0, 2, 2, 4, 1]))
    print(1, Solution().maxWidthRamp(list(range(50000, 1, -1)) + [2]))
    print(49998, Solution().maxWidthRamp(list(range(1, 50000))))
    end = time.perf_counter()
    print(end - start)
