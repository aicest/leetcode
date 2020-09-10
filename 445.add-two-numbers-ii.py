from __ListNode import *

#
# @lc app=leetcode id=445 lang=python3
#
# [445] Add Two Numbers II
#

# @lc code=start
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        m, node = 0, l1
        while node:
            m, node = m + 1, node.next
        n, node = 0, l2
        while node:
            n, node = n + 1, node.next
        if m < n:
            m, n = n, m
            l1, l2 = l2, l1
        head = node = ListNode(None)
        stack = []
        while m > n:
            m -= 1
            node.next = ListNode(l1.val)
            stack.append(node.next)
            node, l1 = node.next, l1.next
        while m:
            m -= 1
            node.next = ListNode(l1.val + l2.val)
            stack.append(node.next)
            node, l1, l2 = node.next, l1.next, l2.next
        carry = 0
        while stack:
            node = stack.pop()
            node.val, carry = (node.val + carry) % 10, (node.val + carry) // 10
        if carry:
            head.next = ListNode(carry, head.next)
        return head.next


# @lc code=end

if __name__ == "__main__":
    create = ListNode.create
    format = ListNode.format
    result = Solution().addTwoNumbers(create([7, 2, 4, 3]), create([5, 6, 4]))
    print("7->8->0->7->NULL" == format(result))
    result = Solution().addTwoNumbers(create([8, 9, 9, 4]), create([6]))
    print("9->0->0->0->NULL" == format(result))
    result = Solution().addTwoNumbers(create([9, 9, 9, 4]), create([6]))
    print("1->0->0->0->0->NULL" == format(result))
