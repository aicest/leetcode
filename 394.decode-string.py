#
# @lc app=leetcode id=394 lang=python3
#
# [394] Decode String
#

# @lc code=start
class Solution:
    def decodeString(self, s: str) -> str:
        # https://docs.python.org/3/library/stdtypes.html#str.isalnum
        # https://blog.csdn.net/zhangchen124/article/details/81630631
        stack = [""]
        state = "alpha"
        for c in s:
            if c == "[":
                stack.append("")
                state = "alpha"
            elif c == "]":
                alpha = stack.pop()
                digit = int(stack.pop())
                stack[-1] += digit * alpha
            elif state == "alpha" and c.isdecimal():
                stack.append(c)
                state = "digit"
            else:
                stack[-1] += c
        return stack[0]


# @lc code=end

if __name__ == "__main__":
    print("cccccc" == Solution().decodeString("03[02[c]]"))
    print("accaccacc" == Solution().decodeString("03[a02[c]]"))
    print("abcbc" == Solution().decodeString("01[a]2[bc]"))
    print("aaaaaaaaaabcbc" == Solution().decodeString("10[a]2[bc]"))
    print("aaabcbc" == Solution().decodeString("3[a]2[bc]"))
    print("accaccacc" == Solution().decodeString("3[a2[c]]"))
    print("abcabccdcdcdef" == Solution().decodeString("2[abc]3[cd]ef"))
    print("abccdcdcdxyz" == Solution().decodeString("abc3[cd]xyz"))
