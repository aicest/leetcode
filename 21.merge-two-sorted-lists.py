from __ListNode import *

#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = head = ListNode(None)
        while l1 and l2:
            if l1.val <= l2.val:
                node.next, node, l1 = l1, l1, l1.next
            else:
                node.next, node, l2 = l2, l2, l2.next
        if l1:
            node.next = l1
        if l2:
            node.next = l2
        return head.next


# @lc code=end

if __name__ == "__main__":
    l1 = ListNode.create([])
    l2 = ListNode.create([1])
    l3 = Solution().mergeTwoLists(l1, l2)
    print(ListNode.format(l3) == "1->NULL")

    l1 = ListNode.create([1])
    l2 = ListNode.create([1, 2, 3])
    l3 = Solution().mergeTwoLists(l1, l2)
    print(ListNode.format(l3) == "1->1->2->3->NULL")

    l1 = ListNode.create([1, 2, 4])
    l2 = ListNode.create([1, 3, 4])
    l3 = Solution().mergeTwoLists(l1, l2)
    print(ListNode.format(l3) == "1->1->2->3->4->4->NULL")
