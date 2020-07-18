#
# @lc app=leetcode id=368 lang=python3
#
# [368] Largest Divisible Subset
#

# @lc code=start
class Solution:
    def largestDivisibleSubset(self, nums):
        nums = sorted(nums)
        best = []
        dp = {}
        for a in nums:
            if a not in dp:
                dp[a] = []
            for b in reversed(dp):
                subset = dp[b]
                if (a % b == 0 or b % a == 0) and (len(dp[a]) < len(subset) + 1):
                    dp[a] = subset + [a]
                    if len(dp[a]) > len(best):
                        best = dp[a]
                        break
        return best


# @lc code=end

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print([], Solution().largestDivisibleSubset([]))
    print([1], Solution().largestDivisibleSubset([1]))
    print([1, 2], Solution().largestDivisibleSubset([1, 2, 3]))
    print([1, 2, 6], Solution().largestDivisibleSubset([1, 2, 3, 6]))
    print([1, 2, 10, 20], Solution().largestDivisibleSubset([1, 2, 3, 5, 6, 10, 20]))
    print([1, 2, 4, 8], Solution().largestDivisibleSubset([1, 2, 4, 8]))
    print([4, 8, 16], Solution().largestDivisibleSubset([3, 4, 16, 8]))
    print([2, 4, 8], Solution().largestDivisibleSubset([2, 3, 4, 8]))
    # fmt: off
    print([9, 18, 90, 180, 360, 720], Solution().largestDivisibleSubset([5, 9, 18, 54, 108, 540, 90, 180, 360, 720]))
    print(Solution().largestDivisibleSubset([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912, 1073741824]))
    # fmt: on
    end = time.perf_counter()
    print(end - start)
