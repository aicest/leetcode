from typing import *

#
# @lc app=leetcode id=338 lang=python3
#
# [338] Counting Bits
#

# @lc code=start
class Solution:
    def countBits(self, num: int) -> List[int]:
        # F[n] = 1 + F[n-2^x]
        dp = [0]
        exp = 1
        for i in range(1, num + 1):
            if i == exp:
                exp <<= 1
                dp.append(1)
            else:
                dp.append(1 + dp[i - exp])
        return dp


# @lc code=end

if __name__ == "__main__":
    print([0] == Solution().countBits(0))
    print([0, 1] == Solution().countBits(1))
    print([0, 1, 1] == Solution().countBits(2))
    print([0, 1, 1, 2, 1, 2] == Solution().countBits(5))
    print([0, 1, 1, 2, 1, 2, 2] == Solution().countBits(6))
    print([0, 1, 1, 2, 1, 2, 2, 3] == Solution().countBits(7))
    print([0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4] == Solution().countBits(15))
