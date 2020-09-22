#
# @lc app=leetcode id=165 lang=python3
#
# [165] Compare Version Numbers
#

# @lc code=start
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        l1, l2 = len(v1), len(v2)
        if l1 < l2:
            v1.extend([0] * (l2 - l1))
        elif l1 > l2:
            v2.extend([0] * (l1 - l2))
        for i in range(max(l1, l2)):
            if v1[i] < v2[i]:
                return -1
            if v1[i] > v2[i]:
                return 1
        return 0


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().compareVersion("1.01", "1.001"))
    print(0 == Solution().compareVersion("1.0", "1.0.0"))
    print(-1 == Solution().compareVersion("0.1", "1.1"))
    print(1 == Solution().compareVersion("1.0.1", "1"))
    print(-1 == Solution().compareVersion("7.5.2.4", "7.5.3"))
