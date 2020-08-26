from typing import *

#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ht = {}
        for s in strs:
            ss = "".join(sorted(s))
            if ss not in ht:
                ht[ss] = []
            ht[ss].append(s)
        return list(ht.values())


# @lc code=end

if __name__ == "__main__":
    print(
        [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
        == Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    )
