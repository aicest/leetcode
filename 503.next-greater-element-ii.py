#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums):
        if not nums:
            return []
        n = len(nums)
        result = [None] * n
        for i in range(n - 1, -1, -1):
            if nums[i] < nums[i + 1 - n]:
                result[i] = nums[i + 1 - n]
                continue
            for j in range(i + 1 - n, (i + 1 - n) + n - 1):
                best = nums[j] if result[j] == None else max(nums[j], result[j])
                if nums[i] < best:
                    result[i] = best
                    break
            else:
                result[i] = -1
        return result


# @lc code=end

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    assert [2, -1, 2] == Solution().nextGreaterElements([1, 2, 1])
    assert [2, -1, -1, 2, 1, 1] == Solution().nextGreaterElements([1, 2, 2, 1, 0, -1])
    assert [3, 2, 3, 3, -1] == Solution().nextGreaterElements([2, 1, 2, 1, 3])
    end = time.perf_counter()
    print(end - start)
