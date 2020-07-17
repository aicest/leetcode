#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums):
        result = []
        for i in range(1 << len(nums)):
            path = []
            for j in range(len(nums)):
                if i & 1 << j:
                    path.append(nums[j])
            if path not in result:
                result.append(path)
        return result


# @lc code=end

if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
    print(Solution().subsets([1, 2, 3, 3]))
