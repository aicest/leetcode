#
# @lc app=leetcode id=60 lang=python3
#
# [60] Permutation Sequence
#

# @lc code=start
class Solution:
    def getPermutation(self, n, k):
        k, path = self.dfs(list(range(1, n + 1)), [], n, k, {0: 1, 1: 1, 2: 2})
        return "".join(map(str, path))

    def dfs(self, arr, path, n, k, dp):
        j = len(arr)
        m = dp[j - 1] if j - 1 in dp else self.factorial(j - 1, dp)
        for i in range(j):
            if m < k:
                k -= m
                continue
            curr = path + [arr[i]]
            if len(curr) == n:
                return k - 1, curr
            k, curr = self.dfs(arr[0:i] + arr[i + 1 : n], curr, n, k, dp)
            if k == 0:
                return k, curr
        return k, []

    def factorial(self, n, dp):
        if n not in dp:
            dp[n] = n * self.factorial(n - 1, dp)
        return dp[n]


# @lc code=end

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(Solution().getPermutation(3, 3))
    print(Solution().getPermutation(4, 9))
    print(Solution().getPermutation(8, 27428))
    print(Solution().getPermutation(9, 116907))
    print(Solution().getPermutation(9, 362880))
    print(Solution().getPermutation(8, 27428))
    print(Solution().getPermutation(9, 116907))
    print(Solution().getPermutation(9, 362880))
    print(Solution().getPermutation(8, 27428))
    print(Solution().getPermutation(9, 116907))
    print(Solution().getPermutation(9, 362880))
    print(Solution().getPermutation(8, 27428))
    print(Solution().getPermutation(9, 116907))
    print(Solution().getPermutation(9, 362880))
    end = time.perf_counter()
    print(end - start)
