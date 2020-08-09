#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.used = 0
        self.queue = []
        self.map = {}

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.queue.remove(key)
        self.queue.insert(0, key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.queue.remove(key)
            self.used -= 1
        if self.used == self.capacity:
            least = self.queue.pop()
            self.map.pop(least)
        else:
            self.used += 1
        self.queue.insert(0, key)
        self.map[key] = value


# @lc code=end

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache.get(1) == 1)
    cache.put(3, 3)
    print(cache.get(2) == -1)
    cache.put(4, 4)
    print(cache.get(1) == -1)
    print(cache.get(3) == 3)
    print(cache.get(4) == 4)
    cache.put(3, 3)
    cache.put(2, 2)
    print(cache.get(4) == -1)

    cache = LRUCache(2)
    cache.put(2, 1)
    cache.put(2, 2)
    print(cache.get(2) == 2)
    cache.put(1, 1)
    cache.put(4, 1)
    print(cache.get(2) == -1)
