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

        dp = [nums[0]]
        for i in range(1, len(nums)):
            x = nums[i]
            dp[0] = min(dp[0], x)
            n = self.bs(dp, x, 0, len(dp) - 1)
            if dp[n] < x:
                dp.append(x)
            else:
                dp[n] = x
        return len(dp)

    def bs(self, arr, x, start, end):
        if start == end:
            return start
        pivot = (start + end) // 2
        if arr[pivot] == x:
            return pivot
        if x < arr[pivot]:
            return self.bs(arr, x, start, pivot)
        else:
            return self.bs(arr, x, pivot + 1, end)


# @lc code=end

if __name__ == "__main__":
    print(Solution().lengthOfLIS([]))
    print(Solution().lengthOfLIS([10]))
    print(Solution().lengthOfLIS([10, 10, 10]))
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
    print(Solution().lengthOfLIS(range(2500)))  # 回溯法 => 超时
    print(Solution().lengthOfLIS([1, 9, 10, 6, 7, 8, 2, 3, 4, 5]))
    print(Solution().lengthOfLIS([10, 11, 9, 10, 6, 7, 8]))
