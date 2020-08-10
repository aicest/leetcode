#
# @lc app=leetcode id=232 lang=python3
#
# [232] Implement Queue using Stacks
#

# @lc code=start
class MyQueue:
    def __init__(self):
        self.head, self.tail = "^", "$"
        self.next, self.prev = {}, {}
        self.next[self.head], self.prev[self.tail] = self.tail, self.head
        self.map = {}
        self.unique = 0

    def __insert(self, prev, key):
        self.next[prev], self.next[key] = key, self.next[prev]
        self.prev[key], self.prev[self.next[key]] = prev, key

    def __remove(self, key):
        self.next[self.prev[key]] = self.next[key]
        self.prev[self.next[key]] = self.prev[key]
        self.next.pop(key)
        self.prev.pop(key)

    def push(self, value: int) -> None:
        key = self.unique = self.unique + 1
        self.__insert(self.prev[self.tail], key)
        self.map[key] = value

    def pop(self) -> int:
        key = self.next[self.head]
        self.__remove(key)
        return self.map.pop(key)

    def peek(self) -> int:
        key = self.next[self.head]
        return self.map[key]

    def empty(self) -> bool:
        return len(self.map) == 0


# @lc code=end

if __name__ == "__main__":
    queue = MyQueue()
    queue.push(1)
    queue.push(2)
    print(queue.peek() == 1)
    print(queue.pop() == 1)
    print(queue.empty() == False)
    print(queue.pop() == 2)
    print(queue.empty() == True)
