#
# @lc app=leetcode id=300 lang=python3
#
# [300] Longest Increasing Subsequence
#

# @lc code=start
class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0

        dp = {1: nums[0]}
        best = 1
        for i in range(1, len(nums)):
            x = nums[i]
            dp[1] = min(dp[1], x)
            for n in range(best, 0, -1):
                if dp[n] < x:
                    if n + 1 not in dp:
                        dp[n + 1] = x
                        best = n + 1
                        break
                    else:
                        dp[n + 1] = min(dp[n + 1], x)
                        break
        return best


# @lc code=end

if __name__ == "__main__":
    print(Solution().lengthOfLIS([]))
    print(Solution().lengthOfLIS([10]))
    print(Solution().lengthOfLIS([10, 10, 10]))
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().lengthOfLIS(range(2500)))  # 回溯法 => 超时
    print(Solution().lengthOfLIS([1, 9, 10, 6, 7, 8, 2, 3, 4, 5]))
    print(Solution().lengthOfLIS([10, 11, 9, 10, 6, 7, 8]))
