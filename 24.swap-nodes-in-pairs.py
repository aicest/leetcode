from __ListNode import *

#
# @lc app=leetcode id=24 lang=python3
#
# [24] Swap Nodes in Pairs
#

# @lc code=start
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        head = ListNode(None, head)
        prev, curr = head, head.next
        while curr and curr.next:
            node = curr.next.next
            prev.next = curr.next
            prev.next.next = curr
            curr.next = node
            prev, curr = curr, curr.next
        return head.next


# @lc code=end

if __name__ == "__main__":
    result = Solution().swapPairs(ListNode.create([]))
    print(ListNode.format(result) == "NULL")
    result = Solution().swapPairs(ListNode.create([1]))
    print(ListNode.format(result) == "1->NULL")
    result = Solution().swapPairs(ListNode.create([1, 2, 3, 4]))
    print(ListNode.format(result) == "2->1->4->3->NULL")
