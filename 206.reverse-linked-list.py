#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
class Solution:
    def reverseList(self, head):
        tail = None
        while head:
            node = head
            head = head.next
            node.next = tail
            tail = node
        return tail

    def traverse(self, node):
        if not node.next:
            return node, node
        head, tail = self.traverse(node.next)
        tail.next = node
        node.next = None
        return head, node


# @lc code=end

from __ListNode import *

if __name__ == "__main__":
    create = ListNode.create
    format = ListNode.format
    print("3->2->1->NULL" == format(Solution().reverseList(create([1, 2, 3]))))
    print("2->1->NULL" == format(Solution().reverseList(create([1, 2]))))
    print("1->NULL" == format(Solution().reverseList(create([1]))))
    print("NULL" == format(Solution().reverseList(create([]))))
