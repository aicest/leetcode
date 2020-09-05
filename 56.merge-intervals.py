from typing import *

#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort(key=lambda pair: pair[0])
        for start, end in intervals:
            if result and result[-1][1] >= start:
                result[-1][1] = max(result[-1][1], end)
            else:
                result.append([start, end])
        return result


# @lc code=end

if __name__ == "__main__":
    result = Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    print([[1, 6], [8, 10], [15, 18]] == result)
    result = Solution().merge([[1, 4], [4, 5]])
    print([[1, 5]] == result)
    result = Solution().merge([[1, 4], [0, 5]])
    print([[0, 5]] == result)
    result = Solution().merge([[1, 4], [0, 0]])
    print([[0, 0], [1, 4]] == result)
