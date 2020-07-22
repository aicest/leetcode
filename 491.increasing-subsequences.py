#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums):
        return self.dfs(nums, 0, len(nums) - 1, [])

    def dfs(self, nums, start, end, path, root=None, result=None, found=None):
        result = [] if result == None else result
        found = {} if found == None else found
        if len(path) >= 2 and tuple(path) not in found:
            result.append(path)
            found[tuple(path)] = True
        for i in range(start, end + 1):
            if root == None or root <= nums[i]:
                self.dfs(nums, i + 1, end, path + [nums[i]], nums[i], result, found)
        return result


# @lc code=end

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(Solution().findSubsequences([4, 3, 2, 1, 0, 1, 2, 3, 4]))
    print(Solution().findSubsequences([4, 3, 2, 1]))
    print(Solution().findSubsequences([4, 6, 7, 7]))
    Solution().findSubsequences([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
    end = time.perf_counter()
    print(end - start)
