#
# @lc app=leetcode id=491 lang=python3
#
# [491] Increasing Subsequences
#

# @lc code=start
class Solution:
    def findSubsequences(self, nums):
        result = []
        found = {}
        n = len(nums)
        for i in range(1 << n):
            path = []
            for j in range(n):
                if i & 1 << j:
                    prev = path[-1] if path else None
                    if prev == None or prev <= nums[j]:
                        path.append(nums[j])
                    else:
                        break
            if len(path) >= 2 and tuple(path) not in found:
                result.append(path)
                found[tuple(path)] = True
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
