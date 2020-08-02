class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def create(arr) -> "ListNode":
        head = ListNode(None)
        node = head
        for val in arr:
            node.next = ListNode(val)
            node = node.next
        return head.next

    @staticmethod
    def format(node):
        result = ""
        while node:
            result += str(node.val) + "->"
            node = node.next
        return result + "NULL"
