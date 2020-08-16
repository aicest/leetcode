from __ListNode import *

#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 1. C = y + z
        # 2. F = 2*S
        # 3. F = x + y + n*C, n >= 1
        # 4. S = x + y
        # 5. 2+3+4 => x + y + n*C = 2*(x + y)
        # 6. 1+5 => x = (n-1)*C + z
        # 7. 6 => x = z, n = 1
        slow, fast = head, head
        while fast:
            fast = fast.next.next if fast.next else None
            slow = slow.next
            if fast == slow:
                break
        left, right = head, fast
        while left and right and left != right:
            left = left.next
            right = right.next
        return right


# @lc code=end

if __name__ == "__main__":

    def create(arr, pos):
        head, tail = ListNode.create(arr), None
        node = head
        while node:
            if pos == 0 and not tail:
                tail = node
            else:
                pos -= 1
            if node.next:
                node = node.next
            else:
                node.next = tail
                break
        return head

    print(2 == Solution().detectCycle(create([3, 2, 0, -4], 1)).val)
    print(1 == Solution().detectCycle(create([1, 2], 0)).val)
    print(2 == Solution().detectCycle(create([1, 2], 1)).val)
    print(1 == Solution().detectCycle(create([1], 0)).val)
    print(None == Solution().detectCycle(create([1], -1)))
    print(None == Solution().detectCycle(create([1, 2], -1)))
    print(None == Solution().detectCycle(create([1, 2, 3], -1)))
    print(None == Solution().detectCycle(create([1, 2, 3, 4], -1)))
    print(None == Solution().detectCycle(create([], 0)))
    print(None == Solution().detectCycle(create([], -1)))
