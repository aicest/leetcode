from typing import *

#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        arr = []
        rowMin, rowMax = 0, len(matrix)
        colMin, colMax = 0, len(matrix[0]) if matrix else 0
        i, j = 0, 0
        while True:
            if j >= colMax:
                break
            while j < colMax:
                arr.append(matrix[i][j])
                j += 1
            rowMin += 1
            i, j = i + 1, j - 1
            if i >= rowMax:
                break
            while i < rowMax:
                arr.append(matrix[i][j])
                i += 1
            colMax -= 1
            i, j = i - 1, j - 1
            if j < colMin:
                break
            while j >= colMin:
                arr.append(matrix[i][j])
                j -= 1
            rowMax -= 1
            i, j = i - 1, j + 1
            if i < rowMin:
                break
            while i >= rowMin:
                arr.append(matrix[i][j])
                i -= 1
            colMin += 1
            i, j = i + 1, j + 1
        return arr


# @lc code=end

if __name__ == "__main__":
    print([] == Solution().spiralOrder([]))
    print([] == Solution().spiralOrder([[]]))
    print([1] == Solution().spiralOrder([[1]]))
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print([1, 2, 3, 6, 9, 8, 7, 4, 5] == Solution().spiralOrder(matrix))
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print([1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7] == Solution().spiralOrder(matrix))
