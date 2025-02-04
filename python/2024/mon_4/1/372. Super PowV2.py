from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        # Calculate a^k mod 1337 for 0 <= k <= 9
        powers = [a ** k % MOD for k in range(10)]

        # Calculate (a^b) mod 1337
        res = 1
        for digit in b:
            res = (res ** 10) % MOD
            res = (res * powers[digit]) % MOD
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.superPow(133, [1, 2, 2, 4, 5, 5, 6, 7, 8, 8]))
