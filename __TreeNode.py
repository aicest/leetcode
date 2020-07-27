class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @staticmethod
    def create(nums):
        root = TreeNode(nums.pop(0)) if nums else None
        nodeList = [root] if root else None
        while nodeList:
            curr = nodeList.pop(0)
            leftVal = nums.pop(0) if nums else None
            rightVal = nums.pop(0) if nums else None
            curr.left = TreeNode(leftVal) if isinstance(leftVal, int) else None
            curr.right = TreeNode(rightVal) if isinstance(rightVal, int) else None
            if curr.left:
                nodeList.append(curr.left)
            if curr.right:
                nodeList.append(curr.right)
        return root
