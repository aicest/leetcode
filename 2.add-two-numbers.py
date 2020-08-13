from __ListNode import *

#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = head = ListNode(None)
        carry = 0
        while l1 and l2:
            val = l1.val + l2.val + carry
            val, carry = val % 10, val // 10
            node.next = ListNode(val)
            node = node.next
            l1, l2 = l1.next, l2.next
        if l1:
            node.next = l1
        elif l2:
            node.next = l2
        while node.next and carry:
            val = node.next.val + carry
            val, carry = val % 10, val // 10
            node.next.val = val
            node = node.next
        if carry:
            node.next = ListNode(carry)
        return head.next


# @lc code=end

if __name__ == "__main__":
    create = ListNode.create
    result = Solution().addTwoNumbers(create([4]), create([6]))
    print(ListNode.format(result) == "0->1->NULL")
    result = Solution().addTwoNumbers(create([3, 9, 9, 9]), create([6]))
    print(ListNode.format(result) == "9->9->9->9->NULL")
    result = Solution().addTwoNumbers(create([4, 9, 9, 8]), create([6]))
    print(ListNode.format(result) == "0->0->0->9->NULL")
    result = Solution().addTwoNumbers(create([4, 9, 9, 9, 9]), create([6]))
    print(ListNode.format(result) == "0->0->0->0->0->1->NULL")
    result = Solution().addTwoNumbers(create([2, 4, 4]), create([5, 6]))
    print(ListNode.format(result) == "7->0->5->NULL")
    result = Solution().addTwoNumbers(create([2, 4]), create([5, 6, 4]))
    print(ListNode.format(result) == "7->0->5->NULL")
    result = Solution().addTwoNumbers(create([2, 4, 3]), create([5, 6, 4]))
    print(ListNode.format(result) == "7->0->8->NULL")
