#
# @lc app=leetcode id=71 lang=python3
#
# [71] Simplify Path
#

# @lc code=start
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for portion in path.split("/"):
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or portion == "":
                pass
            else:
                stack.append(portion)
        result = "/".join(stack)
        return "/" + result


# @lc code=end

if __name__ == "__main__":
    print("/home" == Solution().simplifyPath("/home/"))
    print("/" == Solution().simplifyPath("/../"))
    print("/home/foo" == Solution().simplifyPath("/home//foo/"))
    print("/c" == Solution().simplifyPath("/a/./b/../../c/"))
    print("/c" == Solution().simplifyPath("/a/../../b/../c//.//"))
    print("/a/b/c" == Solution().simplifyPath("/a//b////c/d//././/.."))
