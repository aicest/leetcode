#
# @lc app=leetcode id=155 lang=python3
#
# [155] Min Stack
#

# @lc code=start
class MinStack:
    def __init__(self):
        self.arr = []
        self.min = [float("inf")]

    def push(self, x: int) -> None:
        self.arr.append(x)
        if x <= self.min[-1]:
            self.min.append(x)

    def pop(self) -> None:
        if self.arr.pop() == self.min[-1]:
            self.min.pop()

    def top(self) -> int:
        return self.arr[-1]

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
