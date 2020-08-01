#
# @lc app=leetcode id=853 lang=python3
#
# [853] Car Fleet
#

# @lc code=start
class Solution:
    def carFleet(self, target, positionList, speedList):
        carList = sorted(zip(positionList, speedList), key=lambda c: c[1])
        count = 0
        n = len(carList)
        while n != 0:
            count += 1
            n -= 1
            p0, s0 = carList.pop(0)
            t0 = (target - p0) / s0
            i = 0
            while i < n:
                p1, s1 = c1 = carList[i]
                t1 = (p0 - p1) / (s1 - s0) if p0 >= p1 and s1 > s0 else float("inf")
                if t1 <= t0:
                    carList.remove(c1)
                    n -= 1
                else:
                    i += 1
        return count


# @lc code=end

if __name__ == "__main__":
    print(2 == Solution().carFleet(7, [1, 2, 3], [3, 2, 2]))
    print(2 == Solution().carFleet(7, [2, 1, 3], [2, 3, 2]))
    print(2 == Solution().carFleet(7, [3, 1, 2], [2, 3, 2]))
    print(2 == Solution().carFleet(7, [3, 2, 1], [2, 2, 3]))
    print(3 == Solution().carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
    print(1 == Solution().carFleet(12, [5, 3, 4, 2], [1, 3, 2, 5]))
