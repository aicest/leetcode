from __ListNode import *

#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        node, count = head, 0
        while node:
            node, count = node.next, count + 1
        prev, curr = None, head
        n = count >> 1
        while n != 0:
            n -= 1
            curr.next, prev, curr = prev, curr, curr.next
        if count % 2 == 1:
            curr = curr.next
        left, right = prev, curr
        while left and right and left.val == right.val:
            left, right = left.next, right.next
        return not left and not right


# @lc code=end

if __name__ == "__main__":
    print(Solution().isPalindrome(ListNode.create([1])))
    print(Solution().isPalindrome(ListNode.create([1, 2])))
    print(Solution().isPalindrome(ListNode.create([1, 2, 2, 1])))
    print(Solution().isPalindrome(ListNode.create([1, 2, 1, 3, 1, 2, 1])))
    print(Solution().isPalindrome(ListNode.create([1, 2, 1, 3, 3, 1, 2, 1])))
