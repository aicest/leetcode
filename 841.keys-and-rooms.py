#
# @lc app=leetcode id=841 lang=python3
#
# [841] Keys and Rooms
#

# @lc code=start
class Solution:
    def canVisitAllRooms(self, rooms):
        return len(self.dfs(rooms, 0, [0])) == len(rooms)

    def dfs(self, rooms, i, path):
        for key in rooms[i]:
            if key not in path:
                path = self.dfs(rooms, key, path + [key])
        return path


# @lc code=end

if __name__ == "__main__":
    print(Solution().canVisitAllRooms([[1], [2], [3], []]))
    print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))
