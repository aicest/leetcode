from __ListNode import *

#
# @lc app=leetcode id=25 lang=python3
#
# [25] Reverse Nodes in k-Group
#

# @lc code=start
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        node = head
        start, i = node, 0
        head, tail = None, ListNode(None)
        while node:
            i += 1
            if i == k:
                node.next, node = None, node.next
                start, end = self.reverse(start)
                tail.next = start
                head, tail = head or start, end
                start, i = node, 0
            else:
                node = node.next
        tail.next = start
        return head

    def reverse(self, head: ListNode):
        prev = tail = head
        next, prev.next = prev.next, None
        while next:
            curr, next = next, next.next
            curr.next, prev = prev, curr
        return prev, tail


# @lc code=end

if __name__ == "__main__":
    create = ListNode.create
    result = Solution().reverseKGroup(create([]), 1)
    print("NULL" == ListNode.format(result))
    result = Solution().reverseKGroup(create([1]), 1)
    print("1->NULL" == ListNode.format(result))
    result = Solution().reverseKGroup(create([1, 2, 3, 4, 5]), 1)
    print("1->2->3->4->5->NULL" == ListNode.format(result))
    result = Solution().reverseKGroup(create([1, 2, 3, 4, 5]), 2)
    print("2->1->4->3->5->NULL" == ListNode.format(result))
    result = Solution().reverseKGroup(create([1, 2, 3, 4, 5]), 3)
    print("3->2->1->4->5->NULL" == ListNode.format(result))
    result = Solution().reverseKGroup(create([1, 2, 3, 4, 5]), 4)
    print("4->3->2->1->5->NULL" == ListNode.format(result))
    result = Solution().reverseKGroup(create([1, 2, 3, 4, 5]), 5)
    print("5->4->3->2->1->NULL" == ListNode.format(result))
