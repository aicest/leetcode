#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, A, B):
        # https://zh.wikipedia.org/zh-cn/%E4%B8%AD%E4%BD%8D%E6%95%B8
        # 中位数（又称中值，英语：Median），统计学中的专业名词，代表一个样本、种群或概率分布中的一个数值，其可将数值集合划分为数量相等的上下两部分。
        # 对于有限的数集，可以通过把所有观察值高低排序后找出正中间的一个作为中位数。
        # 如果观察值有偶数个，则中位数不唯一，通常取最中间的两个数值的平均数作为中位数。
        m = len(A)
        n = len(B)
        if m > n:
            A, B = B, A
            m, n = n, m
        return self.bs(A, B, m, n, 0, m, (m + n) % 2 == 1)

    def bs(self, A, B, m, n, start, end, odd):
        # i + j == (m-i) + (n-j) => j = (m-i+n-i) / 2 = (m+n) / 2 - i
        i = (start + end) // 2
        j = (m + n) // 2 - i
        if (i == 0 or j == n or A[i - 1] <= B[j]) and (
            j == 0 or i == m or B[j - 1] <= A[i]
        ):
            leftMax = max(
                float("-inf") if i == 0 else A[i - 1],
                float("-inf") if j == 0 else B[j - 1],
            )
            rightMin = min(
                float("inf") if i == m else A[i], float("inf") if j == n else B[j]
            )
            if odd:
                return rightMin
            else:
                return (leftMax + rightMin) / 2
        elif i == 0 or j == n or A[i - 1] <= B[j]:
            return self.bs(A, B, m, n, i + 1, end, odd)
        else:
            return self.bs(A, B, m, n, start, i, odd)


# @lc code=end

if __name__ == "__main__":
    print(Solution().findMedianSortedArrays([], [1]))
    print(Solution().findMedianSortedArrays([], [1, 2]))
    print(Solution().findMedianSortedArrays([], [1, 2, 3]))
    print(Solution().findMedianSortedArrays([], [1, 2, 3, 4]))
    print(Solution().findMedianSortedArrays([1], [1]))
    print(Solution().findMedianSortedArrays([1], [2]))
    print(Solution().findMedianSortedArrays([2], [1]))
    print(Solution().findMedianSortedArrays([2], [1, 3]))
    print(Solution().findMedianSortedArrays([1, 2], [3, 4]))
    print(Solution().findMedianSortedArrays([1, 2, 5, 6], [3, 4]))
    print(Solution().findMedianSortedArrays([1, 2, 4, 6, 7], [3, 5]))
