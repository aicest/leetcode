#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        pair = {")": "(", "]": "[", "}": "{"}
        stack = []
        for c in s:
            if c not in pair:
                stack.append(c)
            elif not stack or stack.pop() != pair[c]:
                return False
        return not stack


# @lc code=end

if __name__ == "__main__":
    print(Solution().isValid(""))
    print(not Solution().isValid("("))
    print(Solution().isValid("()"))
    print(Solution().isValid("()[]{}"))
    print(not Solution().isValid("(]"))
    print(not Solution().isValid("([)]"))
    print(Solution().isValid("{[]}"))
