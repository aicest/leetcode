#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target, P, S):
        # 核心：位置靠后的车辆，赶上前车后则同速行进，速度再怎么快也不会越过前车直奔终点
        count = 0
        leadingCarTime = float("-inf")
        for p, s in sorted(zip(P, S), key=lambda c: c[0], reverse=True):
            t = (target - p) / s
            if t > leadingCarTime:
                count += 1
                leadingCarTime = t
        return count


# @lc code=end

if __name__ == "__main__":
    print(2 == Solution().carFleet(7, [1, 2, 3], [3, 2, 2]))
    print(2 == Solution().carFleet(7, [2, 1, 3], [2, 3, 2]))
    print(2 == Solution().carFleet(7, [3, 1, 2], [2, 3, 2]))
    print(2 == Solution().carFleet(7, [3, 2, 1], [2, 2, 3]))
    print(3 == Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print(1 == Solution().carFleet(12, [5, 3, 4, 2], [1, 3, 2, 5]))
