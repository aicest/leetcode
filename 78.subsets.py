#
# @lc app=leetcode id=78 lang=python3
#
# [78] Subsets
#

# @lc code=start
class Solution:
    def subsets(self, nums):
        return self.dfs(nums, 0, len(nums) - 1, [], {})

    def dfs(self, nums, start, end, path, dp):
        result = [path]
        for i in range(start, end + 1):
            curr = path + [nums[i]]
            if (i + 1, end) not in dp:
                dp[(i + 1, end)] = self.dfs(nums, i + 1, end, [], dp)
            for cp in dp[(i + 1, end)]:
                cp = curr + cp
                if cp not in result:
                    result.append(cp)
        return result


# @lc code=end

if __name__ == "__main__":
    print(Solution().subsets([1, 2, 3]))
    print(Solution().subsets([1, 2, 3, 3]))
