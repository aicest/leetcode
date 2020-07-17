#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums):
        # DPi = DPi-1 + DPi-1 * Ai
        result = [[]]
        for a in nums:
            for i in range(len(result)):
                path = result[i] + [a]
                if path not in result:
                    result.append(path)
        return result


# @lc code=end

if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
    print(Solution().subsets([1, 2, 3, 3]))
