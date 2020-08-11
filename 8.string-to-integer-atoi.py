#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    INT_MIN = -1 << 31
    INT_MAX = (1 << 31) - 1
    INT_MAP = dict(zip(map(str, range(10)), range(10)))

    def myAtoi(self, s: str) -> int:
        result = 0
        sign = 1
        state = "space"
        i, n = 0, len(s)
        while i < n:
            c = s[i]
            if state == "space":
                if c == " ":
                    i += 1
                else:
                    state = "sign"
            elif state == "sign":
                if c == "+":
                    state = "digit"
                    i += 1
                elif c == "-":
                    state = "digit"
                    i += 1
                    sign = -1
                else:
                    state = "digit"
            elif state == "digit":
                if c in self.INT_MAP:
                    result = result * 10 + self.INT_MAP[c]
                    i += 1
                else:
                    break
        result *= sign
        return max(min(result, self.INT_MAX), self.INT_MIN)


# @lc code=end

if __name__ == "__main__":
    print(0 == Solution().myAtoi(""))
    print(0 == Solution().myAtoi("+"))
    print(0 == Solution().myAtoi("-"))
    print(0 == Solution().myAtoi("-+"))
    print(0 == Solution().myAtoi("+-"))
    print(0 == Solution().myAtoi("-+1"))
    print(0 == Solution().myAtoi("+-1"))
    print(0 == Solution().myAtoi("+0 123"))
    print(0 == Solution().myAtoi("-0 123"))
    print(1 == Solution().myAtoi("+1 123"))
    print(-1 == Solution().myAtoi("-1 123"))
    print(0 == Solution().myAtoi("+0+123"))
    print(0 == Solution().myAtoi("-0+123"))
    print(1 == Solution().myAtoi("+1+123"))
    print(-1 == Solution().myAtoi("-1+123"))
    print(42 == Solution().myAtoi("42"))
    print(42 == Solution().myAtoi("    +42"))
    print(-42 == Solution().myAtoi("   -42"))
    print(0 == Solution().myAtoi("    --42"))
    print(0 == Solution().myAtoi("    ++42"))
    print(4193 == Solution().myAtoi("4193 with words"))
    print(0 == Solution().myAtoi("words and 987"))
    print(-2147483648 == Solution().myAtoi("-91283472332"))
    print(2147483647 == Solution().myAtoi("91283472332"))
    print(-2147483648 == Solution().myAtoi("-9128347233223233232232323222323232232"))
    print(2147483647 == Solution().myAtoi("9128347233223233232232323222323232232"))
