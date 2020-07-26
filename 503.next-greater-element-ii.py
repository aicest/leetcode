#
# @lc app=leetcode id=503 lang=python3
#
# [503] Next Greater Element II
#

# @lc code=start
class Solution:
    def nextGreaterElements(self, nums):
        # https://www.cnblogs.com/ilovezyg/p/6477503.html
        n = len(nums)
        result = [-1] * n
        stack = []
        for i in range(n * 2):
            i = i % n
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]
            stack.append(i)
        return result


# @lc code=end

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print([-1, 4, 4, 4] == Solution().nextGreaterElements([4, 3, 2, 1]))
    print([2, 3, 4, -1] == Solution().nextGreaterElements([1, 2, 3, 4]))
    print([2, -1, 2, -1] == Solution().nextGreaterElements([1, 2, 1, 2]))
    print([-1, 2, -1, 2] == Solution().nextGreaterElements([2, 1, 2, 1]))
    print([2, 3, 3, -1] == Solution().nextGreaterElements([1, 2, 1, 3]))
    print([3, -1, 2, 3] == Solution().nextGreaterElements([1, 3, 1, 2]))
    print([3, 3, -1, 2] == Solution().nextGreaterElements([2, 1, 3, 1]))
    print([-1, 2, 3, 3] == Solution().nextGreaterElements([3, 1, 2, 1]))
    end = time.perf_counter()
    print(end - start)
