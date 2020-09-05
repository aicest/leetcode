#
# @lc app=leetcode id=191 lang=python3
#
# [191] Number of 1 Bits
#

# @lc code=start
class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count


# @lc code=end

if __name__ == "__main__":
    print(3 == Solution().hammingWeight(0b00000000000000000000000000001011))
    print(0 == Solution().hammingWeight(0b00000000000000000000000000000000))
    print(1 == Solution().hammingWeight(0b00000000000000000000000010000000))
    print(31 == Solution().hammingWeight(0b11111111111111111111111111111101))
