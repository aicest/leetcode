#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#

# @lc code=start
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 1:
            return 0
        ht = [1] * n
        ht[0] = ht[1] = 0
        for i in range(2, (n + 1) // 2):
            if ht[i] == 1:
                for j in range(i, (n + i - 1) // i):
                    ht[i * j] = 0
        return sum(ht)


# @lc code=end

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    print(0 == Solution().countPrimes(0))
    print(0 == Solution().countPrimes(1))
    print(0 == Solution().countPrimes(2))
    print(1 == Solution().countPrimes(3))
    print(2 == Solution().countPrimes(4))
    print(3 == Solution().countPrimes(6))
    print(3 == Solution().countPrimes(7))
    print(4 == Solution().countPrimes(10))
    print(6 == Solution().countPrimes(17))
    print(8 == Solution().countPrimes(23))
    print(41537 == Solution().countPrimes(499979))
    end = time.perf_counter()
    print(end - start)
