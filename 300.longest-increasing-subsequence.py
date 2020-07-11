#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums):
        return self.dfs(nums, 0, len(nums) - 1, [])

    def dfs(self, nums, start, end, path, root=None):
        best = len(path)
        for i in range(start, end + 1):
            child = nums[i]
            if root == None or root < child:
                best = max(best, self.dfs(nums, i + 1, end, path + [child], child))
        return best


# @lc code=end

if __name__ == "__main__":
    print(Solution().lengthOfLIS([]))
    print(Solution().lengthOfLIS([10]))
    print(Solution().lengthOfLIS([10, 10, 10]))
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().lengthOfLIS(range(23)))  # 回溯法 => 超时
