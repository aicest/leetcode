#
# @lc app=leetcode id=532 lang=python3
#
# [532] K-diff Pairs in an Array
#

# @lc code=start
class Solution:
    def findPairs(self, nums, k):
        if k < 0:
            return 0
        count = 0
        ht = {}
        found = {}
        for a in nums:
            b0 = a - k
            b1 = a + k
            if b0 in ht and (a, b0) not in found:
                count += 1
                found[(a, b0)] = found[(b0, a)] = True
            if b1 in ht and (a, b1) not in found:
                count += 1
                found[(a, b1)] = found[(b1, a)] = True
            ht[a] = True
        return count


# @lc code=end
if __name__ == "__main__":
    print(2 == Solution().findPairs([3, 1, 4, 1, 5], 2))
    print(4 == Solution().findPairs([1, 2, 3, 4, 5], 1))
    print(1 == Solution().findPairs([1, 3, 1, 5, 4], 0))
    print(0 == Solution().findPairs([1, 2, 3, 4, 5], -1))
