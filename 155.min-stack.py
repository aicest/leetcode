#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    def __init__(self):
        self.min = [float("inf")]
        self.node, self.prev, self.next = {}, {}, {}
        self.id, self.head, self.tail = -1, "^", "$"
        self.prev[self.tail] = self.head
        self.next[self.head] = self.tail

    def __remove(self, key):
        self.node.pop(key)
        self.prev[self.next[key]] = self.prev[key]
        self.next[self.prev[key]] = self.next[key]
        self.prev.pop(key)
        self.next.pop(key)

    def __insert(self, prev, value):
        key = self.id = self.id + 1
        self.node[key] = value
        self.prev[key] = prev
        self.next[key] = self.next[prev]
        self.prev[self.next[prev]] = key
        self.next[prev] = key

    def push(self, value: int) -> None:
        self.__insert(self.prev[self.tail], value)
        if value <= self.min[-1]:
            self.min.append(value)

    def pop(self) -> None:
        key = self.prev[self.tail]
        value = self.node[key]
        self.__remove(key)
        if value == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.node[self.prev[self.tail]]

    def getMin(self) -> int:
        return self.min[-1]


# @lc code=end

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin() == -3)
    minStack.pop()
    print(minStack.top() == 0)
    print(minStack.getMin() == -2)
    minStack.push(-3)
    minStack.pop()
    minStack.push(-3)
    print(minStack.getMin() == -3)
    minStack.pop()
    minStack.push(-2)
    print(minStack.getMin() == -2)
    minStack.pop()
    print(minStack.getMin() == -2)

    minStack = MinStack()
    minStack.push(2)
    minStack.push(0)
    minStack.push(3)
    minStack.push(0)
    print(minStack.getMin() == 0)
    minStack.pop()
    print(minStack.getMin() == 0)
    minStack.pop()
    print(minStack.getMin() == 0)
    minStack.pop()
    print(minStack.getMin() == 2)
