from __ListNode import *

#
# @lc app=leetcode id=141 lang=python3
#
# [141] Linked List Cycle
#

# @lc code=start
class Solution:
    def hasCycle(self, head):
        slow = head
        fast = slow.next if slow else None
        while slow and fast:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next if fast.next else None
        return False


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

    print(Solution().hasCycle(create([3, 2, 0, -4], 1)))
    print(Solution().hasCycle(create([1, 2], 0)))
    print(Solution().hasCycle(create([1], -1)))
    print(Solution().hasCycle(create([1], 0)))
    print(Solution().hasCycle(create([1, 2, 3, 2, 1], -1)))
