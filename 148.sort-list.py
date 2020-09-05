from __ListNode import *

#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#

# @lc code=start
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.ms(head)

    def ms(self, head, count=None):
        if not head or not head.next:
            return head
        if count == None:
            node, count = head, 0
            while node:
                node, count = node.next, count + 1
        leftCount = count + 1 >> 1
        rightCount = count - leftCount
        prev, curr, count = ListNode(None, head), head, leftCount
        while count:
            prev, curr, count = prev.next, curr.next, count - 1
        prev.next = None
        left, right = head, curr
        return self.m(self.ms(left, leftCount), self.ms(right, rightCount))

    def m(self, left, right):
        head = prev = ListNode(None)
        while left and right:
            if left.val <= right.val:
                prev.next, prev, left = left, left, left.next
            else:
                prev.next, prev, right = right, right, right.next
        prev.next = left or right
        return head.next


# @lc code=end

if __name__ == "__main__":
    create = ListNode.create
    result = Solution().sortList(create([]))
    print("NULL" == ListNode.format(result))
    result = Solution().sortList(create([1]))
    print("1->NULL" == ListNode.format(result))
    result = Solution().sortList(create([4, 2, 1, 3]))
    print("1->2->3->4->NULL" == ListNode.format(result))
    result = Solution().sortList(create([-1, 5, 3, 4, 0]))
    print("-1->0->3->4->5->NULL" == ListNode.format(result))
