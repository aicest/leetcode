#
# @lc app=leetcode id=567 lang=python3
#
# [567] Permutation in String
#

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ht1, ht2 = {}, {}
        for c in s1:
            ht1[c] = ht1[c] + 1 if c in ht1 else 1
        i, j, n = 0, 0, len(s2)
        while j < n:
            c = s2[j]
            if c in ht1:
                ht2[c] = ht2[c] + 1 if c in ht2 else 1
                while ht2[s2[i]] > ht1[s2[i]]:
                    ht2[s2[i]] -= 1
                    i += 1
                if ht2 == ht1:
                    return True
            else:
                ht2 = {}
                i = j + 1
            j += 1
        return False


# @lc code=end

if __name__ == "__main__":
    print(Solution().checkInclusion("dxd", "ddx"))
    print(Solution().checkInclusion("dxde", "dedx"))
    print(Solution().checkInclusion("abc", "eidbacooo"))
    print(not Solution().checkInclusion("abc", "eidbaacooo"))
    print(Solution().checkInclusion("ab", "eidbaooo"))
    print(not Solution().checkInclusion("ab", "eidboaoo"))
    print(Solution().checkInclusion("abcdxabcde", "abcdeabcdx"))
