#
# @lc app=leetcode id=1436 lang=python3
#
# [1436] Destination City
#

# @lc code=start
class Solution:
    def destCity(self, paths):
        s = set()
        d = set()
        for a, b in paths:
            s.add(a)
            d.add(b)
        return list(d - s)[0]


# @lc code=end

if __name__ == "__main__":
    # fmt: off
    print(Solution().destCity([["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]))
    # fmt: on
    print(Solution().destCity([["B", "C"], ["D", "B"], ["C", "A"]]))
    print(Solution().destCity([["A", "Z"]]))
