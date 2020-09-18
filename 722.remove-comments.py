from typing import *

#
# @lc app=leetcode id=722 lang=python3
#
# [722] Remove Comments
#

# @lc code=start
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        state = "plain"
        text = ""
        wrap = True
        for line in source:
            i, n = 0, len(line)
            while i < n:
                if state == "plain":
                    if line[i : i + 2] == "/*":
                        state = "block-comment"
                        wrap = False
                        i += 2
                    elif line[i : i + 2] == "//":
                        state = "inline-comment"
                    else:
                        text += line[i]
                        i += 1
                elif state == "block-comment":
                    if line[i : i + 2] == "*/":
                        state = "plain"
                        wrap = True
                        i += 2
                    else:
                        i += 1
                elif state == "inline-comment":
                    state = "plain"
                    break
            if text and wrap:
                result.append(text)
                text = ""
        return result


# @lc code=end

if __name__ == "__main__":
    result = Solution().removeComments(["", "int main() { }", ""])
    print(result == ["int main() { }"])
    result = Solution().removeComments(["", "int main() {", "/**/", "}", ""])
    print(result == ["int main() {", "}"])
    result = Solution().removeComments(["", "int main() {", "", "/**/", "", "}", ""])
    print(result == ["int main() {", "}"])
    result = Solution().removeComments(["int main() {", "/*//*/", "}"])
    print(result == ["int main() {", "}"])
    result = Solution().removeComments(["int main() {", "int a=0;///**/int b=0;", "}"])
    print(result == ["int main() {", "int a=0;", "}"])
    result = Solution().removeComments(["int main() {/*", "*/", "}"])
    print(result == ["int main() {", "}"])
    result = Solution().removeComments(
        [
            "/*Test program */",
            "int main()",
            "{ ",
            "  // variable declaration ",
            "int a, b, c;",
            "/* This is a test",
            "   multiline  ",
            "   comment for ",
            "   testing */",
            "a = b + c;",
            "}",
        ]
    )
    print(result == ["int main()", "{ ", "  ", "int a, b, c;", "a = b + c;", "}"])
    result = Solution().removeComments(["a/*comment", "line", "more_comment*/b"])
    print(result == ["ab"])
    result = Solution().removeComments(
        [
            "struct Node{",
            "    /*/ declare members;/**/",
            "    int size;",
            "    /**/int val;",
            "};",
        ]
    )
    print(result == ["struct Node{", "    ", "    int size;", "    int val;", "};"])
    result = Solution().removeComments(["a/*/b//*c", "blank", "d/*/e*//f"])
    print(result == ["ae*"])
    result = Solution().removeComments(["a/*b*/c/*d*/e//f"])
    print(result == ["ace"])
    result = Solution().removeComments(["a/*b*/c/*d*/e/*f*/g//h/*i*/"])
    print(result == ["aceg"])
    result = Solution().removeComments(["a//", "b"])
    print(result == ["a", "b"])
