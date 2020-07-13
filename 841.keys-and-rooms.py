#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms):
        path = [False] * len(rooms)
        keys = [0]
        while keys:
            key = keys.pop()
            if not path[key]:
                path[key] = True
                keys.extend(rooms[key])
        return all(path)


# @lc code=end

if __name__ == "__main__":
    print(Solution().canVisitAllRooms([[1], [2], [3], []]))
    print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
