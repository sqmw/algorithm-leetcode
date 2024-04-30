from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """
        method2: 动态规划，多指针
        T(n): O(n)
        S(n): O(n)

        rec_f[i] == prime * math.ceil(rec_f[i - 1] / prime) # 需要对每一个 prime 都进行这样的操作，最后取最小的 rec_f[i]
        """
        prime_index_list: List[int] = [0] * len(primes)
        rec_f: List[int] = [1] * (n + 1)
        product_list: List[int] = [1] * len(primes)
        for i in range(1, n + 1):
            rec_f[i] = min(product_list)
            # 这里的时间复杂度是 O(len(primes)) 是一个常量
            for j in range(len(primes)):
                if product_list[j] == rec_f[i]:
                    prime_index_list[j] += 1
                    product_list[j] = rec_f[prime_index_list[j]] * primes[j]
        return rec_f[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.nthSuperUglyNumber(12000000, [2, 7, 13, 19]), end='\t')
