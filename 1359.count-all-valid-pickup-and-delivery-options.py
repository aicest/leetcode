#
# @lc app=leetcode id=1359 lang=python3
#
# [1359] Count All Valid Pickup and Delivery Options
#

# @lc code=start
class Solution:
    def countOrders(self, n):
        # F1 = 1 * (1) = 1
        # F2 = 1 * (3 + 2 + 1) = 6
        # F3 = 6 * (5 + 4 + 3 + 2 + 1) = 6 * 15 = 90
        # F[i] = F[i-1] * S[i]
        # S[i-1] = (2*(i-1) - 1) + ... + 2 + 1
        # S[i] = (2i - 1) + (2i - 2) + (2i - 3) + ... + 2 + 1
        # S[i] = (2i - 1) + (2i - 2) + (2*(i-1) - 1) + ... + 2 + 1
        # S[i] = (2i - 1) + (2i - 2) + S[i-1] = S[i-1] + 4i - 3
        s = 0
        f = 1  # 0!
        for i in range(1, n + 1):
            s += 4 * i - 3
            f *= s
            f %= 1e9 + 7
        return int(f)


# @lc code=end

if __name__ == "__main__":
    print(Solution().countOrders(1))
    print(Solution().countOrders(2))
    print(Solution().countOrders(3))
    print(Solution().countOrders(18))
