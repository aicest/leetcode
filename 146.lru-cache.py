#
# @lc app=leetcode id=146 lang=python3
#
# [146] LRU Cache
#

# @lc code=start
class LRUCache:
    def __init__(self, quota: int):
        self.quota, self.used = quota, 0
        self.map = {}
        self.head, self.tail = "^", "$"
        self.next, self.prev = {}, {}
        self.next[self.head], self.prev[self.tail] = self.tail, self.head

    def __remove(self, key):
        self.next[self.prev[key]] = self.next[key]
        self.prev[self.next[key]] = self.prev[key]
        self.next.pop(key)
        self.prev.pop(key)

    def __insert(self, prev, key):
        self.next[prev], self.next[key] = key, self.next[prev]
        self.prev[key], self.prev[self.next[key]] = prev, key

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1
        self.__remove(key)
        self.__insert(self.head, key)
        return self.map[key]

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.__remove(key)
            self.used -= 1
        if self.used == self.quota:
            least = self.prev[self.tail]
            self.__remove(least)
            self.map.pop(least)
            self.used -= 1
        self.__insert(self.head, key)
        self.map[key] = value
        self.used += 1


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
