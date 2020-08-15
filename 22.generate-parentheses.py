from typing import *

#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # F[n] = dedup(sum{2*(n-1)+1, 2*(n-2)+1, ..., 2*1+1, 2*0+1})
        prev, portion = {"": True}, "()"
        for i in range(n):
            curr = {}
            for path in prev.keys():
                for k in range(2 * i + 1):
                    curr[path[0:k] + portion + path[k:]] = True
            prev = curr
        return list(prev)

    def dfs(self, parentheses, path, target):
        stack = []
        for portion in path:
            if portion == "(":
                stack.append(portion)
            elif not stack or stack.pop() != "(":
                return []
        if target == 0:
            return [path] if not stack else []
        result = []
        for paren in parentheses:
            result += self.dfs(parentheses, path + paren, target - 1)
        return result


# @lc code=end

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print([""] == Solution().generateParenthesis(0))
    print(["()"] == Solution().generateParenthesis(1))
    print(["(())", "()()"] == sorted(Solution().generateParenthesis(2)))
    # fmt: off
    print(["((()))", "(()())", "(())()", "()(())", "()()()"] == sorted(Solution().generateParenthesis(3)))
    print(["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"] == sorted(Solution().generateParenthesis(4)))
    # fmt: on
    Solution().generateParenthesis(5)
    Solution().generateParenthesis(6)
    Solution().generateParenthesis(7)
    Solution().generateParenthesis(8)
    Solution().generateParenthesis(9)
    end = time.perf_counter()
    print(end - start)
