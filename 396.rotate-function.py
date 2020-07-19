#
# @lc app=leetcode id=396 lang=python3
#
# [396] Rotate Function
#

# @lc code=start
class Solution:
    def maxRotateFunction(self, A):
        # F0 = 0*A0 + 1*A1 + 2*A2 + 3*A3
        # F1 = 0*A3 + 1*A0 + 2*A1 + 3*A2
        # F1 - F0 = sum(A) - 4*A3
        # F[i] = F[i-1] + sum(A) - n*A[n-i]
        acc = sum(A)
        curr = sum(i * a for i, a in enumerate(A))
        result = curr
        for i in range(1, n := len(A)):
            curr += acc - n * A[n - i]
            result = max(result, curr)
        return result


# @lc code=end

if __name__ == "__main__":
    print(Solution().maxRotateFunction([]))
    print(Solution().maxRotateFunction([4, 3, 2]))
    print(Solution().maxRotateFunction([4, 3, 2, 6]))
