import heapq
from typing import List, Set


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        """
        method1: 使用堆排序
        T(n): O(nlog(n))
        S(n): O(n)
        """
        diff_set: Set = {1}
        rec_f: List[int] = [1]
        for _ in range(n - 1):
            val_popped = heapq.heappop(rec_f)
            for item in [val_popped * prime for prime in primes if val_popped * prime not in diff_set]:
                diff_set.add(item)
                heapq.heappush(rec_f, item)

        return heapq.heappop(rec_f)


if __name__ == "__main__":
    s = Solution()
    for i in range(1, 20):
        print(s.nthSuperUglyNumber(i, [2, 7, 13, 19]), end='\t')
